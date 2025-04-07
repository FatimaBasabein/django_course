
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management_app.urls')),
]

handler404 ='management_app.views.custom_page_not_found'