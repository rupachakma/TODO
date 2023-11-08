from django.urls import path

from task import views

urlpatterns = [
    path('', views.signuppage,name="signuppage"),
    path('loginpage', views.loginpage,name="loginpage"),
    path('logoutpage', views.logoutpage,name="logoutpage"),
    path('homepage', views.homepage,name="homepage"),
    path('addtask', views.addtask,name="addtask"),
    path('deletetask/<int:id>', views.deletetask,name="deletetask"),
    path('change_status/<int:id>/<str:status>', views.change_status,name="change_status"),
    path('myprofile', views.myprofile,name="myprofile"),
    path('updateprofile', views.updateprofile,name="updateprofile"),
]