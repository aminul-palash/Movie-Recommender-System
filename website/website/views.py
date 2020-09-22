# Create your views here.
from django.shortcuts import render

from django.views.generic.base import TemplateView

class index(TemplateView):
    template_name = 'home.html'

    def __init__(self):
        self.movie_name = ''
        self. movie_list = ''
    def get(self,request):
        return render(request, 'index.html',{'movie_list':movie_list})

    def post(self,request):
        self.movie_list = request.POST['serach']

        if self.movie_list != '':
            try:
                pass
            except:
                pass
        return render(request, 'index.html',{'movie_list':movie_list})