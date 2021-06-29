from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer





class CustomerList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return  Response(serializer.data)
    def post(self):
        pass