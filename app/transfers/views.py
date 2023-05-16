from django.shortcuts import render
from .forms import TransferForm
from django.contrib import messages
from .models import Transfer
from django.views import View

# Create your views here.

class TransferView(View):
    
    def get(self, request, *args, **kwargs):
        form = TransferForm()
        context = {'form': form}
        return render(request, 'transactions/transfer_form.html', context)
    