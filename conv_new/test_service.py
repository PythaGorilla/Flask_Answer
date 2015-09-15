# Webservice to log Events to Warehouse and Adobe Campaign 
from flask import Flask, render_template, request, jsonify
from factory import StateFactory
from datarep import DataRepository
from condata import ConversationData
import sys
import happybase
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

HOST = '10.36.32.111'
PORT = 4322
PREFIX = '/dev/1.0/convmanager/'


# Start Planning API
@app.route(PREFIX + 'start_planning/', methods=['POST'])
def start_planning():
    if not request.json:
        abort(400)
    else:
        try:
            json = request.json
            uid = json['uid']
            # dataobj.update_context(uid,'1')
            # dataobj.update_state_table(uid,'101','101')
            return convobj.get_json_data('101', uid)
        except:
            print "Cannot Start Planning"


# Start Update Planning API
@app.route(PREFIX + 'update_planning/', methods=['POST'])
def update_planning():
    if not request.json:
        abort(400)
    else:
        try:
            json = request.json
            uid = json['uid']
            dataobj.update_context(uid, '2')
            dataobj.update_state_table(uid, '201', '201')
            return convobj.get_json_data('201', uid)
        except:
            print "Cannot start Update Planning"

            # Get Current conversation API


@app.route(PREFIX + 'get_cur_conv/', methods=['GET'])
def get_question():
    if not request.args:
        abort(400)
    else:
        try:
            uid = request.args.get('uid')
            sid = dataobj.get_current_state_id(uid)
            if (sid != ''):
                return convobj.get_json_data(sid, uid)
            elif (sid == ''):
                dataobj.update_context(uid, '1')
                dataobj.update_state_table(uid, '101', '101')
        except:
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
            time = datetime.datetime.utcnow()
            key = json['uid'] + ":" + json['qid'] + ":" + str(time)
            ch = ':'.join(json['choice'])
            dataobj.post_conv_data(key, json['qid'], ch)
            cid = dataobj.get_context(uid)
            sid = stateobj.start_conv_mgr(uid, json['qid'], cid)
            # dataobj.update_state_table(uid,sid,json['qid'])
            return convobj.get_json_data('101')
        except:
            print "Cannot Post Conversation"

        # Run


if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT
    )
