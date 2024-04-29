# Generated by Django 5.0.1 on 2024-04-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('CF', 'Coffee'), ('SNK', 'Snacks'), ('BVG', 'Beverages')], max_length=3)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]