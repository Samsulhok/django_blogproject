from django.urls import path
from  .views import *


app_name ="blogapp"

urlpatterns=[
	path("", HomeView.as_view(), name="home"),
	path("contact/", ContactView.as_view(), name="contact"),
	path("index/", IndexView.as_view(), name="index"),
	path("about/", AboutView.as_view(), name="about"),
	path("nepal/", NepalView.as_view(), name="nepal"),




]

