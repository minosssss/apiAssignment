from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from accountBook.models import Record, Payment
from accountBook.serializers import RecordSerializer, PaymentSerializer, AccountSerializer


class PaymentView(APIView):
    def get(self, request):
        user = request.user
        payments = Payment.objects.filter(user_id=user.pk)
        serializers = PaymentSerializer(payments, many=True).data
        return Response(serializers)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save(user=request.user)
            payment_serializer = PaymentSerializer(payment).data
            return Response(data=payment_serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Failed"})

class RecordView(APIView):
    def get(self, request):
        user = request.user
        records = Record.objects.filter(user_id=user.pk)
        serializers = RecordSerializer(records, many=True).data
        return Response(serializers)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save(user=request.user)
            record_serializer = RecordSerializer(record).data
            return Response(data=record_serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Failed"})