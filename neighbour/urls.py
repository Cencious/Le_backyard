from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home, name='home'),
    path('register/',views.register,name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('user/', views.profile, name='profile'),
    path('search/', views.search_hood, name='search_hoods'),
    
    path('neighbourhood/',views.neighborhood,name='neighbourhood'),
    path('joinhood/<neighborhood_id>',views.join_hood,name="joinhood"),
    path('leavehood/<neighborhood_id>',views.leave_hood,name="leavehood")

]
