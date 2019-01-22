"""fujtsuProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from requirementTwo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   
    url(r'^created/', views.get_name, name='get_name'),
    url(r'^new_record/', views.get_name, name='get_name'),
    url(r'^updated/', views.update_record, name='update_record'),
    
    
    
]
