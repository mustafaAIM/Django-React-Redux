from ecomapp import views
from django.urls import path
urlpatterns = [
  path('',views.getRoutes),
  path('products/',views.getProducts)
]