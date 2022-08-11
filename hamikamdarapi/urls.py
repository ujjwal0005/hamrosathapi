"""hamikamdarapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from account import views as account
from Blog import views as blog

urlpatterns = [
    path('admin/', admin.site.urls),

    # userprofile
    path('register/',account.create_user,name="register"),
    path('user/update/',account.update_user,name="updateuser"),
    path('login/',account.obtain_auth_token, name='login'),
    path('logout/',account.logout, name='logout'),
    path('userprofile/',account.current_user,name='userprofile'),

    # doctorprofile
    path('doctorprofile/',account.doctor_profile,name='doctorprofile'),
    path('doctorprofile/update/',account.doctor_profileedit, name='updatedoctorprofile'),

    # blogs
    path('blog/',blog.create_blog,name='create_blog'),
    path('blog/<int:id>/',blog.update_blog,name='update_blog'),
    path('blogs/',blog.get_blogs,name='get_blog'),
    path('userblogs/',blog.get_userblog,name='user_blog'),

]
