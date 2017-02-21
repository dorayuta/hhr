### handhistory db access class
import sqlite3
from constants import *

class handhistoryDb:
    def __init__(self):
        self.conn = None
        # check for table
        self.connectTable()

    def connectTable(self):
        self.conn = sqlite3.connect(HANDHISTORY_DB)
        
    def createTable(self):
        # only call once!
        self.conn = sqlite3.connect(HANDHISTORY_DB)
        try:
            conn.execute('''CREATE TABLE hands
                 (date text, trans text, symbol text, qty real, price real)''')
        except:
            print "Hand history table already exists!"

    def readHandHistoryFile():
        pass

    
    
