###################
#### STRUCTURE ####
# 
# Haughty core:
#   business logic
# 
# Presenter:
#   Prepares data for output by the view
# 
# STORY I: user writes & saves new ticket
# 1. User types entries into Title, Body, and Affected System fields - then hits Save
# 2. Presenter retrieves the data, validates it - then sends to Core
# 3. Core logic stores data in Database
# 4. Core sends a new dictionary to the Presenter
# 5. Presenter builds a new page - then sends to View


#################
#### IMPORTS ####
import datetime
import random
import time


######################
#### HAUGHTY CORE ####
class core:

    def storeNewTicket(ticket_data):
        ID = core.generateNewID()
        ticket_data["ID"] = ID
        now = datetime.datetime.now()
        ticket_data["created_on"] = now.strftime("%Y%m%d")
        ticket_data["created_at"] = now.strftime("%H:%M")
        ticket_data["birth_second"] = int(time.time())
        ticket_data["last_modified"] = int(time.time())
        f = open("lib/db/" + ID, "w")
        ticket = str(ticket_data)
        f.write(ticket)
        f.close()
        

    def generateNewID():
        f = open("lib/UIDs.csv", "r+")
        UIDs = f.read()
        UID = str(random.randrange(20000, 29999, 1))
        while UID in UIDs:
            UID = str(random.randrange(20000, 29999, 1))
        f.write(UID + ",")
        f.close()
        return UID



###################
#### PRESENTER ####
class presenter:

    def newTicket(data):
        core.storeNewTicket(data)
