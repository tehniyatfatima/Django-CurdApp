

from django.contrib import admin
from django.urls import path
from django.urls import path, include
from curd import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('curd.urls'))
]
