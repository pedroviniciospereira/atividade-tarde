from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"page_app/partial/home.html")
def services (request):
    return render(request, "page_app/partial/services.html")
def contato (request):
    return render(request, "page_app/partial/contato.html")