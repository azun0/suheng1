from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
<<<<<<< HEAD
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
=======
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
>>>>>>> e24fc0b17f683d9f1c9332a49cd0e5110def2307
]