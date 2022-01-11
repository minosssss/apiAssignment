from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accountBook.models import Record, Payment
from accountBook.serializers import RecordSerializer, PaymentSerializer

class RecordViewSet(ModelViewSet):

    serializer_class = RecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            records = Record.objects.all().order_by('-date')
        else:
            records = Record.objects.filter(user=user.pk)
        return records

    def get_permissions(self):
        if self.action == "delete":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    @action(detail=False) #action = url_path
    def search(self, request):
        print(request.GET.get)
        payment = request.GET.get("payment", None)
        category = request.GET.get("category", None)
        classification = request.GET.get("classification", None) #1 수입, 2 지출
        date = request.GET.get("date", None) #지정날짜
        date_from = request.GET.get("date_from", None) #부터~
        date_to = request.GET.get("date_to", None) #~까지
        amout_lte = request.GET.get("amout_down", None) #보다 아래
        amout_gte = request.GET.get("amout_up", None) #보다 위
        note = request.GET.get("note", None) #포함하는
        status = request.GET.get("status", None) #2 = False = 삭제
        filter_kwargs = {}
        if payment is not None:
            filter_kwargs["payment__name"] = payment
        if category is not None:
            filter_kwargs["category__type"] = category
        if classification is not None:
            filter_kwargs["classification"] = classification
        if date is not None:
            filter_kwargs["date"] = date
        if date_from and date_to is not None:
            filter_kwargs["date__range"] = date_from, date_to
        if amout_lte is not None:
            filter_kwargs["amout__lte"] = amout_lte
        if amout_gte is not None:
            filter_kwargs["amout__gte"] = amout_gte
        if note is not None:
            filter_kwargs["note__istartswith"] = note
        if status is not None:
            filter_kwargs["status"] = status
        paginator = self.paginator
        try:
            records = Record.objects.filter(**filter_kwargs)
        except ValueError:
            records = Record.objects.all()
        results = paginator.paginate_queryset(records, request)
        serializer = RecordSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        payments = Payment.objects.filter(user=user.pk)
        return payments

