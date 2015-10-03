__author__ = 'Jian Mo'
import os
import client.client_main as client_main
import unittest
import client.post_client as cl
from scrapy.selector import Selector

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):

        # import web client from flask module

        self.app = client_main.app.test_client()
        self.uid="1"
        self.cid="1"
        self.app.post('/',data=dict(uid=self.uid,cid=self.cid))
        self.qid="101"

    def tearDown(self):
        pass

    #test client connections
    def test_connection(self):
        rv = self.app.get('/')
        #print rv.data
        assert 'Post questions' in rv.data


   # trying to recursively traverse all questions
    def test_questions(self):

        # if it's initial question,then post

        if self.qid=="101":
            rv=self.app.post('/main',buffered=True, content_type='multipart/form-data', data={"uid":self.uid,"qid":self.qid,"cid":self.cid,"Choices":"1"},follow_redirects=True)
            print "rv.data=",rv.data
            sel = Selector(rv)

            #read possible choices from web page

            self.choices = sel.xpath(
                '//select//option//@value').extract()
            self.qid=sel.xpath(
                '//label//input[@name="qid"]//@value').extract()
            print "qid==,",self.qid
            print "initial post"
            assert 'Question_ID' in rv.data

            self.test_questions()

        else:

            # otherwise looping the posting answer process

            # post every possible answer to server and test if feedback ok
            for count,choice in enumerate(self.choices,start=0):

                #recursion call
                self.test_questions()

                rv=self.app.post('/main', buffered=True, content_type='multipart/form-data', data={"uid":self.uid,"qid":self.qid[count],"cid":self.cid,"Choices":choice}, follow_redirects=True,)

                print "choices=",rv.data
                sel = Selector(rv)
                choices = sel.xpath(
                    '//select//option//@value').extract()
                qid=sel.xpath(
                    '//label//input[@name="qid"]//@value').extract()
                print "post 2"
                assert 'Question_ID' in rv.data

                # Termination condition
                if self.qid==qid:
                    pass
                else:
                    self.choices=choices
                    self.qid=qid
                    self.test_questions()

if __name__ == '__main__':
    unittest.main()
