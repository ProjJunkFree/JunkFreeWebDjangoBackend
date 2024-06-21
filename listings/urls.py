from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myitems/', views.UserItemList.as_view(), name='my_items'),
    path('myitems/<int:pk>/', views.UserItemList.as_view(), name='user_item_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
