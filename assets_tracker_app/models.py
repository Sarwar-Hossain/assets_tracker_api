from django.db import models
import uuid


class Company(models.Model):
    company_name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=150, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=255, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.company_name


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255, unique=True, editable=False)
    device_img = models.ImageField(upload_to='device_images', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=255, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.device_name

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = str(uuid.uuid4())
        super(Device, self).save(*args, **kwargs)


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    password = models.CharField(max_length=150, null=False)
    mobile_no = models.CharField(max_length=20, null=False, unique=True, blank=False)
    email = models.CharField(max_length=50, null=True)
    employee_image = models.ImageField(upload_to='employee_images', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=255, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.employee_name


class DeviceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    expected_return_date = models.DateTimeField()
    condition_on_checkout = models.CharField(max_length=255)
    condition_on_return = models.CharField(max_length=255, null=True)
    return_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=255, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.CharField(max_length=255, null=True, default=None)

    class Meta:
        unique_together = ['employee', 'device', 'checkout_date']

    def __str__(self):
        return self.employee
