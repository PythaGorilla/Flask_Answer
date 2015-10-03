__author__ = 'Jian Mo'
import urllib2,urllib
import json
import time, datetime
from flask import Flask, render_template, request, jsonify


url_start = "http://127.0.0.1/start_planning/"
url_choice="http://127.0.0.1/get_cur_conv/"
url_answer="http://127.0.0.1/post_conv/"



def start_planning(url_start,uid="2",cid="1"):
    data = {"uid":uid,"cid":cid}
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

def post_answer(url_answer,uid,qid,choice):
    data = {"uid": uid,"qid":qid,"choice":choice}
    data = json.dumps(data)
    req = urllib2.Request(url_answer, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()

    return response

class JsonParser():
    def __init__(self,jdata):
        print jdata
        self.data_dict=json.loads(jdata.replace('\r\n', '\\r\\n'))
        self.choiceType_id=self.data_dict["data"]["choiceType"]["id"]
        self.choiceType_text=self.data_dict["data"]["choiceType"]["type"]
        self.choices_id=[i["id"] for i in self.data_dict["data"]["choices"]]
        self.choices_text=[i["text"] for i in self.data_dict["data"]["choices"]]
        self.context=self.data_dict["data"]["context"]
        self.question=self.data_dict["data"]["question"]
        self.questionID=self.data_dict["data"]["questionId"]
        self.theme=self.data_dict["data"]["theme"]
        self.transitionText=self.data_dict["data"]["transitionText"][0]


# print star_planning(url_start)
# #print get_question(url_choice)
# print post_answer(url_answer,"1","101","1")
# print post_answer(url_answer,"1","102","1")
# # print post_answer(url_answer,"102","2")
#
