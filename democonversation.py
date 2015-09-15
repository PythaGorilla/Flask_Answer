# -*- coding: utf-8 -*-
from datarep import DataRepository
from condata import ConversationData

from factory import *

dataobj = DataRepository()
convobj = ConversationData()


class DemoState:
    def get_next_state(self):
        pass

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Meat_901(DemoState):
    def __init__(self):
        self.stateid = '901'
        self.isFinal = False
        self.label = 'Like Meat'

    def getNextState(self, uid, qid):
        out = dataobj.search_conv_log(uid, qid)
        if (out == '1'):
            return Barbecue_903()
        else:
            return Fish_902()


class Fish_902(DemoState):
    def __init__(self):
        self.stateid = '902'
        self.isFinal = False
        self.label = 'Like fish'

    def getNextState(self, uid, cid):
        out = dataobj.search_conv_log(uid, cid)
        if (out == '1'):
            return Spicy_Sauce_906()
        else:
            return Club_Sandwich_909()


class Barbecue_903(DemoState):
    def __init__(self):
        self.stateid = '903'
        self.isFinal = False
        self.label = 'Like the Smell of Barbecue'

    def getNextState(self, uid, cid):
        out = dataobj.search_conv_log(uid, cid)
        if (out == '1'):
            return Ribs_904()
        else:
            return Beef_Kung_Pao_905()


class Ribs_904(DemoState):
    def __init__(self):
        self.stateid = '904'
        self.isFinal = True
        self.label = 'Baby back ribs'

    def getNextState(self, uid, cid):
        return Ribs_904()


class Beef_Kung_Pao_905(DemoState):
    def __init__(self):
        self.stateid = '905'
        self.isFinal = True
        self.label = 'Beef Kung Pao'

    def getNextState(self, uid, cid):
        return Beef_Kung_Pao_905()


class Spicy_Sauce_906(DemoState):
    def __init__(self):
        self.stateid = '906'
        self.isFinal = False
        self.label = 'Sweet Sauce'

    def getNextState(self, uid, cid):
        out = dataobj.search_conv_log(uid, cid)
        if (out == '1'):
            return Szechuan_Shrimp_907()
        else:
            return Lemon_Fish_908()


class Szechuan_Shrimp_907(DemoState):
    def __init__(self):
        self.stateid = '907'
        self.isFinal = True
        self.label = 'Szechuan Shrimps'

    def getNextState(self, uid, cid):
        return Szechuan_Shrimp_907()


class Lemon_Fish_908(DemoState):
    def __init__(self):
        self.stateid = '908'
        self.isFinal = True
        self.label = 'Lemon fish'

    def getNextState(self, uid, cid):
        return Lemon_Fish_908()


class Club_Sandwich_909(DemoState):
    def __init__(self):
        self.stateid = '909'
        self.isFinal = True
        self.label = 'Club Sandwich'

    def getNextState(self, uid, cid):
        return Club_Sandwich_909()
