"""
Definition of views.
"""
from django import utils
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views import View
from django.views.generic import DetailView
from app.forms import BootstrapRegistrationForm, CheckoutForm, CreateReviewForm
from django.utils import timezone
import pytz
import requests
import matplotlib
from .models import *
from matplotlib import pyplot as plt
from booking.models import Reservation
from django.db.models import Sum
from tzlocal import get_localzone
from django.shortcuts import get_object_or_404

def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'app/vacant.html', {'vacancies': vacancies})

# def product_detail(request, product_id):
#     product = Service.objects.all( pk=product_id)
#     context = {'product': product}
#     return render(request, 'app/product_detail.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Service, pk=product_id)
    cart, created = Cart_2.objects.get_or_create(user=request.user)

    try:
        cart_item = CartItem_2.objects.get(cart=cart, product=product) 
        cart_item.quantity += 1
        cart_item.save()
    except CartItem_2.DoesNotExist:
        cart_item = CartItem_2.objects.create(cart = cart, product=product, quantity=1)

    messages.success(request, f"{product.name} Added!")
    return redirect('shop')


@login_required
def cart_view(request):
    cart = Cart_2.objects.get(user=request.user)
    cart_items = CartItem_2.objects.filter(cart=cart)
    total_price = sum(item.quantity * item.product.price for item in cart_items)

    for cart_item in cart_items:
        cart_item.item_price = cart_item.quantity * cart_item.product.price

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'app/cart.html', context)


@login_required
def checkout(request):
    cart = Cart_2.objects.get(user=request.user)
    cart_items = CartItem_2.objects.filter(cart=cart)
    total_price = sum(cart_item.quantity * cart_item.product.price for cart_item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, total_price=total_price)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
            cart.delete()  # Очистка корзины
            messages.success(request, 'Syccess!')
            return redirect('shop')  # Перенаправление на страницу подтверждения
    else:
        form = CheckoutForm()

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
    }
    return render(request, 'app/pay.html', context)


@login_required
def order_success(request):
    return render(request, 'app/shop.html')

def shopview(request):
     services = Service.objects.all()
     return render(request, 'app/shop.html', {'services': services}) 

# @login_required
# def cart_view(request):
#     cart, created = CartItem.objects.get_or_create()
#     return render(request, 'app/cart.html', {'cart': cart})

# @login_required
# def add_to_cart(request, product_id):
#     product = Service.objects.get(pk=product_id)
#     cart, created = Cart.objects.get_or_create() 
#     cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    product = Service.objects.get(pk=product_id)
    cart = Cart_2.objects.get() 
    cart_item = CartItem_2.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

# @login_required
# def update_cart_item(request, product_id):
#     product = Service.objects.get(pk=product_id)
#     cart = Cart.objects.get() 
#     cart_item = CartItem.objects.get(product=product, cart=cart)
#     quantity = request.POST.get('quantity')
#     if quantity:
#         cart_item.quantity = quantity
#         cart_item.save()
#     return redirect('cart')

# @login_required
# def checkout(request):
#     cart = Cart.objects.get() 
#     return render(request, 'app/pay.html', {'cart': cart})

# def contact(request):
#          contacts = Contact.objects.all()
#          return render(request, 'app/contact.html', {'contacts': contacts})

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'app/contact.html', {'employees': employees}) 

def animm(request):
    return render(request, 'app/animat.html')

def js(request):
    news = Full_News.objects.all()
    return render(request, 'app/JS.html', {'news': news})

def news(request):
    news = Full_News.objects.all()
    return render(request, 'app/new_news.html', {'news': news})

def fullNews(request, news_id):
    fullNews = Full_News.objects.filter(pk=news_id)
    return render(request, 'app/fullNews.html', {'fullNews': fullNews})

def quest(request):
    quests = Answer.objects.all()
    return render(request, 'app/quest.html', {'quests': quests}) 

def answer(request, quest_id):
    quests = Answer.objects.filter(pk=quest_id)
    return render(request, 'app/answer.html', {'quests': quests}) 

def politic(request):
    politics = PolCon.objects.all()
    return render(request, 'app/politic.html', {'politics': politics}) 

def rev_list(request):
    politics = Review2.objects.order_by('-date')
    return render(request, 'app/review.html', {'politics': politics}) 

class ReviewListView( ListView):
    model = Review2
    template_name = 'app/review.html'

class ReviewListCreate( CreateView ):
    model = Review
    form_class = CreateReviewForm
    template_name = 'app/create_review.html'

def createRew(request):
     if request.method == "POST" and request.user.is_authenticated:
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False) 
            review.user = request.user 
            review.date = datetime.now()
            review.save()  
            return HttpResponseRedirect(reverse('review'))  
     else:
         form = CreateReviewForm()
     return render(request, 'app/create_review.html', {'form': form})

#API

class MedicalFactsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            url = 'https://api.publicapis.org/entries'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                
                
                facts = []
                if 'results' in data and data['results']:
                    for result in data['results']:
                        fact = result.get('description', '')
                        if fact:
                            facts.append(fact)
                return render(request, 'app/news.html', {'facts': facts})
            else:
                return render(request, 'app/news.html', {'error': 'Failed to fetch data from API'})
        return HttpResponseNotFound("Page not found")
    
def current_time(request):
    user_timezone = get_localzone()
    
    current_date_utc = timezone.now()
    current_date_user_tz = current_date_utc.astimezone(user_timezone)
    context = {
         'current_date_utc': current_date_utc.strftime('%d/%m/%Y %H:%M:%S'),
            'current_date_user_tz': current_date_user_tz.strftime('%d/%m/%Y %H:%M:%S'),
            'user_timezone': user_timezone.key,
    }
    return render(request, 'app/layout.html', context)

def home(request):
    """Renders the home page."""
    user_timezone = get_localzone()

    current_date_utc = timezone.now()
    current_date_user_tz = current_date_utc.astimezone(user_timezone)
    latest_article = Full_News.objects.latest('news_id')

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'current_date_utc': current_date_utc.strftime('%d/%m/%Y %H:%M:%S'),
            'current_date_user_tz': current_date_user_tz.strftime('%d/%m/%Y %H:%M:%S'),
            'user_timezone': user_timezone.key,
            'latest_article': latest_article, 
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    abouts = About.objects.all()
    user_timezone = get_localzone()

    current_date_utc = timezone.now()
    current_date_user_tz = current_date_utc.astimezone(user_timezone)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'current_date_utc': current_date_utc.strftime('%d/%m/%Y %H:%M:%S'),
            'current_date_user_tz': current_date_user_tz.strftime('%d/%m/%Y %H:%M:%S'),
            'user_timezone': user_timezone.key,
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'abouts' : abouts,
        }
    )

def register(request):
    if request.method == 'POST':
        form = BootstrapRegistrationForm(request.POST)
        if form.is_valid():
              user = form.save()
              login(request, user)
              messages.success(request, "Registration successful!")
        return redirect('client_add_first')  # Replace 'home' with the desired redirect URL
    else:
        form = BootstrapRegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def yearly_sales_report(year):
    orders = Reservation.objects.filter(date__year=year, is_canceled=False)
    total_sales_for_year = orders.aggregate(total_sales=Sum('price_prom'))['total_sales'] or 0
    return total_sales_for_year

def yearly_sales_trend():
    current_year = datetime.now().year
    last_three_years = range(current_year - 2, current_year + 1)
    yearly_sales_ = []

    for year in last_three_years:
        sales = yearly_sales_report(year)
        yearly_sales_.append(round(sales, 2))

    return list(last_three_years), yearly_sales_

def linear_sales_trend():

    matplotlib.use('Agg')

    years, sales = yearly_sales_trend()

    plt.figure(figsize=(14, 6))

    plt.plot(years, sales, color='yellowgreen', marker='o', linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('More, rub')
    plt.title('Per Year')
    plt.xticks(years)
    plt.grid(True)


    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    yearly_sales_data = list(zip(years, sales))

    return url, yearly_sales_data


def year_sales_volume():
    matplotlib.use('Agg')

    years, sales = yearly_sales_trend()

    image_urls = []

    colors = ['yellowgreen', 'yellowgreen', 'yellowgreen']

    plt.figure(figsize=(10, 10))

    plt.bar(years, sales, color=colors)
    plt.xlabel('Year')
    plt.ylabel('Sel, rub')
    plt.xticks(years)
    plt.title(f'Per year - {years}')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    image_urls.append(url)

    return image_urls