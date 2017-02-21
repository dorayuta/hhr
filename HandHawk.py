import handhistoryDb
from constants import *
'''
Client object.
'''
class client:
    def __init__(self):
        self.name = "name"
        self.hhDb = handhistoryDb.handhistoryDb()

    def run(self):
        print self.hhDb


    

