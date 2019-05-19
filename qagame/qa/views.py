from django.shortcuts import render,redirect
from qa.models import player,question
import random
import json
# Create your views here.

def index(request):
    content = {}
    content['page_title'] = '歡迎!!'
    return render(request,"start.html",content)

def play_game(request):
    content = {}
    try:
        if request.method == 'POST':
            
            name = request.POST['name']
            sub1 = request.POST['sub1']
            sub2 = request.POST['sub2']
            if sub1 ==sub2:
                return redirect('/')
            print(name+sub1+sub2)
            subject_list = ['國文','英文','數學','地理','自然','歷史']
            no_exam_sub = random.choice(subject_list)
            while no_exam_sub == sub1 or no_exam_sub == sub2:
                no_exam_sub = random.choice(subject_list)
            print(no_exam_sub)
            user = player(name=name)
            # user.save()
            content['play_name'] = name
            # 開始出題
            test_qa = question.objects.exclude(subject=no_exam_sub)
            # 題庫 test_qa
            allQA = []

            list_hint = [None]*10
            list_remove = [None]*10
            for i in range(0,10):
                this_qa = {}
                this_qa['no'] = str(i+1)
                this_qa['subject'] = test_qa[i].subject
                this_qa['topic'] = test_qa[i].topic
                this_qa['optionA'] = test_qa[i].optionA
                this_qa['optionB'] = test_qa[i].optionB
                this_qa['optionC'] = test_qa[i].optionC
                this_qa['optionD'] = test_qa[i].optionD
                this_qa['answer'] = test_qa[i].Answer
                this_qa['hint'] = test_qa[i].hint
                list_hint[i] = test_qa[i].hint
                this_qa['remove'] = test_qa[i].remove
                list_remove[i] = test_qa[i].remove
                this_qa['hint_btn'] = 'hint' + str(i+1)
                this_qa['delete_btn'] = 'delete' + str(i+1)
                this_qa['message_id'] = 'message' + str(i+1)
                this_qa['hint_count'] = 'hint' + str(i+1) + '_count'
                this_qa['delete_count'] = 'delete'+ str(i+1) +'_count'
                allQA.append(this_qa)

            content['All_QA'] =  allQA
            content['hint_ary'] = json.dumps(list_hint)
            content['delete_ary'] = json.dumps(list_remove)
            return render(request,"play.html",content)
    except Exception as e:
        print(str(e))
        return redirect('/')


def result(request):
    if request.method == 'POST':
        hint1 = request.POST['hint1']
        delete1 = request.POST['delete1']
        print(hint1+' ' +delete1)
    return redirect('/')