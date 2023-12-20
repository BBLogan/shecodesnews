# News Setup Step 12: adding a new view

from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.StoryView.as_view(), name='story'),
]
