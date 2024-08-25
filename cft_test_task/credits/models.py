from django.db import models

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Manufacturer(TimestampModel):
    name = models.CharField(max_length=255)


class Product(TimestampModel):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    credit_application = models.ForeignKey("CreditApplication", related_name="product", on_delete=models.CASCADE)


class Contract(TimestampModel):
    number = models.CharField(max_length=255)


class CreditApplication(TimestampModel):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="credit_application"
    )
