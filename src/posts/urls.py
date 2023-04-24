from django.urls import path, include
from .views import post_comment_create_and_list_view, like_unlike_post, PostDeleteView, PostUpdateView
from profiles.views import ProfileDetailView

app_name = 'posts'

urlpatterns = [
    path('', post_comment_create_and_list_view, name='main-post-view'),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),

]