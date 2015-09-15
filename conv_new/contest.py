from planruletest import *
from updateruletest import *
import unittest

#Class PlanningTestSuite consists of all Test Cases related to Planning
class PlanningTestSuite:
 #Initialize PlanningTestSuite Class    
 def __init__(self):
     suite = unittest.TestSuite()
     suite.addTest(unittest.makeSuite(Contextualisation_101_test))
     suite.addTest(unittest.makeSuite(Proposition_objectifs_102_test))
     suite.addTest(unittest.makeSuite(Proposition_objectifs_103_test))     
     suite.addTest(unittest.makeSuite(Explorer_volets_104_test))
     suite.addTest(unittest.makeSuite(Explorer_modules_105_test))
     suite.addTest(unittest.makeSuite(Objectif_106_test))
     suite.addTest(unittest.makeSuite(Proposition_objectifs_107_test))
     suite.addTest(unittest.makeSuite(Debuter_semaine_108_test))
     suite.addTest(unittest.makeSuite(Explorer_volets_109_test))
     suite.addTest(unittest.makeSuite(Explorer_modules_110_test))
     suite.addTest(unittest.makeSuite(Objectif_111_test))
     suite.addTest(unittest.makeSuite(Proposition_objectifs_112_test))
     suite.addTest(unittest.makeSuite(Fin_planification1_113_test))
     suite.addTest(unittest.makeSuite(Fin_planification2_114_test))
     suite.addTest(unittest.makeSuite(Fin_planification1_115_test))
     suite.addTest(unittest.makeSuite(Idle_116_test))
     unittest.TextTestRunner(verbosity=2).run(suite) 

#Class MesoPointTestSuite consists of all Test Cases related to MesoPoint 
class MesoPointTestSuite:
 #Initialize MesoPointTestSuite Class    
 def __init__(self):
     suite = unittest.TestSuite()
     suite.addTest(unittest.makeSuite(Contextualisation1_201_test))
     suite.addTest(unittest.makeSuite(Plaisir_202_test))
     suite.addTest(unittest.makeSuite(Barrieres_difficulte1_203_test))     
     suite.addTest(unittest.makeSuite(Intention_204_test))
     suite.addTest(unittest.makeSuite(End_205_test))
     suite.addTest(unittest.makeSuite(Idle_206_test))
     unittest.TextTestRunner(verbosity=2).run(suite) 
            	
#Run All Tests            	
if __name__ == '__main__':
    PlanningTestSuite()
    MesoPointTestSuite()
 
