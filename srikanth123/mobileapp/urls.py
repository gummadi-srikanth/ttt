from django.conf.urls import url
from mobileapp import views

urlpatterns=[
    url(r'^ home/',views.home,name="home"),
    url(r'^$',views.index,name="index"),
    url(r'^start/',views.start,name="start"),
    url(r'^sri/',views.sri,name="sri"),
    url(r'^company/',views.company,name="company"),

]