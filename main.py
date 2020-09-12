###################
#### STRUCTURE ####
# 
# Haughty core:
#   business logic
# 
# Entity: database:
#   stores and retrieves tickets
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
import json


######################
#### HAUGHTY CORE ####
class core:

    def storeNewTicket(ticket_data):
        ID = generateNewID()
        ticket_data["ID"] = ID
        f = open("lib/db/" + ID, "w")
        f.write(ticket_data)
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

    def newTicket(json_data):

