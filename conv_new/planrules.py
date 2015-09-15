# -*- coding: utf-8 -*-
from datarep import DataRepository
from condata import ConversationData
from mock import mockdb

from factory import *

# Initialize Data Repository Class
dataobj = DataRepository()

# Intialize Conversation Data Class
convobj = ConversationData()

# Intialize MockDB Class for test
mockobj = mockdb()


# Planning State Base Class
class Plan_State:
    def get_next_state(self):
        pass


# Planning States
class Contextualisation_101(Plan_State):
    def __init__(self):
        self.stateid = '101'
        self.isFinal = False
        self.label = 'Contextualisation'

    def getNextState(self, uid, qid, mock=False):
        if mock == False:
            print "i'm in 101"
            out = dataobj.search_conv_log(uid, qid)
        elif mock == True:
            row = mockobj.read_csv()
            out = row[0][2]
        print
        if (out == '1'):
            return Proposition_objectifs_102()
        else:
            return Fin_planification1_115()

    def getConversationData(self, qid, uid):
        print "101 was called"
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)  # dump data into json


class Proposition_objectifs_102(Plan_State):
    def __init__(self):
        self.stateid = '102'
        self.isFinal = False
        self.label = 'Proposition_objectifs'

    def getNextState(self, uid, qid, mock=False):
        if mock == False:
            out = dataobj.search_conv_log(uid, qid)
        elif mock == True:
            row = mockobj.read_csv()
            out = row[0][2]

        if (out == '1'):
            return Proposition_objectifs_103()
        else:
            return Fin_planification1_115()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Proposition_objectifs_103(Plan_State):
    def __init__(self):
        self.stateid = '103'
        self.isFinal = False
        self.label = 'Proposition_objectifs'

    def getNextState(self, uid, qid):
        return Explorer_volets_104()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Explorer_volets_104(Plan_State):
    def __init__(self):
        self.stateid = '104'
        self.isFinal = False
        self.label = 'Explorer_volets'

    def getNextState(self, uid, qid):
        return Explorer_modules_105()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Explorer_modules_105(Plan_State):
    def __init__(self):
        self.stateid = '105'
        self.isFinal = False
        self.label = 'Explorer_module'

    def getNextState(self, uid, qid, mock=False):
        if mock == False:
            out = dataobj.search_conv_log(uid, qid)
        elif mock == True:
            row = mockobj.read_csv()
            out = row[0][2]
        if (out == '1'):
            return Objectif_106()
        else:
            return Proposition_objectifs_107()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Objectif_106(Plan_State):
    def __init__(self):
        self.stateid = '106'
        self.isFinal = False
        self.label = 'Objectif'

    def getNextState(self, uid, qid):
        return Debuter_semaine_108()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Proposition_objectifs_107(Plan_State):
    def __init__(self):
        self.stateid = '107'
        self.isFinal = False
        self.label = 'Proposition_objectifs'

    def getNextState(self, uid, qid):
        return Debuter_semaine_108()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Debuter_semaine_108(Plan_State):
    def __init__(self):
        self.stateid = '108'
        self.isFinal = False
        self.label = 'Debuter_semaine'

    def getNextState(self, uid, qid, mock=False):
        if mock == False:
            out = dataobj.search_conv_log(uid, qid)
        elif mock == True:
            row = mockobj.read_csv()
            out = row[0][2]
        if (out == '4'):
            return Explorer_volets_109()
        elif (out == '5'):
            return Fin_planification2_114()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Explorer_volets_109(Plan_State):
    def __init__(self):
        self.stateid = '109'
        self.isFinal = False
        self.label = 'Explorer_volets'

    def getNextState(self, uid, qid):
        return Explorer_modules_110()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Explorer_modules_110(Plan_State):
    def __init__(self):
        self.stateid = '110'
        self.isFinal = False
        self.label = 'Explorer_modules'

    def getNextState(self, uid, qid, mock=False):
        if mock == False:
            out = dataobj.search_conv_log(uid, qid)
        elif mock == True:
            row = mockobj.read_csv()
            out = row[0][2]
        if (out == '1'):
            return Objectif_111()
        else:
            return Proposition_objectifs_112()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Objectif_111(Plan_State):
    def __init__(self):
        self.stateid = '111'
        self.isFinal = False
        self.label = 'Objectif'

    def getNextState(self, uid, qid):
        return Fin_planification1_113()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Proposition_objectifs_112(Plan_State):
    def __init__(self):
        self.stateid = '112'
        self.isFinal = False
        self.label = 'Proposition_objectifs'

    def getNextState(self, uid, qid):
        return Fin_planification1_113()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Fin_planification1_113(Plan_State):
    def __init__(self):
        self.stateid = '113'
        self.isFinal = False
        self.label = 'Fin_planification1'

    def getNextState(self, uid, qid):
        return Fin_planification2_114()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Fin_planification2_114(Plan_State):
    def __init__(self):
        self.stateid = '114'
        self.isFinal = False
        self.label = 'Fin_planification2'

    def getNextState(self, uid, qid):
        return Idle_116()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Fin_planification1_115(Plan_State):
    def __init__(self):
        self.stateid = '115'
        self.isFinal = False
        self.label = 'Contextualisation'

    def getNextState(self, uid, qid):
        return Idle_116()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)


class Idle_116(Plan_State):
    def __init__(self):
        self.stateid = '116'
        self.isFinal = True
        self.label = 'Idle State'

    def getNextState(self, uid, qid):
        return Idle_116()

    def getConversationData(self, qid, uid):
        row = dataobj.get_conv_data(qid)
        return convobj.get_json_data(row, qid, uid)
