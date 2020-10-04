from django.urls import path
from . import views


urlpatterns = [
    path('<product_id>/', views.view_reviews, name='view_reviews'),
    path('add_review/<product_id>/', views.add_review, name='add_review'),
]