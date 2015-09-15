from datarep import DataRepository
from condata import ConversationData
from mock import mockdb
from factory import *
import unittest
import datetime

# Intialize MockDB Class for test
mockobj = mockdb()


# MesoPoint Rule Test Super Class
class MesoPointRuleTest(unittest.TestCase):
    def setUp(self):
        print("Setting up environment for Meso Point test cases")

    def tearDown(self):
        print("Cleaning up environment for Meso oint test cases")


# MesoPoint Rules Test
class Contextualisation1_201_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Contextualisation1_201().getNextState('1', '1').stateid, '202', 'Incorrect State')


class Plaisir_202_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Plaisir_202().getNextState('1', '1').stateid, '203', 'Incorrect State')


class Barrieres_difficulte1_203_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Barrieres_difficulte1_203().getNextState('1', '1').stateid, '204', 'Incorrect State')


class Intention_204_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Intention_204().getNextState('1', '1').stateid, '205', 'Incorrect State')


class End_205_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(End_205().getNextState('1', '1').stateid, '206', 'Incorrect State')


class Idle_206_test(MesoPointRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Idle_206().getNextState('1', '1').stateid, '206', 'Incorrect State')
