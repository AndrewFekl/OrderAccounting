from django.db import models

class Customer(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Orders(models.Model):
    description = models.CharField(max_length=500, null=True, blank=True)
    amount = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.description




