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
                this_qa['answer_btn'] = 'answer' + str(i+1)
                this_qa['message_id'] = 'message' + str(i+1)
                this_qa['select_id'] = 'select' + str(i+1)
                this_qa['hint_count'] = 'hint' + str(i+1) + '_count'
                this_qa['delete_count'] = 'delete'+ str(i+1) +'_count'
                this_qa['dropdown'] = 'dropdown' + str(i+1)
                allQA.append(this_qa)

            content['All_QA'] =  allQA
            content['hint_ary'] = json.dumps(list_hint)
            content['delete_ary'] = json.dumps(list_remove)
            content['page_title'] = name + '遊玩中'
            return render(request,"play.html",content)
        else:
            return redirect('/')
    except Exception as e:
        print(str(e))
        return redirect('/')


def result(request):
    content = {}
    if request.method == 'POST':
        RealAnswer,hint,delete,ExamAnswer = [],[],[],[]
        player_name = request.POST['player']
        for i in range(1,11):
            hint.append(request.POST['hint'+str(i)])
            delete.append(request.POST['delete'+str(i)])
            RealAnswer.append(request.POST['answer'+str(i)])
            ExamAnswer.append(request.POST['dropdown'+str(i)])
        print(player_name)
        print('hint',hint)
        print('delete',delete)
        print('RealAnswer',RealAnswer)
        print('ExamAnswer',ExamAnswer)
        delete_no = 0
        hint_no = 0
        correct = 0
        score  = 0
        for i in range(10):
            if hint[i] == '1':
                hint_no += 1
                score -= 5
            if delete[i] == '1':
                delete_no += 1
                score -= 5
            if ExamAnswer[i] == RealAnswer[i]:
                correct += 1
                if i == 9:
                    score += 20
                else:
                    score += 10
            if score < 0:
                score = 0
        p = player.objects.create(name=player_name,no_Q=correct,score=score,no_remove=delete_no,no_hint=hint_no)
        p.save()
        AllPlayer = player.objects.all().order_by('score')[::-1]
        rank_list = []
        for per_player in range(0,len(AllPlayer)):
            this_rank = {}
            if per_player == 0:
                content['first'] = AllPlayer[per_player].name
                content['score_st'] = AllPlayer[per_player].score
            this_rank['this_name'] = AllPlayer[per_player].name
            this_rank['this_score'] = AllPlayer[per_player].score
            this_rank['this_correct'] = AllPlayer[per_player].no_Q
            this_rank['this_hint_no'] = AllPlayer[per_player].no_hint
            this_rank['this_delete_no'] = AllPlayer[per_player].no_remove
            this_rank['score_width'] ='width:' + str(int(AllPlayer[per_player].score)/110*100) + '%'
            this_rank['correct_width'] = 'width:' + str(int(AllPlayer[per_player].no_Q)/10*100) + '%'
            this_rank['hint_width'] = 'width:' + str(int(AllPlayer[per_player].no_hint)/10*100) + '%'
            this_rank['delete_width'] = 'width:' + str(int(AllPlayer[per_player].no_remove)/10*100) + '%'
            rank_list.append(this_rank)
        content['rank_list'] = rank_list
        # content['name'] = player_name
        # content['score'] = score
        # content['hint_no'] = hint_no
        # content['delete_no'] = no_hint
        # content['correct'] = correct
        content['page_title'] = '結果'
        return render(request,"result.html",content)
    else:
        return redirect('/')