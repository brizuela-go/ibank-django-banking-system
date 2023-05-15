from django.contrib import admin

from .models import User, UserAddress, UserBankAccount
# from .models import BankAccountType


# admin.site.register(BankAccountType)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)
