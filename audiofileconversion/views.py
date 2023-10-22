from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("audiofileconversion/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "audiofileconversion/index.html", context)

def detail(request, question_id):
    return render(request, "audiofileconversion/detail.html", "You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

## To Whisper
def speech_to_text(request):
    if request.method == "POST":
        audio_file = request.FILES['audio_file']
        transcriber = Transcriber()
        text = transcriber.transcribe(audio_file)

        return render(request, 'result.html', {'text': text})
    return render(request, 'upload.html')

# Create your views here.
