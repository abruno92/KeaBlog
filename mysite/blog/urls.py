from django.conf.urls import url

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]


