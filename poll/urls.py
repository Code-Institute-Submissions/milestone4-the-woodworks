from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_poll, name='view_poll'),
    path('add_vote/<poll_product_id>/', views.add_vote, name='add_vote'),
]
