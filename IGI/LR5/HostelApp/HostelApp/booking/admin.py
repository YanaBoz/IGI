from django.contrib import admin
from app.models import Profile
from booking.models import RoomCategory, Room, Client, Reservation, Payment, PromoCode

admin.site.register(Profile)
@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('category', 'room_number', 'capacity', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'notes', 'has_child')
    search_fields = ('first_name', 'last_name')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'room', 'arrival_date', 'departure_date', 'final_price', 'created_at')
    list_filter = ('arrival_date', 'departure_date')
    date_hierarchy = 'arrival_date'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'amount', 'payment_date')
    list_filter = ('payment_date',)

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount_type', 'discount_value')