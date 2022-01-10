from rest_framework import serializers
from rest_framework.fields import ChoiceField

from accountBook.models import Record, Payment, Category
from users.serializer import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('name', 'group')
        read_only_fields = ("id",)


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('type',)


class RecordSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    payment = PaymentSerializer()
    category = CategorySerializer()

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ("id",)


