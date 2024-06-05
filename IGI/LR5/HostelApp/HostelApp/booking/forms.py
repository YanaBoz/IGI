from django import forms
from booking.models import Reservation, Room

class BookingForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    promo_code = forms.CharField(required=False)

    class Meta:
        model = Room
        fields = ['arrival_date', 'departure_date', 'promo_code']

    def clean(self):
        cleaned_data = super().clean()
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")
        if arrival_date and departure_date and arrival_date >= departure_date:
            raise forms.ValidationError("Arrival date must be before departure date.")
        return cleaned_data
    
class ReservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['arrival_date', 'departure_date', 'notes']  # Only relevant fields

    # You can add custom validation or widgets if needed
    # For example, to ensure arrival date is before departure date:
    def clean(self):
        cleaned_data = super().clean()
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")
        if arrival_date and departure_date and arrival_date >= departure_date:
            raise forms.ValidationError("Arrival date must be before departure date.")
        return cleaned_data

class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'room_number', 'capacity', 'description', 'photo']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), 
        }