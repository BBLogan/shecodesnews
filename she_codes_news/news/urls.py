# news/urls.py
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import IndexView, StoryView, AddStoryView, EditStoryView, DeleteStoryView, DeleteStoryDoneView, AuthorDetailView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('create-story/', views.AddStoryView.as_view(), name='createStory'),
    path('<int:pk>/edit-story/', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/delete-story/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('delete-story-done/', DeleteStoryDoneView.as_view(), name='deleteStory_done'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author')
    ]