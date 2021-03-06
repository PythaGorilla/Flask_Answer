# Webservice to log Events to Warehouse and Adobe Campaign
from os import abort
from flask import Flask, render_template, request, jsonify
from factory import StateFactory
from datarep import DataRepository
from condata import ConversationData
import sys
# import happybase
import datetime

# Initialize the Flask application
app = Flask(__name__)
app.debug = True

# Initialize Data Repository Class
dataobj = DataRepository()
# Intialize Conversation Data Class
convobj = ConversationData()
# Intialize State Factory Class
stateobj = StateFactory()

HOST = '0.0.0.0'
PORT = 80
PREFIX = '/dev/1.0/convmanager/'


# Start Planning API
@app.route(PREFIX + 'start_planning/', methods=['POST'])
def start_planning():
    if not request.json:
        abort(400)
    else:
        try:
            json = request.json
            userid = json['uid']
            dataobj.update_context(userid, '1')
            dataobj.update_state_table(userid, '101', '101')
            print "ok1"
            state = stateobj.start_conv_mgr(userid, '101', '1')
            print "ok2"
            out = state.getConversationData('101', int(userid))
            print "ok3"

            return out
        except Exception as e:
            print e
            print "Cannot Start Planning"


# Start Update Planning API
@app.route(PREFIX + 'update_planning/', methods=['POST'])
def update_planning():
    if not request.json:
        abort(400)
    else:
        try:
            json = request.json
            userid = json['uid']
            dataobj.update_context(userid, '2')
            dataobj.update_state_table(userid, '201', '201')
            state = stateobj.start_conv_mgr(userid, '201', '2')
            out = state.getConversationData('201', userid)
            return out
        except Exception as e:
            print e
            print "Cannot start Update Planning"

            # Get Current conversation API


@app.route(PREFIX + 'get_cur_conv/', methods=['GET'])
def get_question():
    if not request.args:
        abort(400)
    else:
        try:
            uid = request.args.get('uid')
            userid = str(uid)
            sid = dataobj.get_current_state_id(userid)
            if not (sid == ""):
                cid = dataobj.get_context(uid)
                state = stateobj.start_conv_mgr(userid, sid, cid)
                out = state.getConversationData(state.stateid, userid)
                return out
            elif (sid == ''):
                dataobj.update_context(userid, '1')
                dataobj.update_state_table(userid, '101', '101')
                state = stateobj.start_conv_mgr(userid, '101', '1')
                out = state.getConversationData('101', userid)
                return out
        except Exception as e:
            print e
            print "Cannot Get the Current Conversation"


# Post Conversation Answers
@app.route(PREFIX + 'post_conv/', methods=['POST'])
def post():
    if not request.json:
        abort(400)
    else:
        try:
            json = request.json
            uid = json['uid']
            cur_state = json['qid']
            choice = json['choice']
            time = datetime.datetime.utcnow()
            key = json['uid'] + ":" + json['qid'] + ":" + str(time)

            dataobj.post_conv_data(uid, cur_state, choice)
            cid = dataobj.get_context(uid)
            state = stateobj.start_conv_mgr(uid, cur_state, cid)
            print "ok4"
            new_state = state.getNextState(uid, cur_state)
            print "ok5"
            dataobj.update_state_table(uid, new_state.stateid, cur_state)
            print "ok6"
            return new_state.getConversationData(new_state.stateid, uid)
        except Exception as e:
            print e
            print "Cannot Post Conversation"

        # Run


if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT
    )
