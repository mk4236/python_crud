from django import forms

from board.models import Board


class BoardCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=256,
        label="제목",
        error_messages={'required': '제목을 입력해주세요'}
    )
    contents = forms.CharField(
        widget=forms.Textarea,
        label="내용",
        error_messages={'required': '내용을 입력해주세요'}
    )

    class Meta:
        model = Board
        fields = ['title', 'contents']


class BoardUpdateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=256,
        label="제목",
        error_messages={'required': '제목을 입력해주세요'}
    )
    contents = forms.CharField(
        widget=forms.Textarea,
        label="내용",
        error_messages={'required': '내용을 입력해주세요'}
    )

    class Meta:
        model = Board
        fields = ['title', 'contents']
