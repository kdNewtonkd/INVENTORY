# Generated by Django 4.2.4 on 2023-08-22 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]