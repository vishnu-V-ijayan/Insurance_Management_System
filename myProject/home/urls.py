from django.urls import path,include
from . import views

from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    path('', views.index,name="index"),
    path('signup/',views.Sign_up,name="signup"),
    path('handlelogin/',views.handlelogin,name="handlelogin"),
    path('handlelogout/',views.handlelogout,name="handlelogout"),
    path('customer_home/',views.customer_home,name="customer_home"),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
