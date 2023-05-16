from django.shortcuts import render
from .forms import TransferForm
from django.contrib import messages
from .models import Transfer

# Create your views here.

class TransferView():
    
    def get(self, request, *args, **kwargs):
        form = TransferForm()
        context = {'form': form}
        return render(request, 'transactions/transfer_form.html', context)
    