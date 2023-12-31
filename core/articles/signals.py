from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    ShareArticle,
    CommentShareArticle,
    Article,
    ArticleApprovalStatus,
    PendingArticle,
)


@receiver(post_save, sender=ShareArticle)
def send_mail_shared_articles(sender, instance, created, **kwargs):
    if created:
        subject = f"{instance.sender} share a Document with you"
        message = f"{instance.article.title}, {instance.content}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            instance.recipient,
        ]
        send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=CommentShareArticle)
def send_mail_post_comment_to_articles(sender, instance, created, **kwargs):
    if created:
        if instance.sender == instance.share_article.sender:
            subject = f"{instance.sender} write a new comment in {instance.share_article.article.title} for  you"
            message = instance.content
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [
                instance.share_article.recipient,
            ]
            send_mail(subject, message, from_email, recipient_list)
        elif instance.sender == instance.share_article.recipient:
            subject = f"{instance.sender} write a new comment in {instance.share_article.article.title} for  you"
            message = instance.content
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [
                instance.share_article.sender,
            ]
            send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=PendingArticle)
def article_send_to_approve_box(sender, instance, created, **kwargs):
    if created:
        instance.approval_status = ArticleApprovalStatus.objects.get(name="Pending")
        instance.save()


@receiver(post_save, sender=PendingArticle)
def delete_after_approved(sender, instance, created, **kwargs):
    if instance.approval_status == ArticleApprovalStatus.objects.get(name="Approved"):
        PendingArticle.objects.get(id=instance.pk).delete()
