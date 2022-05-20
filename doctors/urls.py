from django.urls import path
from .views import Login, Registration
urlpatterns = [
    #=======================================================================================#
    #			                            project                                     	#
    #=======================================================================================#
    path('login', Login.as_view()),
    path('register', Registration.as_view()),
]
