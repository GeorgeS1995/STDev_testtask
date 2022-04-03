import uuid

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from millionaire_game.models import Question, GameSession, Answer
from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


class WelcomeView(TemplateView):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        session_id = uuid.uuid4()
        GameSession.objects.create(session=session_id)
        return HttpResponseRedirect(reverse('question', args=(session_id,)))


class QuestionsView(generic.DetailView):
    template_name = "question.html"
    QUESTION_COUNT = 5
    model = GameSession
    slug_field = 'session'
    slug_url_kwarg = 'session'

    def _get_used_questions_ids(self) -> list:
        return [o.question.id for o in self.object.answers.all()]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        used_questions_ids = self._get_used_questions_ids()
        context['question'] = Question.objects.exclude(id__in=used_questions_ids).order_by('?').first()
        context['session'] = str(self.object.session)
        return context

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.answers.add(Answer.objects.get(id=request.POST['answer']))
        answers_count = obj.answers.all().count()
        if answers_count == 5:
            redirect = HttpResponseRedirect(reverse('result', args=(kwargs['session'],)))
        else:
            redirect = HttpResponseRedirect(reverse('question', args=(kwargs['session'],)))
        return redirect


class ResultView(generic.DetailView):
    template_name = "result.html"
    model = GameSession
    slug_field = 'session'
    slug_url_kwarg = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score'] = sum(a.question.complexity for a in self.object.answers.filter(is_correct=True))
        context['questions'] = {a.question.id: {"text": a.question.text,
                                                "client_answer": a.text} for a in
                                self.object.answers.filter(is_correct=False)}
        context['correct_answers'] = {a.question.id: a.text for a in
                                      Answer.objects.filter(is_correct=True,
                                                            question_id__in=context['questions'].keys())}
        return context
