from django import forms
from django.contrib.auth.hashers import check_password
from django.forms.utils import ErrorList

from user.models import User


class LoginForm(forms.ModelForm):
    user_email = forms.EmailField(
        max_length=256,
        label="이메일",
        error_messages={"required": "이메일을 입력해주세요"}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=16,
        label="비밀번호",
        error_messages={"required": "비밀번호를 입력해주세요"}
    )

    class Meta:
        model = User
        fields = ['user_email', 'password']

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        self.user_id = None

    def clean(self):
        clean_data = super().clean()
        user_email = clean_data.get('user_email')
        password = clean_data.get('password')

        if user_email and password:
            try:
                user = User.objects.get(user_email=user_email)
            except User.DoesNotExist:
                self.add_error('user_email', '존재하지 않는 이용자입니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 확인해주세요')
            else:
                self.user_id = user.id


class UpdateForm(forms.ModelForm):
    user_name = forms.CharField(
        max_length=64,
        label="사용자 명",
        error_messages={"required": "사용자 명을 입력해주세요"}
    )
    user_email = forms.EmailField(
        max_length=256,
        label="이메일",
        error_messages={"required": "이메일을 입력해주세요"}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=16,
        label="비밀번호",
        error_messages={"required": "비밀번호를 입력해주세요"}
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=16,
        label="비밀번호 확인",
        error_messages={"required": "비밀번호 확인을 입력해주세요"}
    )

    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'password']

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        re_password = clean_data.get('re_password')

        if password != re_password:
            self.add_error('password', '비밀번호를 확인해주세요')
            self.add_error('re_password', '비밀번호를 확인해주세요')
            return
