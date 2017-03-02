from django.conf.urls import url
from django.contrib import admin
from tw_perm_data_analysis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^Top_10_Companies_by_year/', views.top_com_yr, name='top_com_yr'),
    url(r'^Top_10_States_by_year/', views.top_state_yr, name='top_state_yr'),
    url(r'^By_area_and_year/', views.by_area_yr, name='by_area_yr'),
    url(r'^By_year_more/', views.by_yr_more, name='by_yr_more'),
    url(r'^By_state_more/', views.by_state_more, name='by_state_more'),
    url(r'^QA/', views.qa_page, name='qa_page'),
    url(r'^working/', views.working, name='working'),
]

