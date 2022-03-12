from django.views.generic import FormView, DetailView

from board.forms import BoardCreateForm
from board.models import Board


class BoardCreateView(FormView):
    template_name = "board_create.html"
    form_class = BoardCreateForm
    success_url = "/board/create"

    def form_valid(self, form):
        board = Board(
            title=form.data.get('title'),
            contents=form.data.get('contents')
        )
        board.save()
        return super().form_valid(form)


class BoardDetailView(DetailView):
    template_name = "board_detail.html"
    model = Board  # URLConf에서 pk 파라미터의 값을 활용하여 자동으로DB를 조회한다
