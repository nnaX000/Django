from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import SignUpForm, LoginForm

#회원가입 기능
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#로그인 기능
def login_view(request):
    form = LoginForm()  

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']

            #기존 authenticate의 경우 username과 pwd를 바탕으로 유효한 유저인지 검증을 하나, 이 함수를 커스터마이즈하여
            #id와 pwd를 기준으로 유효한 유저인지 검증을 하고 싶어서 다음과 같이 바꿔줌.
            #이 코드에서 사용자가 제출한 id와 pwd가 실제 db에 있는 유저인지 검증
            user = authenticate(request, username=id, password=password)

            if user is not None:
                #user 변수에 재대로 유저변수가 들어옴 = 로그인 진행시켜!(회원가입을 했던 유저이므로)
                login(request, user)
                #로그인 후에는 홈화면으로 리다이렉트
                return redirect('home')
            else:
                #db에 해당하는 유저가 없으면 해당하는 유저가 없다고 팝업을 띄운다.
                messages.error(request, '해당하는 유저가 없습니다!')

    return render(request, 'login.html', {'form': form})




