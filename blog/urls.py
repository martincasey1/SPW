from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, like_view, AddCommentView, gallery_image_view, success, display_gallery_images
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about'),
    path('like/<int:pk>', like_view, name='like-post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('image_upload', gallery_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
    path('gallery_list', display_gallery_images, name = 'gallery_list'),
    path("contact", views.contact, name="contact"),
]
