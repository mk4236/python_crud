from django.shortcuts import redirect
from django.views.generic import FormView, DetailView, ListView, UpdateView

from board.forms import BoardCreateForm, BoardUpdateForm
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
            title=form.cleaned_data.get('title'),
            contents=form.cleaned_data.get('contents'),
            insert_user=user
        )
        board.save()
        return super().form_valid(form)


class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardUpdateForm

    template_name = "board_update.html"

    def form_valid(self, form):
        user_id = self.request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return redirect("/user/login/")
        else:
            return redirect("/user/logout/")

        board = Board.objects.get(pk=self.kwargs.get("pk"))
        board.title = form.cleaned_data.get('title')
        board.contents = form.cleaned_data.get('contents')
        board.save()

        return super().form_valid(form)

    # pk를 이용하여 detail 페이지로 돌아갈 수 있게 success_url을 제어한다
    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return f'/board/detail/{pk}'


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BoardListView, self).get_context_data()
        # pagination
        page = context['page_obj']
        paginator = page.paginator
        page_list = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['page_list'] = page_list

        return context
