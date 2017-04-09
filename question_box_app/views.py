from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AskQuestion
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'question_box_app/index.html')


def profile(request):
    return render(request, 'question_box_app/profile.html')


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.filter(question_id=question_id)
    return render(request, 'question_box_app/question.html', {'question': question, 'form': AnswerQuestion, 'answers': answers})


def ans_comment(request, question_id=1):
    return render(request, 'question_box_app/anscomment.html', {'form': CommentOnAns})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#
# def answer(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AnswerQuestion(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/api/answer/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AnswerQuestion()
#
#     return render(request, 'question_box_app/answer.html', {'form': form})
#

def ask(request):
    return render(request, 'question_box_app/ask.html', {'form': AskQuestion})

def q_upvote(request, user_id, answer_id):
    # make a new instance of the vote
    qv = QuestionVote(user=user_id, answer=answer_id, score=1)
    return redirect()



    return render(request, 'question_box_app/vote.html', context)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('created')
    serializer_class = QuestionSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('score')
    serializer_class = UserProfileSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('created')
    serializer_class = AnswerSerializer


class QuestionCommentViewSet(viewsets.ModelViewSet):
    queryset = QuestionComment.objects.all().order_by('created')
    serializer_class = QuestionCommentSerializer


class AnswerCommentViewSet(viewsets.ModelViewSet):
    queryset = AnswerComment.objects.all().order_by('created')
    serializer_class = AnswerCommentSerializer


class QuestionVoteViewSet(viewsets.ModelViewSet):
    queryset = QuestionVote.objects.all().order_by('score')
    serializer_class = QuestionVoteSerializer


class AnswerVoteViewSet(viewsets.ModelViewSet):
    queryset = AnswerVote.objects.all().order_by('score')
    serializer_class = AnswerVoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('text')
    serializer_class = TagSerializer
