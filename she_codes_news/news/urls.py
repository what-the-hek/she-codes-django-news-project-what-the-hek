from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit-story/', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name='addComment'),
    path('<int:pk>/delete-story/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('delete-success/', views.delete_success_view, name='deleteSuccess'),
    path('user/<int:pk>/', views.AuthorStories.as_view(), name='authorStories'),
]
