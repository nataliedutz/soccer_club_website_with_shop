from django.urls import path
from .views import disclaimer_view, impressum_view

app_name = 'legal'

urlpatterns = [
    path('disclaimer/', disclaimer_view, name='disclaimer'),
    path('impressum/', impressum_view, name='impressum'), 
    ]
