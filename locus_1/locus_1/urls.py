from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('humans.urls')),

    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
]
