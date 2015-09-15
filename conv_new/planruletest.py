from datarep import DataRepository
from condata import ConversationData
from mock import mockdb
from factory import *
import unittest
import datetime

# Intialize MockDB Class for test
mockobj = mockdb()


# Planning Rule Test Super Class
class PlanningRuleTest(unittest.TestCase):
    def setUp(self):
        print("Setting up environment for Plannification test cases")

    def tearDown(self):
        print("Cleaning up environment for Plannification test cases")


# Planning Rules Test
class Contextualisation_101_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."
        self.time = datetime.datetime.utcnow()
        data = [['1', '101', '1', self.time]]
        mockobj.write_data_csv(data)

    def tearDown(self):
        print("Cleaning up...")
        mockobj.empty_file()

    def runTest(self):
        self.assertEqual(Contextualisation_101().getNextState('1', '1', True).stateid, '102', 'Incorrect State')
        mockobj.empty_file()
        data = [['1', '101', '2', self.time]]
        mockobj.write_data_csv(data)
        self.assertEqual(Contextualisation_101().getNextState('1', '1', True).stateid, '115', 'Incorrect State')


class Proposition_objectifs_102_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."
        self.time = datetime.datetime.utcnow()
        data = [['1', '102', '3', self.time]]
        mockobj.write_data_csv(data)

    def tearDown(self):
        print("Cleaning up...")
        mockobj.empty_file()

    def runTest(self):
        self.assertEqual(Proposition_objectifs_102().getNextState('1', '1', True).stateid, '103', 'Incorrect State')
        mockobj.empty_file()
        data = [['1', '102', '2', self.time]]
        mockobj.write_data_csv(data)
        self.assertEqual(Proposition_objectifs_102().getNextState('1', '1', True).stateid, '104', 'Incorrect State ')


class Proposition_objectifs_103_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Proposition_objectifs_103().getNextState('1', '1').stateid, '104', 'Incorrect State')


class Explorer_volets_104_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Explorer_volets_104().getNextState('1', '1').stateid, '105', 'Incorrect State')


class Explorer_modules_105_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."
        self.time = datetime.datetime.utcnow()
        data = [['1', '101', '1', self.time]]
        mockobj.write_data_csv(data)

    def tearDown(self):
        print("Cleaning up...")
        mockobj.empty_file()

    def runTest(self):
        self.assertEqual(Explorer_modules_105().getNextState('1', '1', True).stateid, '106', 'Incorrect State')
        mockobj.empty_file()
        data = [['1', '101', '2', self.time]]
        mockobj.write_data_csv(data)
        self.assertEqual(Explorer_modules_105().getNextState('1', '2', True).stateid, '107', 'Incorrect State')


class Objectif_106_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Objectif_106().getNextState('1', '1').stateid, '108', 'Incorrect State')


class Proposition_objectifs_107_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Proposition_objectifs_107().getNextState('1', '1').stateid, '108', 'Incorrect State')


class Debuter_semaine_108_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."
        self.time = datetime.datetime.utcnow()
        data = [['1', '101', '4', self.time]]
        mockobj.write_data_csv(data)

    def tearDown(self):
        print("Cleaning up...")
        mockobj.empty_file()

    def runTest(self):
        self.assertEqual(Debuter_semaine_108().getNextState('1', '4', True).stateid, '109', 'Incorrect State')
        mockobj.empty_file()
        data = [['1', '101', '5', self.time]]
        mockobj.write_data_csv(data)
        self.assertEqual(Debuter_semaine_108().getNextState('1', '5', True).stateid, '114', 'Incorrect State')


class Explorer_volets_109_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Explorer_volets_109().getNextState('1', '1').stateid, '110', 'Incorrect State')


class Explorer_modules_110_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."
        self.time = datetime.datetime.utcnow()
        data = [['1', '101', '1', self.time]]
        mockobj.write_data_csv(data)

    def tearDown(self):
        print("Cleaning up...")
        mockobj.empty_file()

    def runTest(self):
        self.assertEqual(Explorer_modules_110().getNextState('1', '4', True).stateid, '111', 'Incorrect State')
        mockobj.empty_file()
        data = [['1', '101', '5', self.time]]
        mockobj.write_data_csv(data)
        self.assertEqual(Explorer_modules_110().getNextState('1', '5', True).stateid, '112', 'Incorrect State')


class Objectif_111_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Objectif_111().getNextState('1', '1').stateid, '113', 'Incorrect State')


class Proposition_objectifs_112_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Proposition_objectifs_112().getNextState('1', '1').stateid, '113', 'Incorrect State')


class Fin_planification1_113_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Fin_planification1_113().getNextState('1', '1').stateid, '114', 'Incorrect State')


class Fin_planification2_114_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Fin_planification2_114().getNextState('1', '1').stateid, '116', 'Incorrect State')


class Fin_planification1_115_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Fin_planification1_115().getNextState('1', '1').stateid, '116', 'Incorrect State')


class Idle_116_test(PlanningRuleTest):
    def setUp(self):
        print "Starting test case Execution..."

    def tearDown(self):
        print("Cleaning up...")

    def runTest(self):
        self.assertEqual(Idle_116().getNextState('1', '1').stateid, '116', 'Incorrect State')
