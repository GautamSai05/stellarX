from django.shortcuts import render

def gravity_simulation_view(request):
    return render(request, 'gravity_simulation/gravity_simulation.html')