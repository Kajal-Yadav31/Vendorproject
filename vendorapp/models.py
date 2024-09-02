from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quantity_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def performance_metrics(self):
        completed_po = Purchase.objects.filter(vendor =self, stauts='completed')
        total_orders = completed_po.count()

        if total_orders > 0:
            on_time_deliveries = completed_po.filter(delivery_date__lte=models.F('delivery_date')).count
            on_time_delivery_rate = on_time_deliveries / total_orders * 100

            total_quality_rating = completed_po.aggregate(total=models.Sum('quanlity_rating'))['total']
            quality_rating_avg = total_quality_rating / total_orders if total_quality_rating else 0.0

            fulfillment_rate = total_orders / Purchase.objects.filter(vendor=self).count()

            self.on_time_delivery_rate = on_time_delivery_rate
            self.quality_rating_avg = quality_rating_avg
            self.fulfillment_rate = fulfillment_rate
            self.save

            HisPerformance.objects.create(vendor=self, on_time_delivery_rate=on_time_delivery_rate, quality_rating_avg=quality_rating_avg, average_response_time = self.average_responce_time, fulfillment_rate = fulfillment_rate )




class Purchase(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    quanlity_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknoeledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


class HisPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quantity_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


