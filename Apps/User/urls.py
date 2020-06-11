"""
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
from Apps.User import views as views_user

urlpatterns = [
    path('', views_user.home, name='home'),
    path('login', views_user.loginn, name='login'),
    path('register', views_user.register, name='register'),
    path('cerrarSesion', views_user.cerrarSesion, name='cerrarSesion'),
    
]
