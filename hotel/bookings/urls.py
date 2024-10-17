from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:room_id>/payment/', views.payment, name='payment'),
]