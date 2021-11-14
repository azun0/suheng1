from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'templates/accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'templates/accounts/logout.html'), name='logout'),
]