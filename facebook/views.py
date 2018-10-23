
from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment


# Create your views here.
def play(request) :
    return render(request, 'play.html')

count = 0
def play2(request) :
    abc ='xanha'
    age = 19
    
    global count
    count = count+1
    
    if age >= 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘 날씨가 좋았다 - 10월2일', '오늘은 추웠다 - 10월3일', '배고프다 - 9월1일', '마지막글 테스트']

    return render(request, 'play2.html', {'name': abc, 'count': count, 'age' : status, 'diary' : diary })

def profile(request) :
    return render(request, 'xanha/profile.html')

def event(request) :
    abc = 'xanha'
    age = 19

    global count
    count = count + 1

    if age >= 19:
        status = '성인'
    else:
        status = '청소년'

    if count == 7:
        result = '당첨'
    else:
        result = '꽝'

    return render(request, 'event.html', {'name': abc, 'count': count, 'age': status, 'event': result})


def newsfeed(request):
    #모든 뉴스피드 글을 불러오는 작업
    #데이터베이스에서 꺼내오는 것(모델링)
    articles= Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request, pk):
    # pk번 글을 불러오기
    article= Article.objects.get(pk=pk)  # pk= primary key

    # 코멘트를 저장하라
    if request.method == 'POST' :
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{ pk }')
        # alter
    # return redirect(f'/feed/{ pk }')


    return render(request, 'detail_feed.html', {'feed': article})



def new_feed(request):
    if request.method == 'POST' : #폼이 전송되었을 때만 아래 코드를 실행
        new_article = Article.objects.creat(
            author = request.POST['author'],
            title =  request.POST['title'],
            text = request.POST['content'],
            password = request.POST['password'],
        )

        # 새 글 등록 끝

    return render(request, 'new_feed.html')

def remove_feed(request, pk) :
    article = Article.objects.get(pk=pk)
    return render(request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk) :
    article = Article.objects.get(pk=pk)
    return render(request, 'edit_feed.html', {'feed' : article})


