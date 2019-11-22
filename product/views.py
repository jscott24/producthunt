from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'product/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] \
        and request.POST['image'] and request.POST['icon']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'http//' + request.POST['url']
            product.icon = request.POST['icon']
            product.image = request.POST['image']
            product.pub_date = timezone.datetime.now()
            product.votes_total = 1
            product.hunter = request.user
            product.save()
            return redirect('home')

        else:
            return render(request, 'product/create.html', {'error':'You must fill in all the required items'})
    else:
        return render(request, 'product/create.html')
