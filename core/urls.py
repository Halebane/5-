from django.urls import path
from django.contrib.auth import views as authViews

import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('books/', core.views.Books.as_view(), name='book_list'),
    path('books/<int:pk>/', core.views.BookDetail.as_view(), name='book_detail'),
    path('books/create/', core.views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', core.views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', core.views.BookDelete.as_view(), name='book_delete'),
    path('login/', core.views.LoginView.as_view(), name="login"),
    path('profile/', core.views.ProfilePage.as_view(), name="profile"),
    path('core/profile', core.views.RegisterView.as_view(), name="register"),
    path('exit/', authViews.LogoutView.as_view(next_page='core:login'), name='exit'),
]
