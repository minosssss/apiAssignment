from rest_framework import serializers
from rest_framework.fields import ChoiceField

from accountBook.models import Record, Payment, Category
from users.serializer import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'name','group')
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        payment = Payment.objects.create(**validated_data, user=request.user)
        return payment

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('type',)


class RecordSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    category = CategorySerializer()

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id', 'user',)

    def create(self, validated_data):
        request = self.context.get("request")
        payment = validated_data.get('payment')['name']
        category = validated_data.get('category')['type']
        classification = validated_data.get('classification')
        amout = validated_data.get('amout')
        note = validated_data.get('note')
        status = validated_data.get('status')
        record = Record.objects.create(
            payment = Payment.objects.get(name=payment),
            category = Category.objects.get(type=category),
            classification = classification,
            amout = amout,
            note = note,
            status = status,
            user=request.user)
        return record

