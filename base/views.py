from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def first_page(request):
    return render(request, 'base/first_page.html')

def second_page(request):
    return render(request, 'base/second_page.html')
