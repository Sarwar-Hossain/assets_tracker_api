from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from assets_tracker_app.models import *
from assets_tracker_app.serializers import *
from rest_framework.views import APIView


# Create your views here.

class CompanyAV(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
