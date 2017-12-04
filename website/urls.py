from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^about.html',TemplateView.as_view(template_name="pages/about.html")),
    url(r'^services.html',TemplateView.as_view(template_name="pages/services.html")),
    url(r'^special-offers.html',TemplateView.as_view(template_name="pages/special-offers.html")),
    url(r'^new-patients.html',TemplateView.as_view(template_name="pages/new-patients.html")),

]