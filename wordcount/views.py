from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'name':'Hi Rahul , Welcome to WordCount website'})

def contact(request):
    return HttpResponse("<h2>This is my contact page</h2>")

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    # print(word_list)
    list_length = len(word_list)
    wordDictionary = {}
    for word in word_list:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sorted_list = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':data, 'words':list_length, 'word_dictionary':sorted_list})
