from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import ToDoViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='todo/index.html')),
    url(r'^todo/api/', ToDoViews.as_view()),
]
