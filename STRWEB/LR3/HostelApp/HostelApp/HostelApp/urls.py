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
    client_add,
    client_dashboard,
    RoomCategoryListView,
    RoomCategoryDetailView,
    RoomListViewcl,
    RoomDetailView,
    book_room,
    reservation_confirmation,
    promo_codes,
    RoomUpdateView,
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    client_add,
    client_delete,
    client_add_first,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('news/', views.news, name='news'),
    path('api/deteil_facts/', views.MedicalFactsView.as_view(), name='deteil_facts'),
    path('', views.home, name='home'),
    path('contact/', views.employees, name='contact'),
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
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/update/',ClientUpdateView.as_view(), name='client_update'),
    path('clients/add/', client_add, name='client_add'),
    path('clients/add_first/', client_add_first, name='client_add_first'),
    path('clients/<int:client_id>/delete/',client_delete, name='client_delete'),
    path('quest/', views.quest, name='quest'),
    path('quest/<int:quest_id>/', views.answer, name='answer'),
    path('politic/', views.politic, name='politic'),
    path('review/',views.rev_list, name='review'),
    path('shop/',views.shopview, name='shop'),
    path('shop/cart/',views.cart_view, name='cart'),
    path('shop/add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('shop/remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    #path('shop/update-cart-item/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
    path('shop/checkout/', views.checkout, name='checkout'),
    # path('review/create_review/',views.ReviewListCreate.as_view(), name='create_review'),
    path('review/create_review/',views.createRew, name='create_review'),
    path('news/<int:news_id>/', views.fullNews, name='fullNews'),
    path('anim',views.animm, name ='animate'),
    path ('JAS',views.js, name = 'JAS')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
