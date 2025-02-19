"""
URL configuration for movierecommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# accounts/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('register/', views.register_user, name='register_user'),
    path('signin/', views.signin_user, name='signin_user'), # This could be a POST for API calls or a GET for viewing ratings
    path('rate_movie/', views.rate_movie, name='rate_movie_by_id'),
    path('submit-rating/',views.submit_rating, name='submit_rating'),
    path('get_rate/', views.get_rating, name='get_rating'),
    path('logout/', views.logout_user, name='logout_user'),
]


