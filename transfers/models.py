from django.db import models

# Create your models here.

# Make transfers between accounts


class Transfer(models.Model):
    sender = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="receiver"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    # substract the amount from the sender's account
    def send(self):
        self.sender.account.balance -= self.amount
        self.sender.account.save()

    # add the amount to the receiver's account
    def receive(self):
        self.receiver.account.balance += self.amount
        self.receiver.account.save()

    # save the transfer
    def save(self, *args, **kwargs):
        self.send()
        self.receive()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.amount}"
