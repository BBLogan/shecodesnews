# news/urls.py
from django.urls import path

from . import views
from django.shortcuts import login_required
# from .views import redirect_view

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story', login_required(views.AddStoryView.as_view()), name='newStory'),
    path('<int:pk>/edit', login_required(views.EditStoryView.as_view()), name='editStory'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),
    # demo - different ways to implement a list of author stories
    path('author_1/<str:username>', views.AuthorStoryListView.as_view(), name='authorstorylist'),
    path('author_2/<str:username>', views.AuthorDetailView.as_view(), name='authordetail'),
    # path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('/redirect/', views.AddComment.as_view(), name='redirect_view')
]
