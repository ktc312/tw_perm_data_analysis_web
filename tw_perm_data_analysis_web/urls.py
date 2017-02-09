from django.conf.urls import url
from django.contrib import admin
from tw_perm_data_analysis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
