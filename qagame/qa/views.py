from django.shortcuts import render,redirect

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
            # 開始出題
            
            return render(request,"play.html",content)
    except:
        return redirect('/')
        