from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=64, verbose_name="사용자 명")
    user_email = models.EmailField(max_length=256, verbose_name="이메일")
    password = models.CharField(max_length=256, verbose_name="비밀 번호")
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    update_date = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "t_user"
        verbose_name = "사이트 이용자"
        verbose_name_plural = "사이트 이용자 목록"
