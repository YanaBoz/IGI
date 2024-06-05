"""
Definition of urls for Hostel.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.resolvers import settings
from app import forms, views
from booking.views import (
    ReservationListView, 
    ReservationDetailView,
    ReservationUpdateView,
    client_dashboard,
    RoomCategoryListView,
    RoomCategoryDetailView,
    RoomListViewcl,
    RoomDetailView,
    book_room,
    reservation_confirmation,
    promo_codes,
    RoomUpdateView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('register/', views.register, name='register'),     
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('reservations/', ReservationListView.as_view(), name='reservations'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('client/dashboard/', client_dashboard, name='client_dashboard'),
    path('rooms/categories/', RoomCategoryListView.as_view(), name='room_categories'),
    path('rooms/categories/<int:pk>/', RoomCategoryDetailView.as_view(), name='room_category_detail'),
    path('rooms/', RoomListViewcl.as_view(), name='rooms'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('rooms/<int:pk>/update/',RoomUpdateView, name='room_update'),
    path('rooms/<int:pk>/book/', book_room, name='book_room'),
    path('reservations/<int:pk>/confirmation/', reservation_confirmation, name='reservation_confirmation'),
    path('promo-codes/', promo_codes, name='promo_codes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
