from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from django.urls import path
from main.models import Yogurt
from main.models import Fruit
from main.models import Waffle
from main.models import Doughnut
from main.models import Stock


urlpatterns = [
    url('comment', views.comment, name="comment"),
    url('about', views.about, name="about"),
    url('contact', views.contact, name="contact"),
    url('doughnut', ListView.as_view(queryset=Doughnut.objects.all(),template_name="main/Doughnut/index.html")),
    url('fruit', ListView.as_view(queryset=Fruit.objects.all(),template_name="main/Fruit/index.html")),
    url('waffle', ListView.as_view(queryset=Waffle.objects.all(),template_name="main/Waffle/index.html")),
    url('yogurt', ListView.as_view(queryset=Yogurt.objects.all(),template_name="main/Yogurt/index.html")),
    url('main', ListView.as_view(queryset=Stock.objects.all().order_by("-date_f"),template_name="main/Main/index.html")),
    url('product', views.product, name="product")
]
