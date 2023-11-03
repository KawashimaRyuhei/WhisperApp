from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "audiofileconversion/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by("pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "audiofileconversion/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "audiofileconversion/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "audiofileconversion/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("audiofileconversion:results", args=(question.id,)))
    
def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

