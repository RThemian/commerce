from django.urls import path
from . import views
app_name = 'product'

# ModuleNotFoundError: No module named 'product.urls' when trying to run server
# https://stackoverflow.com/questions/64710069/modulenotfounderror-no-module-named-product-urls-when-trying-to-run-server
# 

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),

]
