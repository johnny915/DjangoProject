# Generated by Django 3.1.3 on 2021-02-12 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(auto_now=True)),
                ('product_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
        ),
    ]
