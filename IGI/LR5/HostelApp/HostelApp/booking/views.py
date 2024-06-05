from pydoc import cli
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from booking.models import RoomCategory, Room, Reservation, PromoCode, Client
from booking.forms import ReservationUpdateForm, BookingForm, RoomUpdateForm  
from decimal import Decimal

# Client Views

@login_required
def client_dashboard(request):
    reservations = Reservation.objects.filter(client=request.user.client) 
    return render(request, 'client/dashboard.html', {'reservations': reservations})

# List all Room Categories
class RoomCategoryListView(ListView):
    model = RoomCategory
    template_name = 'client/room_categories.html'

# Detail View for a single room category
class RoomCategoryDetailView(DetailView):
    model = RoomCategory
    template_name = 'client/room_category_detail.html'

# List all Rooms
class RoomListViewcl(ListView):
    model = Room
    template_name = 'client/clrooms.html'

# Detail View for a single room
class RoomDetailView(DetailView):
    model = Room
    template_name = 'client/room_detail.html'
    

def apply_promo_code(promo_code, price):
    """Applies a promo code discount to the price."""
    if promo_code.discount_type == 'percentage':
        discount = price * (promo_code.discount_value / 100)
    elif promo_code.discount_type == 'fixed_amount':
        discount = promo_code.discount_value
    else:
        discount = 0  # Invalid discount type

    return Decimal(price - discount).quantize(Decimal('0.00'))

# View for booking a room
@login_required
def book_room(request, pk):
    room = Room.objects.get(pk=pk)
    client = Client.objects.get()  # This should be updated to get the correct client
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=room)
        if form.is_valid():
            arrival_date = form.cleaned_data['arrival_date']
            departure_date = form.cleaned_data['departure_date']
            promo_code_str = form.cleaned_data.get('promo_code')

            # Check room availability
            if not room.is_available(arrival_date, departure_date):
                form.add_error('room', "The selected room is not available for the chosen dates.")
                return render(request, 'client/book_room.html', {'form': form, 'room': room})

            # Calculate final price
            final_price = room.calculate_price(arrival_date, departure_date)
            promo_code = None
            if promo_code_str:
                try:
                    promo_code = PromoCode.objects.get(code=promo_code_str)
                    final_price = apply_promo_code(promo_code, final_price)
                except PromoCode.DoesNotExist:
                    form.add_error('promo_code', "Invalid promo code.")
                    return render(request, 'client/book_room.html', {'form': form, 'room': room})

            # Create the reservation
            reservation = Reservation.objects.create(
                client=client,
                room=room,
                arrival_date=arrival_date,
                departure_date=departure_date,
                final_price=final_price,
                promo_code=promo_code  # Now you can pass the promo_code
            )

            # Redirect to confirmation or payment processing
            return redirect('reservation_confirmation', pk=reservation.pk) 
    else:
        form = BookingForm(instance=room)
    return render(request, 'client/book_room.html', {'form': form, 'room': room})

# Confirmation page after booking
@login_required
def reservation_confirmation(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    return render(request, 'client/reservation_confirmation.html', {'reservation': reservation})

# View for listing available promo codes
def promo_codes(request):
    promo_codes = PromoCode.objects.all()
    return render(request, 'client/promo_codes.html', {'promo_codes': promo_codes})


# Employee Views

@login_required
def employee_dashboard(request):
    # You can customize this view to display relevant information for employees.
    # For example, show recent reservations, upcoming check-ins, etc.
    reservations = Reservation.objects.all().order_by('-created_at')[:10]  # Recent 10 reservations
    return render(request, 'employee/dashboard.html', {'reservations': reservations})

# List all Reservations
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'employee/reservations.html'  # Adjust template name

# Detail View for a single reservation
class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'employee/reservation_detail.html'  # Adjust template name

# Update Reservation details
class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'employee/reservation_update.html'
    form_class = ReservationUpdateForm

    def form_valid(self, form):
        reservation = form.save()
        return redirect('reservation_detail', pk=reservation.pk) 


def RoomUpdateView(request, pk):
       room = Room.objects.get(pk=pk)
       if request.method == "POST":
           form = RoomUpdateForm(request.POST, request.FILES, instance=room)
           if form.is_valid():
               form.save()
               return redirect('room_detail', pk=pk)  # Redirect to the updated room's detail view
       else:
           form = RoomUpdateForm(instance=room)
       return render(request, 'employee/room_details_empl.html',
 {'form': form})  # Assuming 'update_room.html' is your template                  
                     
# List all clients
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'employee/clients.html'  # Adjust template name

# Detail View for a single client
class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'employee/client_detail.html'  # Adjust template name

