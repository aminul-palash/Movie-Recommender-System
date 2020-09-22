# Create your views here.
from django.shortcuts import render

from django.views.generic.base import TemplateView
import pandas as pd 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_df = pd.read_csv('website/main_data.csv')

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_df['genres'])
similarity = cosine_similarity(count_matrix)



class index(TemplateView):
    template_name = 'home.html'

    def __init__(self):
        self.movie_name = ''
        self. movie_list = {}
    def get(self,request):
        return render(request, 'home.html',{'movie_list':self.movie_list})

    def post(self,request):
        self.movie_name = request.POST['movie']

        if self.movie_list != '':
            try:
                self. movie_list = rcmd(self.movie_name)
            except:
                pass
        return render(request, 'home.html',{'movie_list':self.movie_list})



def rcmd(m):
    print(m)
    m = m.lower()
    movies_df.head()
    similarity.shape
    
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