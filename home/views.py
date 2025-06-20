from django.shortcuts import render

# Create your views here.
def splash(request):
    return render(request,'home/splash.html')

def home_view(request):
    return render(request,'home/home.html')
