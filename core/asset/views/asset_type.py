from ..models.asset_type import AssetType
from django.urls import reverse_lazy
from ..forms import CreateAssetTypeForm
from base.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseListView,  BaseDetailView
from ..filters import AssetTypeFilters


class AssetTypeListView(BaseListView):
    model = AssetType
    template_name = "asset/type/list.html"
    context_object_name = "type"
    filterset_class = AssetTypeFilters
    permission_required = "asset.view_assettype"


class AssetTypeDetailView(BaseDetailView):
    model = AssetType
    template_name = "asset/type/detail.html"
    permission_required = "asset.change_assettype"

class AssetTypeCreateView(BaseCreateView):
    model = AssetType
    template_name = "asset/type/create.html"
    form_class = CreateAssetTypeForm
    permission_required = "asset.add_assettype"
    success_message = "Type Successfully Created."
    url = "asset:type_detail"


class AssetTypeUpdateView(BaseUpdateView):
    model = AssetType
    template_name = "asset/type/update.html"
    permission_required = "asset.change_assettype"
    success_message = "Type Successfully Updated."
    context_object_name = 'asset_type'
    fields = (
        "name",
        "description",
        "is_active",
    )
    url = "asset:type_detail"


class AssetTypeDeleteView(BaseDeleteView):
    model = AssetType
    template_name = "asset/type/delete.html"
    success_url = reverse_lazy("asset:type_list")
    permission_required = "asset.delete_assettype"
    message = "Type Successfully Deleted"
