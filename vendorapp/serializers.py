from rest_framework import serializers
from .models import Vendor, Purchase, HisPerformance

class VendorSerializer(serializers.ModelSerializer):
    vendor_id = serializers.ReadOnlyField()
    on_time_delivery_rate = serializers.ReadOnlyField()
    quantity_rating_avg = serializers.ReadOnlyField()
    average_response_time = serializers.ReadOnlyField()
    fulfillment_rate = serializers.ReadOnlyField()

    class Meta:
        model = Vendor
        fields = ['vendor_id',
            'name',
            'contact_details',
            'address',
            'vendor_code',
            'on_time_delivery_rate',
            'quantity_rating_avg',
            'average_response_time',
            'fulfillment_rate']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class HisPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HisPerformance
        fields = '__all__'