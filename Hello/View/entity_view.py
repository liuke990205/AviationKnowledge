import csv

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from Hello.ner_ch.src.lstm_crf.main import NER


def toEntityRecognition(request):
    return render(request, 'entity_recognition.html')


def convert(dict, sentence):
    lables = {'AIR': '航空器', 'WEA': '武器', 'MATH': '数学模型', 'SYS': '系统', 'TAR': '性能指标', 'DOC': '参考文档'}
    list = []
    s = 0
    end = len(sentence)

    def function(date):
        return date['start']

    dict.sort(key=function)
    for t in dict:
        start = t['start']
        stop = t['stop']
        type = lables[t['type']]
        if t['start'] > s:
            data = { 'str': sentence[s:start], 'type': 'none'}
            list.append(data)
        data = {'str': sentence[start:stop], 'type': type}
        list.append(data)
        s = stop
        end = stop
    if len(sentence) > end:
        data = {'str': sentence[end:len(sentence)], 'type': 'none'}
        list.append(data)
    return list


def save(list):
    lables = {'AIR': '航空器', 'WEA': '武器', 'MATH': '数学模型', 'SYS': '系统', 'TAR': '性能指标', 'DOC': '参考文档'}
    dict = {}
    dicfile = 'Hello/ner_ch/data/dic.csv'
    with open(dicfile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dict[row[1]] = row[2]
            n = int(row[0])
    add = []
    for t in list:
        word = t['word']
        type = lables[t['type']]
        if word not in dict.keys():
            dict[word] = type
            temp = [n + 1, word, type]
            add.append(temp)
            n = n + 1
    with open(dicfile, "a+", newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerows(add)


def ner(request):
    list = []
    if request.POST:
        sentence = request.POST.get('sentence', None)
        if sentence:
            sentence = sentence.replace(" ", "")
            cn = NER("predict")
            temp = cn.predict(sentence)
            list = convert(temp, sentence)
            save(temp)
    request.session['doc'] = list
    return redirect('/display_result/')


def upload2(request):
    if request.method == 'POST':
        # 获取文件名
        file = request.FILES.get('file')
        if file:
            new_data = []
            with open('Hello/ner_ch/data/uploadfile.txt', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            with open('Hello/ner_ch/data/uploadfile.txt', "r", encoding="utf-8") as lines:
                dataList = lines.readlines()
                for data in dataList:
                    data = data.strip('\n')
                    new_data.append(data)
            list = []
            cn = NER("predict")
            for sentence in new_data:
                sentence = sentence.replace(" ", "")
                temp = cn.predict(sentence)
                list.extend(convert(temp, sentence))
                list.append({'index': '', 'str': '', 'type': 'enter'})
                save(temp)
            request.session['doc'] = list
            return redirect('/display_result/')
        else:
            messages.success(request, "文件为空！")
            return redirect('/ner/')


def display_result(request):
    doc = request.session.get('doc')
    resultList = []
    for li in doc:
        if (li['type'] != 'none') & (li['type'] != 'enter'):
            resultList.append(li)
    print(resultList)
    return render(request, 'entity_recognition.html', {'doc': doc, 'resultList': resultList})



def modifyEntity(request):
    entity = request.POST.get('Entity')
    entityType = request.POST.get('EntityType')
    print(entity, entityType)

    pass