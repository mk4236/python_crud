from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from user.models import User


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
            # POST로 전달받은 전체 값을 전송하려면
            # res_data['preset'] = request.POST
            return render(request, 'create.html', res_data)
        else:
            # 성공하더라도 아직 다른 페이지가 없는 관계로 create 페이지로 돌아간다.
            # admin 페이지에서 user가 생성되었는지 확인한다.
            return render(request, 'create.html', res_data)
