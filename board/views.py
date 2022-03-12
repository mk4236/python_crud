from django.shortcuts import redirect
from django.views.generic import FormView, DetailView, ListView

from board.forms import BoardCreateForm
from board.models import Board
from user.models import User


class BoardCreateView(FormView):
    form_class = BoardCreateForm
    template_name = "board_create.html"
    success_url = "/board/create/"

    def form_valid(self, form):
        # user 정보 취득
        user_id = self.request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return redirect("/user/login/")
        else:
            return redirect("/user/logout/")

        board = Board(
            title=form.data.get('title'),
            contents=form.data.get('contents'),
            insert_user=user
        )
        board.save()
        return super().form_valid(form)


class BoardDetailView(DetailView):
    model = Board  # URLConf에서 pk 파라미터의 값을 활용하여 자동으로DB를 조회한다
    template_name = "board_detail.html"
    context_object_name = "board"


class BoardListView(ListView):
    model = Board
    template_name = "board_list.html"
    context_object_name = "board_list"
    ordering = "-id"
    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = "p"
