from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDeleteView, PurchaseListCreateView, PurchaseRetrieveUpdateDeleteView


urlpatterns = [
    path('vendor/', VendorListCreateView.as_view(), name='vendorLC'),
    path('vendor/<int:vendor_id>/',  VendorRetrieveUpdateDeleteView.as_view(), name="vendorRUD"),
    path('vendors/<int:vendor_id>/performance/', VendorRetrieveUpdateDeleteView.as_view({'get': 'performance'}), name='vendorRUD'),

    path('purchase_orders/', PurchaseListCreateView.as_view(), name='purchaserLC'),
    path('purchase_orders/<int:po_id>/',  PurchaseRetrieveUpdateDeleteView.as_view(), name="purchaseRUD"),
    path('purchases/<int:po_id>/acknowledge/', PurchaseListCreateView.as_view({'post': 'acknowledge'}), name='purchase-acknowledge'),


]