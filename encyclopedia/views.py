from multiprocessing import Condition
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponse as hr
from django import forms
from urllib3 import HTTPResponse
from django.http import HttpResponseRedirect as hrr

from . import util
import markdown as m
from django import forms
import os
import random

class yessir(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget= forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def openWtitle(request, name):
    for i in util.list_entries():
        if name == i or name == i.lower():
            return render(request, "encyclopedia/showtitles.html", {
                "heading": name,
                "content": m.markdown(util.get_entry(name))
            })
    return render(request, "encyclopedia/error.html", {
        "heading": "Error",
        "content": "Requested page couldn't be found :("
    })

def bro(request):
    templist = []
    if request.method == 'POST':
        value = request.POST.get('q')
    for i in util.list_entries():
        if value == i.lower():
            return render(request, "encyclopedia/showtitles.html", {
                "heading": value,
                "content": m.markdown(util.get_entry(value))
            })
        elif value in i.lower():
            templist.append(i)
    return render(request, "encyclopedia/index.html", {
        "entries": templist
    })

def newpage(request):
    form = yessir()
    return render(request, "encyclopedia/newadd.html", {
        'form': form
    })

def save(request):
    if request.method == 'POST':
        tt = request.POST.get('title')
        ct = request.POST.get('content')
        cond = True
        for i in util.list_entries():
            if tt.lower() == i.lower():
                cond = False
                return render(request, 'encyclopedia/error.html', {
                    'heading': 'error',
                    'content': "File already exist"
                })
        if cond == True:
            ct = "#" + tt + "\n" + ct
            util.save_entry(tt, ct)
            return render(request, 'encyclopedia/showtitles.html', {
                'heading': tt,
                'content': m.markdown(util.get_entry(tt))
            })

def edit(request):
    pagename = request.POST.get("thevalue")
    content = util.get_entry(pagename)
    content = content
    form = yessir(initial={'title':pagename, 'content': content})
    return render(request, 'encyclopedia/newpage.html', {
        "form": form
    })

def rand(request):
    c = random.choice(util.list_entries())
    return render(request, 'encyclopedia/showtitles.html', {
        'heading': c,
        'content': m.markdown(util.get_entry(c))
    })

def savenew(request):
    if request.method == 'POST':
        tt = request.POST.get('title')
        ct = request.POST.get('content')
        util.save_entry(tt, ct)
        return render(request, 'encyclopedia/showtitles.html', {
            'heading': tt,
            'content': m.markdown(util.get_entry(tt))
        })