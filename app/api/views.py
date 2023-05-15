from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import UserBankAccount, UserAddress
from transactions.models import Transaction
from .serializers import UBA_Serializer, UserAdressSerializer, TransactionSerializer

# Create your views here.
class UBA_ViewSet(viewsets.ModelViewSet):
    queryset = UserBankAccount.objects.all()
    serializer_class = UBA_Serializer

class TransactionViewSet(APIView):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions)
        return Response(serializer.data, status=status.HTTP_200_OK)
