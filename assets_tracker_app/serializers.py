from rest_framework import serializers
from assets_tracker_app.models import *
from rest_framework.response import Response
from rest_framework import status


# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def save(self):
        password = self.validated_data['password']

        if len(password) >= 6:
            raise serializers.ValidationError({'error': 'Password should be 6 digits!'})

        if Company.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exits!'})

        company = Company(company_name=self.validated_data['company_name'],
                          password=self.validated_data['password'],
                          phone_number=self.validated_data['phone_number'],
                          email=self.validated_data['email'],
                          address=self.validated_data['address'])
        company.save()
        return company


# Company Login Serializer
class CompanyLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(style={'input_type': 'email'})
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = Company
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                company = Company.objects.get(email=email, password=password)
                company_serializer = CompanySerializer(company)

                employee = Employee.objects.filter(company_id=company.id)
                employee_serializer = EmployeeSerializer(employee, many=True)
                device = Device.objects.filter(company_id=company.id)
                device_serializer = DeviceSerializer(device, many=True)
                device_log = DeviceLog.objects.filter(company_id=company.id)
                device_log_serializer = DeviceLogSerializer(device_log, many=True)

            except Company.DoesNotExist:
                return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            if company:
                if company.is_active:
                    data = {
                        'success': True,
                        'message': 'Login Successful!',
                        'company': company_serializer.data,
                        'employee': employee_serializer.data,
                        'device': device_serializer.data,
                        'device_log': device_log_serializer.data,
                    }
                    return data
                else:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')


# Device Serializer
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# Device Serializer
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
