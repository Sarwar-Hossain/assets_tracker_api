# Generated by Django 4.2 on 2023-04-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default=None, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('identifier', models.CharField(editable=False, max_length=255, unique=True)),
                ('device_img', models.ImageField(blank=True, null=True, upload_to='device_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default=None, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default=None, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_tracker_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=150)),
                ('mobile_no', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('employee_image', models.ImageField(blank=True, null=True, upload_to='employee_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default=None, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default=None, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_tracker_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('expected_return_date', models.DateTimeField()),
                ('condition_on_checkout', models.CharField(max_length=255)),
                ('condition_on_return', models.CharField(max_length=255, null=True)),
                ('return_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default=None, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default=None, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_tracker_app.company')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_tracker_app.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_tracker_app.employee')),
            ],
            options={
                'unique_together': {('employee', 'device', 'checkout_date')},
            },
        ),
    ]
