from django.urls import path

from .views import index,getAllUsers,createUser,updateUser,deleteUser 

urlpatterns = [
  path('',index,name='index'),
  path('users/',getAllUsers,name='users'),
  path('createuser/',createUser,name='createuser'),
  path('users/updateuser/<int:user_id>',updateUser,name='updateuser'),
  path('deleteuser/<int:user_id>',deleteUser,name='deleteuser'),
]