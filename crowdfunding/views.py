from django.shortcuts import render

def crowdfunding_view(request):
    return render(request, 'crowdfunding/crowdfunding.html')