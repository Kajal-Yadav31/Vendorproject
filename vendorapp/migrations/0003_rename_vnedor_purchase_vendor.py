# Generated by Django 5.0.6 on 2024-08-28 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0002_remove_purchase_id_purchase_po_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='vnedor',
            new_name='vendor',
        ),
    ]
