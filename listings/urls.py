from django.urls import path
from . import views


urlpatterns = [
    path('myitems/', views.UserItemList.as_view(), name='my_items'),
    path('myitems/<int:pk>/', views.UserItemList.as_view(), name='user_item_detail')
]
