from django.urls import path
from energy import views

urlpatterns = [
    path('api/', views.state_list),
    path('api/<int:pk>/', views.state_detail),
]
