from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api_data/', views.ShopList.as_view()),
    path('api_data/<int:pk>/', views.ShopDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
