#aboutme/urls.py
from django.conf.urls import url
from aboutme import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^projects/$', views.ProjectsPageView.as_view())
]
