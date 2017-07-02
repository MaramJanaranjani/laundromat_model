from django.conf.urls import url
from django.contrib import admin
from samapp import views
urlpatterns = [url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = "home"),
    url(r'^[A-Za-z]laundry_search$', views.laundry_search, name = "laund    ry_search"),
    url(r'^[A-Za-z]shop_view$', views.shop_view, name = "shop_view"),
    url(r'^[A-Za-z]count_clothes$', views.count_clothes, name = "count_clothes"),
    url(r'^[A-Za-z]fast_delivery$', views.fast_delivery,name = "fast_delivery"),    url(r'^[A-Za-z]total_cost$', views.total_cost,name = "total_cost"),
    url(r'^[A-Za-z]address$', views.address,name = "address"),
    url(r'^[A-Za-z]success_message$', views.success_message, name = "suc    cess_message"),
    url(r'^[A-Za-z]ratings$', views.ratings, name = "ratings"),
]
