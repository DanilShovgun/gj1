from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from your_app.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

class PhoneListView(ListView):
    model = Phone
    template_name = 'phone_list.html'
    context_object_name = 'phones'

class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phone_detail.html'
    context_object_name = 'phone'
