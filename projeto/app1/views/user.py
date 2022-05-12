from re import U
from django.shortcuts import render,redirect
from ..models import User
from ..forms import UserModelForm

# Create your views here.

def getAllUsers(request):
  users = User.objects.all()

  context = {
    'users': users,
    'form': UserModelForm
  }

  return render(request,'user/users.html',context=context)

def createUser(request):
    print("criar")
    # Salvar form
    form = UserModelForm(request.POST)
    if form.is_valid():
    # True -> é valido
      form.save()


    return redirect('users')


def updateUser(request, user_id):

    print(user_id)
    user = User.objects.get(pk=user_id)
    print(user)
    # salvar form
    form = UserModelForm(data=request.POST, instance=user)
    if form.is_valid():
        form.save()
        

    return redirect('users')

def deleteUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('users')