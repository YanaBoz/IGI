from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal

#PromoCode
class PromoCode(models.Model):
     code = models.CharField(max_length=20, unique=True)
     description = models.CharField(max_length=255)
     discount_type = models.CharField(max_length=20, choices=(
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
     ), default='percentage')
     discount_value = models.DecimalField(max_digits=5, decimal_places=2)

     def str(self):
         return self.code
     
# Room Categories
class RoomCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2) 

    def str(self):
        return self.name

# Rooms
class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)

    def is_available(self, arrival_date, departure_date):
        """Checks if the room is available for the given dates."""
        reservations = Reservation.objects.filter(
            room=self,
            arrival_date__lte=departure_date,
            departure_date__gte=arrival_date
        ).exclude(pk=self.pk)  # Exclude the current reservation if updating
        return not reservations.exists()

    def calculate_price(self, arrival_date, departure_date):
        """Calculates the price for the room based on the dates."""
        nights = (departure_date - arrival_date).days
        base_price = self.category.price * nights
        # ... (Add any additional price logic, like weekend surcharges) ...
        return Decimal(base_price).quantize(Decimal('0.00'))

# Clients
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    has_child = models.BooleanField(default=False)

    def str(self):
        return f"{self.first_name} {self.last_name}"

# Reservations
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    notes = models.TextField(blank=True)  # Add the 'notes' field
    
    def str(self):
        return f"{self.client} - {self.room} ({self.arrival_date} - {self.departure_date})"

# Payments
class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Payment for {self.reservation} - {self.amount}"
