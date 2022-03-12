from django.views.generic import FormView

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
