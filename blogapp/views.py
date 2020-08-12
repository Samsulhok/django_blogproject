from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name= "home.html"

class ContactView(TemplateView):
	template_name= "contact.html"

class IndexView(TemplateView):
	template_name= "index.html"

class AboutView(TemplateView):
	template_name= "about.html"

class NepalView(TemplateView):
	template_name= "nepal.html"

	
