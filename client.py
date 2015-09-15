__author__ = 'Jian Mo'
import urllib2,urllib
import json
import time, datetime

url_start = "http://127.0.0.1/dev/1.0/convmanager/start_planning/"
url_choice="http://127.0.0.1/dev/1.0/convmanager/get_cur_conv"
url_answer="http://127.0.0.1/dev/1.0/convmanager/post_conv/"
def star_planning(url_start):
    data = {"uid": "2","cid":"41"}
    data = json.dumps(data)
    req = urllib2.Request(url_start, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()

    return response

def get_question(url_choice):
     payload = {'uid': '1'}
     data = urllib.urlencode(payload)
     # print data
     # req = urllib2.Request(url_choice, data)
     url=url_choice+"?"+data
     f = urllib2.urlopen(url)
     response = f.read()
     return response

def post_answer(url_answer,qid,choice):
    data = {"uid": "1","qid":qid,"choice":choice}
    data = json.dumps(data)
    req = urllib2.Request(url_answer, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()

    return response

print star_planning(url_start)
#print get_question(url_choice)
print post_answer(url_answer,"101","1")
print post_answer(url_answer,"102","1")
print post_answer(url_answer,"102","2")

