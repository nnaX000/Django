from django.shortcuts import render
from django.template import engines
from django.contrib.auth import logout


#홈화면 렌더링
def home_view(request):
    return render(request,'home.html')

#로그아웃 기능 구현
def logout_view(request):
    logout(request)
    return render(request,'home.html')
