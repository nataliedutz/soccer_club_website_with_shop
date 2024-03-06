from django.shortcuts import render

def disclaimer_view(request):
    return render(request, 'disclaimer.html')

def impressum_view(request):
    return render(request, 'impressum.html')
