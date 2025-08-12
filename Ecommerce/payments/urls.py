from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path("start-payment/", views.start_payment),
    path("payment-success/", views.payment_success),
    path("payment-cancel/", views.payment_cancel),
]
