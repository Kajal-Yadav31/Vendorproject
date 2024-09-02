from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status, generics
from django.utils import timezone
from rest_framework.response import Response
from .models import Vendor, Purchase, HisPerformance
from .serializers import VendorSerializer, PurchaseSerializer, HisPerformanceSerializer


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'vendor_id'

    @action(detail=True, methods=['get'])
    def performance(self, request, *args, **kwargs):
        vendor = self.get_object()

        # Calculate performance metrics
        completed_orders = vendor.purchase_set.filter(status='completed')
        on_time_deliveries = completed_orders.filter(delivery_date__lte=F('delivery_date')).count()
        total_orders = completed_orders.count()
        on_time_delivery_rate = (on_time_deliveries / total_orders) * 100 if total_orders else 0

        # Assuming quality_rating_avg and average_response_time are methods or properties on Vendor
        current_performance = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': vendor.get_quality_rating_avg(),
            'average_response_time': vendor.get_average_response_time(),
            'fulfillment_rate': vendor.get_fulfillment_rate(),
        }

        # Fetch historical performance data
        historical_performance = HisPerformance.objects.filter(vendor=vendor).values(
            'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate'
        )

        return Response({
            'current_performance': current_performance,
            'historical_performance': list(historical_performance)
        })


class PurchaseListCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get('vendor', None)

        if vendor_id is not None:
            queryset = queryset.filter(vendor__vendor_id = vendor_id)

        return queryset

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, *args, **kwargs):
        po = self.get_object()
        po.acknowledgment_date = timezone.now()
        po.save()  # Ensure that saving the PurchaseOrder triggers the metric update

        # Assuming the Vendor model has a method to recalculate the metrics
        po.vendor.calculate_metrics()
        po.vendor.save()

        return Response({
            'status': 'Acknowledgment updated',
            'average_response_time': po.vendor.get_average_response_time()
        })


class PurchaseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    lookup_field = 'po_id'






