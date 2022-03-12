from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from user.forms import LoginForm, UpdateForm
from user.models import User


def detail(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'detail.html', {'user': user})
    else:
        return redirect('/user/login/')


def create(request):
    if request.method == 'GET':
        # method가 GET이면 유저 생성 페이지를 보여준다
        return render(request, 'create.html')
    elif request.method == 'POST':
        # method가 POST이면 유저를 생성한다
        user_name = request.POST.get("user_name", None)
        user_email = request.POST.get("user_email", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)

        res_data = {}
        if not (user_name and user_email and password and re_password):
            res_data['error'] = '모든 값을 입력해주세요'
        elif password != re_password:
            res_data['error'] = '패스워드를 확인해주세요'
        else:
            user = User(
                user_name=user_name,
                user_email=user_email,
                password=make_password(password)
            )
            user.save()

        if res_data.get('error'):
            # POST로 전달받은 값 중 user_name, user_email을 전달한다. 보안상 password 정보는 제외
            res_data['preset'] = {'user_name': user_name, 'user_email': user_email}
            # res_data['preset'] = request.POST
            # POST로 전달받은 전체 값을 전송하려면
            return render(request, 'create.html', res_data)
        else:
            # 성공하더라도 아직 다른 페이지가 없는 관계로 create 페이지로 돌아간다.
            # admin 페이지에서 user가 생성되었는지 확인한다.
            return render(request, 'create.html', res_data)


def update(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/user/login/")
    else:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect("/user/logout/")

    if request.method == 'GET':
        form = UpdateForm(initial={
            'user_name': user.user_name,
            'user_email': user.user_email,
            'password': '',
            're_password': ''
        })
        return render(request, 'update.html', {'form': form})
    elif request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.user_name = form.cleaned_data.get('user_name')
            user.user_email = form.cleaned_data.get('user_email')
            user.password = form.cleaned_data.get('password')
            user.save()
            return redirect("/user/detail/")
        else:
            return render(request, 'update.html', {'form': form})


def login(request):
    if request.method == 'GET':
        form = LoginForm  # form을 가져온다
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)  # form에 POST 데이터를 전송하여 clean으로 무결성 검사
        if form.is_valid():  # 무결성 검사를 통과하면
            request.session['user_id'] = form.user_id  # user_id를 세션에 등록
            return redirect('/user/detail/')
        else:  # 에러 발생시 폼 다시 전달. filed.errors로 에러 메세지 출력
            return render(request, 'login.html', {'form': form})


def logout(request):
    if request.session.get('user_id'):
        del request.session['user_id']
    return redirect("/user/login")
