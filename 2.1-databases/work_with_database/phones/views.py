from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort', 1)

    if sorting == 'name':
        phone_projects = Phone.objects.all().order_by('name').values()
    elif sorting == 'min_price':
        phone_projects = Phone.objects.all().order_by('price').values()
    elif sorting == 'max_price':
        phone_projects = Phone.objects.all().order_by('-price').values()
    else:
        phone_projects = Phone.objects.all()

    context = {'phones': phone_projects}
    return render(request, template, context)



def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {'phone': phone_object}
    print(phone_object)
    return render(request, template, context)
