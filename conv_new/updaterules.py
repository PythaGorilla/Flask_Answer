# -*- coding: utf-8 -*-
from datarep import DataRepository
from condata import ConversationData
from factory import *

#Initialize Data Repository Class  
dataobj = DataRepository()

#Intialize Conversation Data Class
convobj = ConversationData()

#Update State Base Class
class Update_State:
    def get_next_state(self):
        pass
        
#Update States
class Contextualisation1_201(Update_State):

    def __init__(self):
        self.stateid = '201'
        self.isFinal = False
        self.label = 'Contextualisation1'   

    def getNextState(self,uid,cid):
        return Plaisir_202()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	

class Plaisir_202(Update_State):

    def __init__(self):
        self.stateid = '202'
        self.isFinal = False
        self.label = 'Plaisir'   

    def getNextState(self,uid,cid):
        return Barrieres_difficulte1_203()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	
        
class Barrieres_difficulte1_203(Update_State):

    def __init__(self):
        self.stateid = '203'
        self.isFinal = False
        self.label = 'Barriers'   

    def getNextState(self,uid,cid):
        return Intention_204()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	
                        
class Intention_204(Update_State):

    def __init__(self):
        self.stateid = '204'
        self.isFinal = False
        self.label = 'Intention'   

    def getNextState(self,uid,cid):
        return End_205()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	
 
class End_205(Update_State):

    def __init__(self):
        self.stateid = '205'
        self.isFinal = False
        self.label = 'End'   

    def getNextState(self,uid,cid):
        return Idle_206()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	
        
class Idle_206(Update_State):

    def __init__(self):
        self.stateid = '206'
        self.isFinal = False
        self.label = 'Idle'   

    def getNextState(self,uid,cid):
        return Idle_206()

    def getConversationData(self,qid,uid): 
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row,qid,uid)	               