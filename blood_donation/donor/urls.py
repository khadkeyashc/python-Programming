from django.urls import path
from .views import donate_blood, thank_you

urlpatterns = [
    path('', donate_blood, name='donate_blood'),
    path('thank-you/', thank_you, name='thank_you'),
]
