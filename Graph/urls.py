from django.conf.urls import url, include
from . import views 

urlpatterns =(
    url(r'^csv_upload$', views.csv_upload),
)
