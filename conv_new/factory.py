# -*- coding: utf-8 -*-
from planrules import *
from updaterules import *


# Abstract Factory
class StateFactory(object):
    @staticmethod
    def start_conv_mgr(uid, sid, cid):
        userid = uid
        stateid = sid
        contextid = cid
        factory = StateFactory.get_factory(contextid)
        state = factory.exec_state(sid)
        return state

    @staticmethod
    def get_factory(factory):
        if factory == '1':
            return PlanningFactory()
        elif factory == '2':
            return UpdateFactory()
        raise TypeError('Unknown Factory')


# Planning Factory
class PlanningFactory(object):
    def exec_state(self, sid):
        try:
            options = {'101': Contextualisation_101, '102': Proposition_objectifs_102, '103': Proposition_objectifs_103,
                       '104': Explorer_volets_104,
                       '105': Explorer_modules_105, '106': Objectif_106, '107': Proposition_objectifs_107,
                       '108': Debuter_semaine_108,
                       '109': Explorer_volets_109, '110': Explorer_modules_110, '111': Objectif_111,
                       '112': Proposition_objectifs_112,
                       '113': Fin_planification1_113, '114': Fin_planification2_114, '115': Fin_planification1_115,
                       '116': Idle_116}
            return options[sid]()
        except:
            print "No state available in Plannification"

            # Update Factory


class UpdateFactory(object):
    def exec_state(self, sid):
        try:
            options = {'201': Contextualisation1_201, '202': Plaisir_202, '203': Barrieres_difficulte1_203,
                       '204': Intention_204,
                       '205': End_205, '206': Idle_206}
            return options[sid]()
        except:
            print "No state available in Meso Point"
