from django.urls import path
from .views import HomeView, SignupView, Blog, ReadBlog, index, DeleteBlogView, BlogLikeView, CommentCreateView, FAQView, FAQReplyView, SearchBlog, BlogUpdate
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('faq/', FAQView.as_view(), name="faq"),
    path('faq/<int:id>/reply/', FAQReplyView.as_view(), name="faq_reply"),
    path('blog/', Blog.as_view(), name='blog'),
    path('read_blog/<int:pk>/', ReadBlog.as_view(), name="read_blog"),
    path('delete_blog/<int:pk>/', DeleteBlogView.as_view(), name="delete_blog"),
    path('blog/<int:pk>/like/', BlogLikeView.as_view(), name='blog_like'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='add_comment'),
    path('update-blog/<int:pk>/', BlogUpdate.as_view()),
    # path('search/<str:title>/', SearchBlog.as_view(template_name='searched_blog.html'), name="searchBlog"),
    path('search/', SearchBlog.as_view(), name="search")
]