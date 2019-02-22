from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
import os
import subprocess
import json
import csv
import requests
import random

import requests
from pprint import pprint as pp

endpoint = 'https://shellfishsearch.search.windows.net/indexes/documentdb-index/docs?api-version=2017-11-11&$count=true&queryType=full&$select=*&search="' #Doe,Jane 1"
api_key = '0B16609C8404A9314BAEB433A64F0276'
headers = {'api-key': api_key, 'Accept': 'application/json'}

def index(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            print(request.user, " Is being Logged Out")
            logout(request)

        else:
            name = request.POST['user_name']
            passw = request.POST['pass_word']
            user = authenticate(request, username=name, password=passw)
            if user is not None:
                print(user)
                login(request, user)
            else:
                print("User Login Not Recognized: Access Denied")

    return render(request, 'home.html')

@login_required
def search(request):
    print(request)
    result = []
    types = {}
    filters = []
    majQuerier = []
    words = []
    wordsFound = []
    disc = 'ALL'
    filterString = ""
    profiles = Profile.objects.all()
    num = len(profiles)
    try:
        '''
        if 'major-query' in request.GET and request.GET['major-query']:
            for word in request.GET['major-query'].replace('!',' ').replace('?',' ').replace('.',' ').replace(';',' ').replace(',',' ').split():
                print(num, word + '\n')
                if(word != ''):
                    profiles = profiles.filter(about__icontains=word)
                if(num != len(profiles)):
                    num = len(profiles)
                    wordsFound.append(word)
            print(num)
            query = { 'text' : request.GET['major-query'], 'filters':{'type':filters, 'disciplines': [disc] }}
            result = requests.post('http://127.0.0.1:5000/search', json=query).json()
            types = {"Yrs. Experience":0,"Current Relevance":0,"Office Location":0,"Availability":0}
            result = result['results']
        '''
        temp_endpoint = endpoint + request.GET['major-query'] + '"'
        r = requests.get(temp_endpoint, headers=headers)
        raw_result = r.json()
        result = raw_result['value']
        for res in result:
            res['title'] = res['Name']
        types = {"Yrs. Experience":0,"Current Relevance":0,"Office Location":0,"Availability":0}
        query = { 'text' : request.GET['major-query'], 'filters':{'type':filters, 'disciplines': [disc] }}
            
    except:
        result = '[{"qa": false, "name": "Connection Error", "missing": "", "did": 1, "related": "", "etime": "Tue Aug  8 08:17:56 2017", "snip": ["Connection", "Error"], "score": 94, "answer": "", "path": "Cannot Reach RQA", "size": "", "type": "pptx", "ctime": "Thu Nov 21 05:18:46 2018"}]'
        types = {"Yrs. Experience":0,"Current Relevance":0,"Office Location":0,"Availability":0}
        result = json.loads(result)
    page = request.GET.get('page',1)
    paginator = Paginator(result, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'result.html', {'profiles': list(result), 'users': users, 'pastSearch': request.GET['major-query'], 'types': types, 'majQuerier' : majQuerier, 'words': wordsFound, 'disc':disc, 'filterString':filterString})

@login_required
def profile(request, title = None, document = None):
    print(title)
    temp_endpoint = endpoint + title + '"'
    r = requests.get(temp_endpoint, headers=headers)
    raw_result = r.json()
    #print(len(raw_result['value']))
    #print(raw_result['@odata.count'])
    if (raw_result['@odata.count'] == 1):
        #prof = Profile.objects.get(title = title)
        file_path = os.path.dirname(__file__)
        if file_path != "":
            os.chdir(file_path)
        print(os.getcwd())    
        pdf_names = []
        with open('file_names.csv', 'r') as f:
            reader = csv.reader(f)
            for stuff in reader:
              pdf_names.append(stuff[0])

        num_possible = len(pdf_names)
        num_chose = random.randint(1,10)
        print(num_possible)
        print(num_chose)
        file_names = []
        if(num_possible > 0):
            for i in range(num_chose):
                choice = random.randint(0,num_possible-1);
                file_names.append({"pdf": (pdf_names[choice] + '.pdf'), "jpg": (pdf_names[choice] + '.jpg')})
        return render(request, "profile.html", {"title": title, "profile": raw_result['value'][0], "documents": file_names}) #return render(request, 'profile.html')
    else:
        return render(request, "not_found.html");

@login_required
def item(request, document = None):
    if(document == None):
        return render(request, "not_found.html");
    else:
        try:
            file_path = os.path.dirname(__file__)
            if file_path != "":
                os.chdir(file_path)
            temp_split = document.split('.')
            if (temp_split[-1] == 'pdf'): # return pdf 
                return FileResponse(open("../../../ECEN403/library/"+document,"rb"), content_type='application/pdf')
            else: # return jpg
                return FileResponse(open("../../../ECEN403/thumbnails/"+document,"rb"), content_type='image/jpeg')
        except FileNotFoundError:
            return render(request, "not_found.html");s

'''
class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all() #.order_by('-date_joined')
    serializer_class = ProfileSerializer
'''