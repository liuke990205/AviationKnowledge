from django.shortcuts import render
import csv
from django.shortcuts import render, redirect
from django.contrib import messages

import json
import os
# Create your views here.
from django.http import HttpResponse
import operator


def toEntityRecognition(request):
    return render(request, 'entity_recognition.html')