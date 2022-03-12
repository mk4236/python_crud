from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=256, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    insert_user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    update_date = models.DateTimeField(auto_now=True, verbose_name="수정일", null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_board'
        verbose_name = "게시판"
        verbose_name_plural = "게시판 목록"
