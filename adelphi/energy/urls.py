from django.urls import path, re_path
from energy import views

urlpatterns = [
    path('api/', views.StateList.as_view()),
    path('api/pv_yield', views.StateList.as_view()),
]
