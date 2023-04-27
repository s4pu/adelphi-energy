from django.urls import path
from energy import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.members),
    path('/', views.members),
    path('api/', views.StateList.as_view()),
    path('api/pv_yield', views.StateList.as_view()),
    path('api/pv_yield/', views.StateList.as_view()),
]
