from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
] 