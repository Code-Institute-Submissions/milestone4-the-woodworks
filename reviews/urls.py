from django.urls import path
from . import views


urlpatterns = [
    path('<product_id>/', views.view_reviews, name='view_reviews'),
    # path('add_vote/<poll_product_id>/', views.add_vote, name='add_vote'),
]