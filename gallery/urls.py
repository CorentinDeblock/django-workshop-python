from django.urls import path
from django.http import HttpResponse

from . import views

app_name="gallery"

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('post/', views.CreatePostView.as_view(), name='add_post'),
    path('post/like/<int:post_id>',views.like,name="like"),
    path('post/dislike/<int:post_id>',views.dislike,name="dislike")
]
