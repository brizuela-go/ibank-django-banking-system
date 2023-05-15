from accounts.models import UserBankAccount, UserAddress
from rest_framework import serializers
from transactions.models import Transaction

class UBA_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBankAccount
        exclude = ['user', 'account_no', 'balance', 'interest_start_date', 'initial_deposit_date']

class UserAdressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account']
