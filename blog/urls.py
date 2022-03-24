from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('article/', views.Article.as_view()),
    path('article/<int:id>/', views.ArticleDetails.as_view()),
]
