# Generated by Django 2.1.5 on 2021-11-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='taxa_entrega',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
