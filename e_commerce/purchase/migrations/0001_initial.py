# Generated by Django 4.1 on 2024-05-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('order_id', models.CharField(max_length=1200, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_id', models.CharField(max_length=150)),
            ],
        ),
    ]