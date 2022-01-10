from rest_framework import serializers

from accountBook.models import Record, Payment, Account
from users.serializer import UserSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        exclude = ("id",)

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ("id", "user",)

    def validate(self, data):
        return data


class RecordSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = serializers.StringRelatedField()
    payment = serializers.StringRelatedField()
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ("id", "user",)

    def validate(self, data):
        return data
