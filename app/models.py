from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='cars')

    brand = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.brand} ({self.license_plate})"


class Fine(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='fines')

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.car} - {self.amount}"
        