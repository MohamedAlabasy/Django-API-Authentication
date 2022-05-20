from django.urls import path
from .views import Login, Registration, UserView, Logout
urlpatterns = [
    #=======================================================================================#
    #			                            project                                     	#
    #=======================================================================================#
    path('login', Login.as_view()),
    path('register', Registration.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
]
