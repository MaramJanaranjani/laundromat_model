from django.conf.urls import url
from samapp import views
urlpatterns = [url(r'^$', views.index, name = 'home'),]
