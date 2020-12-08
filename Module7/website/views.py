from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template import Context
import json
import requests

# Create your views here.

# def welcome(request):
#     return HttpResponse("Welcome!")

# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out")
#     return redirect(welcome)

def register(request):
    return render(request, 'registration/register.html')

def registering(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    user = User.objects.create_user(username, email, password)
    return redirect("/")

#cite: https://developer.oxforddictionaries.com/documentation/making-requests-to-the-api
def wordSearch(request):
  
    # #search box
    # html = "<form action = \"word_lookup\" method = \"GET\" id = \"word_lookup\">"
    # html += "<input type = \"text\" name = \"target_word\" id = \"target_word\">"
    # html += "<input type = \"submit\" value = \"Search\" id = \"searchDictionary\">"
    # html += "</form>"

    # #return to home
    # html += "<form action = \"/\" method = \"GET\" id = \"word_lookup\">"
    # html += "<input type = \"submit\" value = \"Home Page\" id = \"homeRedirect\">"
    # html += "</form>"

    # #Oxford API request
    # app_id  = "602817c9"
    # app_key  = "c62076f0b4388a9fb6e1d3ccd40b1faa"
    # language_code = "en-us"
    # endpoint = "entries"
    # word_id = request.GET["target_word"]
    # url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id

    # r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

    # #etymology
    # try:
    #     html += "<b>"+word_id+"</b>"
    #     html += "<div id = \"etymology\">Etymology: "+r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]+"</div>"
    # except KeyError:
    #     html += "<div id = \"failedSearch\">No dictionary results found for "+word_id+"</div>"
    #     return HttpResponse(html) 

    # #phonetic spelling
    # html += "<div id = sound>Phonetic spelling: "+r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["phoneticSpelling"]+"<br>"
    
    # #audio pronunciation
    # html += "<audio controls><source src = "+r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][1]["audioFile"]+" type=\"audio/mpeg\">Your browser does not support audio.</audio></div>"

    # #definitions
    # allEntries = r.json()["results"][0]["lexicalEntries"]
    # for entry in allEntries:
    #     html += "<div id = \"definitions\"><i>"+entry["lexicalCategory"]["text"]+": </i><ul>"
    #     allDefinitions = entry['entries'][0]['senses']
    #     for i in allDefinitions:
    #         html += "<li>"+i['definitions'][0]+"</li>"
    #     html += "</ul></div>"

    # return HttpResponse(html)
    

    #Oxford API request
    app_id  = "602817c9"
    app_key  = "c62076f0b4388a9fb6e1d3ccd40b1faa"
    language_code = "en-us"
    endpoint = "entries"
    word_id = request.GET["target_word"]
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id

    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

    template_name = "result.html"

    #etymology
    etymology = ""
    try:
        etymology += "<b>"+word_id+"</b>"
        etymology += "<div id = \"etymology\">Etymology: "+r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]+"</div>"
    except KeyError:
        notFound = true
        context = {
            "notFound" : notFound
        }
        return render(request, template_name, context) 

    #phonetic spelling
    phoneticSpelling = r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["phoneticSpelling"]
    
    #audio pronunciation
    audioSource = r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][1]["audioFile"]

    #definitions
    allEntries = r.json()["results"][0]["lexicalEntries"]
    definitions = ""
    for entry in allEntries:
        definitions += "<div id = \"definition\"><i>"+entry["lexicalCategory"]["text"]+": </i><ul>"
        allDefinitions = entry['entries'][0]['senses']
        for i in allDefinitions:
            definitions += "<li>"+i['definitions'][0]+"</li>"
        definitions += "</ul></div>"

    context = {
        "phoneticSpelling" : phoneticSpelling,
        "audioSource" : audioSource,
        "listDefinitions" : definitions,
        "etymology" : etymology
    }

    return render(request, template_name, context) 