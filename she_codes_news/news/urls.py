# news/urls.py
from django.contrib import admin
from django.urls import include, path
from .views import IndexView, ExploreView, StoryView, AddStoryView, AddCommentView, EditStoryView, DeleteStoryView, DeleteStoryDoneView, AuthorStoryListView, AuthorDetailView
from django.contrib.auth.decorators import login_required

app_name = 'news'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('', IndexView.as_view(), name='index'),
    path('explore-all-stories/', ExploreView.as_view(), name='allStories'),
    path('story/<int:pk>/', StoryView.as_view(), name='story'),
    path('add-story/', login_required(AddStoryView.as_view()), name='newStory'),
    path('<int:pk>/comment/', login_required(AddCommentView.as_view()), name='addComment'),
    path('story/<int:pk>/edit/', EditStoryView.as_view(), name='editStory'),
    path('story/<int:pk>/delete/', login_required(DeleteStoryView.as_view()), name='deleteStory'),
    path('delete-story-done/', login_required(DeleteStoryDoneView.as_view()), name='deleteStory_done'),
    
    # demo - different ways to implement a list of author stories
    path('author_1/<str:username>', AuthorStoryListView.as_view(), name='authorstorylist'),
    path('author_2/<str:username>', AuthorDetailView.as_view(), name='authordetail'),
    ]

# if in future i need to add other views:
    # path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('/redirect/', views.AddComment.as_view(), name='redirect_view')