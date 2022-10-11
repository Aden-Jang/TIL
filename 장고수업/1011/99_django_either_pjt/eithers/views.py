from django.db.models import Q, Count
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:detail', question.pk)
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    # 1. annotate를 사용하지 않는 방법
    # question = Question.objects.get(pk=question_pk)

    # count_a = len(question.comment_set.filter(pick=0))
    # count_b = len(question.comment_set.filter(pick=1))
    # total_count = count_a + count_b

    if total_count == 0:
        a_per = 0
        b_per = 0
    else:
        a_per = round(count_a / total_count * 100, 2)
        b_per = round(count_b / total_count * 100, 2)

    ###################################################

    # 2. annotate를 사용한 방법
    
    # Filtering on annotations
    count_a = Count('comment', filter=Q(comment__pick=0))
    # count_a=Count('comment', filter=Q(comment__pick=False))
    count_b = Count('comment', filter=Q(comment__pick=1))
    total_count = Count('comment')
    
    question = Question.objects.annotate(
                                    total_count=total_count,
                                    count_a=count_a,
                                    count_b=count_b
                                ).get(pk=question_pk)

    a_per = round(question.count_a / question.total_count * 100, 2) if question.total_count else 0
    b_per = round(question.count_b / question.total_count * 100, 2) if question.total_count else 0
    
    # 1 & 2 공통 사항
    comment_form = CommentForm()    
    comments = question.comment_set.order_by('-pk')

    context = {
        'question': question,
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per,
        'b_per': b_per,
    }
    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)


def random(request):
    # 1. random 모듈을 사용하는 방법
    import random

    pk_list = []
    for value in Question.objects.values('pk'):
        pk_list.append(value['pk'])
    question = Question.objects.get(pk=random.choice(pk_list))

    # 2. random 모듈을 사용하지 않는 방법
    # question = Question.objects.order_by('?')[:1]

    count_a = len(question.comment_set.filter(pick=0))
    count_b = len(question.comment_set.filter(pick=1))
    total_count = count_a + count_b

    comment_form = CommentForm()
    comments = question.comment_set.order_by('-pk')

    if total_count == 0:
        a_per = 0
        b_per = 0
    else:
        a_per = round(count_a / total_count * 100, 2)
        b_per = round(count_b / total_count * 100, 2)
    
    context = {
        'question': question, 
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per, 
        'b_per': b_per,
    }

    return render(request, 'eithers/detail.html', context)
