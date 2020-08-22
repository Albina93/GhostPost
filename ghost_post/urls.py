from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_post/', views.createpost_view, name="addpost"),
    path('roast/', views.roast_view, name="roast"),
    path('boast/', views.boast_view, name="roast"),
    path('sorted_by/', views.sorted_view, name="sortedby"),
    path('upvote/<int:upvote_id>', views.upvote_view, name="upvote_page"),
    path('downvote/<int:downvote_id>', views.downvote_view, name="downvote_page"),
    path('detail/<str:sec_key>', views.detail_view, name="detail_page"),
    path('deletepost/<int:post_id>', views.delete_view, name="delete_page"),
]
