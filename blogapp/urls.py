from django.urls import path
from .views import signupfunc, successfunc, PostListView, PostDetailView, AddPostView, UpdateView, DeleteView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('success/', successfunc, name='success'),
    path('list/', PostListView.as_view(), name='list'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('detail/edit/<int:pk>', UpdateView.as_view(), name='update'),
    path('detail/delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/add_comment/',
         AddCommentView.as_view(), name='add_comment'),
]
