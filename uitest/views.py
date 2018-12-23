from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from uitest import models


def login(request):
    # View code here...
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, '../templates/login.html')
            if user.password == password:
                return render(request,'../templates/index.html')
    return render(request, '../templates/login.html')