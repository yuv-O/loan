from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-payment/', views.add_payment, name='add_payment'),
    path('loan/<int:loan_id>/', views.loan_detail, name='loan_detail'),


]
