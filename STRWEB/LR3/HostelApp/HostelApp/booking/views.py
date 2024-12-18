from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from booking.models import RoomCategory, Room, Reservation, PromoCode, Client
from booking.forms import ReservationUpdateForm, BookingForm, RoomUpdateForm, SelectClientForm  
from decimal import Decimal
from booking.forms import ClientForm, ClientFormFirst
from django.contrib.auth.decorators import login_required

# Client Views

class ClientListView( ListView):
    model = Client
    template_name = 'employee/client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'employee/client_detail.html'

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'employee/client_list.html'  

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'employee/client_detail.html'  

class RoomCategoryListView(ListView):
    model = RoomCategory
    template_name = 'client/room_categories.html'

class RoomCategoryDetailView(DetailView):
    model = RoomCategory
    template_name = 'client/room_category_detail.html'

class RoomListViewcl(ListView):
    model = Room
    template_name = 'client/clrooms.html'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'client/room_detail.html'

class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'employee/reservations.html' 

class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'employee/reservation_detail.html'

def promo_codes(request):
    promo_codes = PromoCode.objects.all()
    return render(request, 'client/promo_codes.html', {'promo_codes': promo_codes})

@login_required
def client_dashboard(request):
    reservations = Reservation.objects.filter(client=request.user.client) 
    return render(request, 'client/dashboard.html', {'reservations': reservations})

@login_required
def employee_dashboard(request):
    reservations = Reservation.objects.all().order_by('-created_at')[:10] 
    return render(request, 'employee/dashboard.html', {'reservations': reservations})

@login_required
def reservation_confirmation(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    return render(request, 'client/reservation_confirmation.html', {'reservation': reservation})

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'employee/client_update.html'
    form_class = ClientForm

    def form_valid(self, form):
        client = form.save()
        return redirect('client_detail', pk=client.pk) 
    
def client_update(request, client_id):
      client = Client.objects.get(pk=client_id)
      if request.method == 'POST':
          form = ClientForm(request.POST, instance=client)
          if form.is_valid():
              form.save()
              return redirect('client_list')
      else:
          form = ClientForm(instance=client)
      return render(request, 'employee/client_update.html', {'form': form, 'client': client})

@login_required
def client_add(request):
         if request.method == 'POST':
             form = ClientForm(request.POST)
             if form.is_valid():
                 form.save()
                 return redirect('client_list')
         else:
             form = ClientForm()
         return render(request, 'employee/client_add.html', {'form': form})

@login_required
def client_add_first(request):
         if request.method == 'POST':
             form = ClientFormFirst(request.POST)
             if form.is_valid():
                 review = form.save(commit=False) 
                 review.user = request.user 
                 review.save()  
             return HttpResponseRedirect(reverse('review'))  
         else:
             form = ClientFormFirst()
         return render(request, 'employee/client_add_first.html', {'form': form})

@login_required
def client_delete(request, client_id):
    """
    View function to handle deleting a Client instance.
    """
    client = Client.objects.get(pk=client_id)

    if request.method == 'POST':
        client.delete()
        return redirect('client_list')  # Replace 'client_list' with the URL name of your client list view.

    context = {'client': client}
    return render(request, 'employee/client_delete.html', context)
    

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
    client_form = SelectClientForm(request.POST or None)
    form = BookingForm(request.POST, instance=room)
    if request.method == 'POST':
        if form.is_valid() and client_form.is_valid():
            client = client_form.cleaned_data['client'] 
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
            # Redirect to the reservation success view
            return redirect('reservation_confirmation', pk=reservation.pk) 

    context = {
        'room': room,
        'form': form,
        'client_form': client_form,
    }
    return render(request, 'client/book_room.html', context)

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
