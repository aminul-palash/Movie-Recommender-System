# Create your views here.
from django.shortcuts import render

from django.views.generic.base import TemplateView
import pandas as pd 
import requests

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_df = pd.read_csv('website/main_data.csv')

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_df['genres'])
similarity = cosine_similarity(count_matrix)


api_url = 'https://api.themoviedb.org/3/search/movie?api_key=41f7cc5e1134d127a09413c900d5f199'

def get_cast(movie_id):
    
    p = 'https://api.themoviedb.org/3/movie/'+movie_id+'/credits?api_key=41f7cc5e1134d127a09413c900d5f199'
    r = requests.get(url = p) 
    con = r.json() 
    cast = []
   
    for i in con['cast']:
        # s = 'image.tmdb.org/t/p/w138_and_h175_face' + 
        # print(s,type(s))
        p = {
            #
            'character':i['character'],
            'name':i['name'],
            'profile_path': i['profile_path'],
        }
        cast.append(p)
    return cast
    

def get_trailer(movie_id):
    try:
        p = 'https://api.themoviedb.org/3/movie/'+movie_id+'/videos?api_key=41f7cc5e1134d127a09413c900d5f199'
        r = requests.get(url = p) 
        con = r.json() 
        return 'https://www.youtube.com/watch?v=' + con['results'][0]['key']
    except:
        return None

def get_genres(movie_id):
    
    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key=41f7cc5e1134d127a09413c900d5f199'
    r = requests.get(url = url) 
    con = r.json() 
    p = ''
    for i in con['genres']:
        p += i['name']+" "
    return p, str(con['runtime']//60) +'h '+ str(con['runtime']%60 )+'m'


class index(TemplateView):
    template_name = 'home.html'

    def __init__(self):
        self.movie_name = ''
        self. movie_list = {}
        
    def get(self,request):
        return render(request, 'home.html',{'movie_list':self.movie_list})

    def post(self,request):
        self.movie_name = request.POST['movie']
        
        title = self.movie_name
        PARAMS = {'query':title} 
        # sending get request and saving the response as response object 
        r = requests.get(url = api_url, params = PARAMS) 
        config = r.json() 
        movie_id = str(config['results'][0]['id'])
        genres,runtime = get_genres(movie_id)
        trailer = get_trailer(movie_id)
        cast = get_cast(movie_id)
        config = {
            'title':config['results'][0]['title'],
            'poster_path':config['results'][0]['poster_path'],
            'overview':config['results'][0]['overview'],
            'release_date':config['results'][0]['release_date'].split('-')[0],
            'genres':genres,
            'runtime':runtime,
            'trailer':trailer,
            'cast':cast,
        }
        if self.movie_list != '':
            # try:
                self. movie_list = rcmd(self.movie_name)
                print(self. movie_list)
                recommended_movies = []
                data={}
                print(type(self. movie_list))
                if self.movie_list !=None:
                    for i in self.movie_list:
                        # print(i)
                        r = requests.get(url = api_url, params = {'query':i} ) 
                        item = r.json() 
                        # print(item,"===================================")
                        try:
                            movie_id = str(item['results'][0]['id'])
                        except:
                            continue
                        genres,runtime = get_genres(movie_id)
                        
                        trailer = get_trailer(movie_id)
                        cast = get_cast(movie_id)
                        
                        data = {
                                    'title':item['results'][0]['title'],
                                    'poster_path':item['results'][0]['poster_path'],
                                    'overview':item['results'][0]['overview'],
                                    'release_date':item['results'][0]['release_date'].split('-')[0],
                                    'genres':genres,
                                    'runtime':runtime,
                                    'trailer':trailer,
                                    'cast':cast,
                                }
                        recommended_movies.append(data)
                        data = {}
                    print(recommended_movies)
                
                    

            # except:
            #     pass
        return render(request, 'home.html',{'config':config,'recommended_movies':recommended_movies})



def rcmd(m):
    print(m)
    m = m.lower()
    movies_df.head()
    similarity.shape
    # if len(data[data['title']==m])!=1:

    if m not in movies_df['title'].unique():
        pass
    else:
        i = movies_df.loc[movies_df['title']==m].index[0]
        print(i)
        lst = list(enumerate(similarity[i]))
        
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(movies_df['title'][a])
        return l