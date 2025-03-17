
from django.urls import path
from. import views
urlpatterns = [
    path('', views.index,name="sTechhome"),
    path('gadgets/', views.gadgets,name="gadgets"),
    path('software/', views.software,name="software"),
    path('gaming/', views.gaming,name="gaming"),
    path('about/', views.about,name="about"),
    path('products/<int:myid>',views.prodview,name="prodview"),
    path('softwares/<int:myid>',views.softview,name="softview"),
    path('games/<int:myid>',views.gameview,name="gameview"),
    path('contact/', views.contact,name="contact"),
    path("loginSignup/", views.AccountPage, name="AccountPage"),
    path('signup', views.handleSignup,name="handleSignup"),
    path('login', views.handleLogin,name="handleLogin"),
    path('logout', views.handleLogout,name="handleLogout"),
    # APi to pose a comment
]