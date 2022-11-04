from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe

from .forms import MovieCreationForm
from .models import Movie

from heapq import heappop, heappush
# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.all()
    context={
        'movies': movies
    }
    return render(request, "movies/index.html", context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie_genres = movie.genres.all()
    ret = []
    for i in movie_genres:
        ret.append(i.name)
    context = {
        'movie': movie,
        'genres': ret,
    }
    return render(request, 'movies/detail.html', context)

'''
user의 쓴 리뷰가 있다면 : genre를 pk 뺄거야.
    genre 순회하면서 pk를 기준으로 딕트 형태로 우선순위를 매길 거야.
    dict로 해석해서 점수를 매기고 리뷰갯수로 나눠서 평균 장르 점수.
없다면 : vote_average 순으로 상위 10개.
'''
@require_safe
def recommended(request):
    me = request.user # 유저 = 나
    mymovies = list(me.myreviews.all()) # 내 모든 리뷰
    review_cnt = len(mymovies) # 가중치 점수를 매길 값은 길이로 매길 것.
    point = {} # 점수 파싱 할 것.
    for review in mymovies: # 내가 쓴 리뷰들을 돌면서 (review의 _set 매니저가 mymovies)
        movie_id = review.movie.id # 리뷰가 참조하는 영화 id 받기
        
        # 그 영화 id로 장르를 순회
        movie = Movie.objects.get(id=movie_id)
        for genre in movie.genres.all():
            genre_pk = genre.pk # 현재 장르 pk
            if point.get(genre_pk, 0):
                point[genre_pk]+=1/review_cnt # 하면서 점수
            else:
                point[genre_pk]=1/review_cnt # 없으면 만들기
    
    movies = list(Movie.objects.all()) # 모든 영화들
    heap = [] # 10개 뽑을 힙.
    가중치 = [0] * len(movies) # 가중치 점수를 매길 리스트. 가중치는 영화 평균 점수 + 장르 점수
    for i in range(len(movies)): # 영화들 전부 돌면서
        movie = movies[i] # 영화를 선정
        가중치[i] += movie.vote_average # 가중치에 영화 평균 점수
        for genre in movie.genres.all(): # 장르 점수 더하기
            가중치[i] += point.get(genre.pk, 0)
        heappush(heap, (-가중치[i], i)) # 힙에 넣어준다. 점수가 높은 순이므로 최대힙으로.

    recommend_list = list() # 추천 영화 리스트
    for i in range(10): # 10개 선정
        p, idx = heappop(heap) # 점수, 영화 idx 선출
        recommend_list.append(movies[idx]) # 영화 idx로 movies에서 접근해서 원하는 영화 삽입

    # 반환
    context = {
        'recommend_list' : recommend_list
    }
    return render(request, 'movies/recommended.html', context)









