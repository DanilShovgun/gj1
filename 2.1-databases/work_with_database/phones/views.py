from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from your_app.models import Phone
from django.views.generic.list import ListView, MultipleObjectMixin, OrderingMixin

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

class PhoneListView(OrderingMixin, ListView):
    model = Phone
    template_name = 'phone_list.html'
    context_object_name = 'phones'
    ordering = ['-name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phone_detail.html'
    context_object_name = 'phone'
