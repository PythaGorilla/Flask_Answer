from datarep import DataRepository
import json

# Initialize Data Repository Class
dataobj = DataRepository()


# Conversation Data class which gets the Conversation Data from database
class ConversationData:
    # Method to Get the Question Id for JSON
    def get_question_id(self, qid):
        return qid

        # Method to get Question Text for JSON

    def get_question_text(self, ques):
        return ques

        # Method to Get choices for JSON

    def get_choices(self, choice_set):
        out = []
        data = choice_set.split(":")
        for item in data:
            d = []
            d = item.split("-")
            out.append({"id": d[0], "text": d[1]})
        return out

        # Method to Get Theme for JSON

    def get_theme(self, theme):
        return theme

    # Method to Get Transition text for JSON
    def get_transition_text(self, ttext):
        out = []
        out = ttext.split(":")
        return out

    # Method to Get Context for JSON
    def get_context(self, context):
        return context

        # Method to Get Choice Type Details for JSON

    def get_choice_type(self, ctype, uid):
        out = {}
        userid = str(uid)
        if not (ctype == "choice" or ctype == "EOS"):
            prev_sid = dataobj.get_prev_state_id(uid)
            print "i'm in condata.py"
            chid = dataobj.search_conv_log(uid, prev_sid)
            id = chid
        else:
            id = 0
        out.update({"type": ctype})
        out.update({"id": id})
        return out

    # Method which retreives converation data in JSON format
    def get_json_data(self, row, qid, uid):
        self.data = ConversationData()

        self.data.questionId = self.get_question_id(qid)
        self.data.theme = self.get_theme(row['theme'])
        self.data.context = self.get_context(row['context'])
        self.data.choiceType = self.get_choice_type(row['ctype'], uid)
        if 'ques' in row:
            self.data.question = self.get_question_text(row['ques'])
        else:
            self.data.question = ""
        if 'choices' in row:
            self.data.choices = self.get_choices(row['choices'])
        else:
            self.data.choices = []
        if 'ttext' in row:
            self.data.transitionText = self.get_transition_text(row['ttext'])
        else:
            self.data.transitionText = []
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4).decode('unicode-escape').encode(
            'utf8')
