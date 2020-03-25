from django.http import HttpResponse
from django.shortcuts import render
import operator
import string

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=[x.strip(string.punctuation)for x in fulltext.split()]
    repeat={}
    for x in wordlist:
        if x in repeat:
            repeat[x]+=1
        else:
            repeat[x]=1
    organized=sorted(repeat.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'repeat':organized})

def about(request):
    return render(request,'about.html')
