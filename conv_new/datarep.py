# import happybase
import sqlite3
import MySQLdb

class DB:
    conn = None

    def connect(self):
        self.conn = MySQLdb.connect(user='root', passwd='3231862', db='flask',
                                    host='localhost',
                                    charset="utf8",
                                    use_unicode=True, )

    def execute(self, *arg):
        try:
            cursor = self.conn.cursor()
            cursor.execute(*arg)
            self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
            print "reconnect"
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(*arg)
        return cursor

    def close(self):
        self.conn.close()


# Singleton Class Manages HBase Connection and HBase Query
class DataRepository(object):
    # Intialize HBase connection
    def __init__(self, db_add="session.db",check_same_thread=False):
        # self.db_add = db_add
        # self.conn = sqlite3.connect(db_add)
        # self.conn.row_factory = sqlite3.Row
        # self.conn = self.conn.cursor()
        self.conn = DB()

    # New Method to make Data Repositiory Class as Singleton
    # def __new__(type):
    #     if not '_the_instance' in type.__dict__:
    #         type._the_instance = object.__new__(type)
    #     return type._the_instance

    # Return conversation table Instance
    def get_conv_log_table(self):
        self.conv_table = self.con.table('user_conv_log')
        return self.conv_table

    # Return state table Instance
    def get_state_table(self):
        self.state_table = self.con.table('state_table')
        return self.state_table

    # Return context table Instance
    def get_context_table(self):
        self.context_table = self.con.table('context_table')
        return self.context_table

    # Return Planning conversation QA table Instance
    def get_plan_conv_qa(self):
        self.con_qa_table = self.con.table('conv_qa')
        return self.con_qa_table

    # Return conversation table Instance
    def get_context(self, uid):
        try:
            # context_table= self.get_context_table()
            #row = self.conn.execute("SELECT * FROM %s WHERE uid=%s", ("context_table", uid)).fetchone()

            sql="SELECT * FROM %s WHERE uid=%s"%("context_table", uid)
            row=self.conn.execute(sql).fetchone()
            print "context_row=",row
        except Exception as e:
            print e
            print "Error:Cannot Get Context"
        if row is not None: # cid exisits
            out = row[1]
        else:
            out = ""
        return out

    # updates context in to context table
    def update_context(self, uid, cid):
        try:
            # context_table= self.get_context_table()
            print uid,cid
            sql="Insert INTO context_table (uid,cid) VALUES (%(a)s, %(b)s) on duplicate KEY update cid=%(b)s"
            self.conn.execute(sql, {'a': uid, 'b': cid})
            print "successful"
            # context_table.put(uid,{'cid':cid})
        except Exception as e:
            print e
            print "Error:Cannot Update ContextState"

    # Get Current state
    def get_current_state_id(self, uid):
        try:
            # state_table = self.get_state_table()
            #row = self.conn.execute("SELECT * FROM %s WHERE uid=%s", ("state_table", uid)).fetchone()
            sql="SELECT * FROM %s WHERE uid=%s"%("state_table", uid)
            row=self.conn.execute(sql).fetchone()
        except Exception as e:
            print e
            print "Error:Cannot Get State"
        if row is not None:
            out = row[1]
        else:
            out = ""
        return out

    # Get Previous state
    def get_prev_state_id(self, uid):
        try:
            # state_table = self.get_state_table()
            # row = state_table.row(uid)
            #row = self.conn.execute("SELECT * FROM %s WHERE uid= %s", ("state_table", uid)).fetchone()

            sql="SELECT * FROM %s WHERE uid=%s"%("state_table", uid)
            row=self.conn.execute(sql).fetchone()
            pass
        except Exception as e:
            print e
            print "Error:Cannot Get State"
        if row is not None:
            out = row[2]
        else:
            out = ""
        return out

    # Update State Table
    def update_state_table(self, uid, cur, prev):
        try:
            # state_table = self.get_state_table()
            # state_table.put(uid, {'cur': cur, 'prev': prev})

            sql="Insert INTO state_table (uid,cur,prev) VALUES (%(a)s, %(b)s,%(c)s) on duplicate KEY update cur=%(b)s,prev=%(c)s"
            self.conn.execute(sql, {'a': uid, 'b': cur,'c':prev})

        except Exception as e:
            print e
            print "Error:Cannot Update State"

    # Post Conversation Data
    def post_conv_data(self, uid,qid,choice):
        try:
            # conv_table = self.get_conv_log_table()
            # conv_table.put(key, {'cid': qid, 'ch': choice})
            # key = uid+qid+timestamp

            sql="Insert INTO user_conv_log (uid,qid,choice) VALUES (%(a)s,%(b)s,%(c)s) on duplicate KEY update qid=%(b)s,choice=%(c)s"
            self.conn.execute(sql, {'a': uid, 'b': qid,'c':choice})
            print "conversation data inserted"
        except Exception as e:
            print e
            print "Error Cannot Post Data"

    # Get Conversation Data
    def get_conv_data(self, qid):
        try:
            # plan_conv_qa = self.get_plan_conv_qa()
            # row = plan_conv_qa.row(qid)
            sql="SELECT * FROM %(a)s WHERE qid=%(b)s"%{'a':"conv_qa",'b':qid}
            print sql
            row=self.conn.execute(sql).fetchone()
            row1={"qid":row[0],"ttext":row[1],"choices":row[2],"context":row[3],"ctype":row[4],"theme":row[5],"ques":row[6]}
            print row1

        except Exception as e:
            print e
            print "Error: Cannot Get Planning Conversation QA"
        return row1

    # Search Conversation Log
    def search_conv_log(self, uid, qid):
        try:
            # conv_log_table = self.get_conv_log_table()
            # rowkey = str(uid) + ":" + str(sid)
            # for key, data in conv_log_table.scan(row_prefix=rowkey):
            sql="SELECT * FROM %(a)s WHERE uid=%(b)s and qid=%(c)s"%{'a':"user_conv_log",'b':uid,'c':qid}
            print sql
            row=self.conn.execute(sql).fetchone()
            print "coversation log row =",row
            if row is not None:
                out = ''
                out = row[2]
            else:
                out = ""
        except Exception as e:
            print e
            print "Cannot Search Conversation Log"
        return out

# Singleton Class Manages HBase Connection and HBase Query
