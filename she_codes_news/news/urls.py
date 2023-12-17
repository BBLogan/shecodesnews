# news/urls.py
from django.urls import path
# from . import views
from .views import IndexView, ExploreView, StoryView, AddStoryView, AddCommentView, EditStoryView, DeleteStoryView, DeleteStoryDoneView, AuthorStoryListView, AuthorDetailView
from django.contrib.auth.decorators import login_required
from django.http import request
# from .views import redirect_view

app_name = 'news'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('news/', include ('news.urls')), if want to use include need to add it to the from django.urls import path, inlucde

    path('explore-all-stories/', ExploreView.as_view(), name='allStories'),
    
    path('story/<int:pk>/', StoryView.as_view(), name='story'),

    path('add-story/', AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='addComment'),

    path('story/<int:pk>/edit/', EditStoryView.as_view(), name='editStory'),
    
    path('story/<int:pk>/delete/', DeleteStoryView.as_view(), name='deleteStory'),
    path('delete-story-done/', DeleteStoryDoneView.as_view(), name='deleteStory_done'),

    
    # demo - different ways to implement a list of author stories
    path('author_1/<str:username>', AuthorStoryListView.as_view(), name='authorstorylist'),
    
    path('author_2/<str:username>', AuthorDetailView.as_view(), name='authordetail'),
    
    # path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('/redirect/', views.AddComment.as_view(), name='redirect_view')
]
