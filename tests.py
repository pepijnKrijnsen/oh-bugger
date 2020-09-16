import unittest
import datetime
import main
import random

class tests(unittest.TestCase):

    def testNewTicket(self):
        td = {
                "title": "New bofr",
                "body": "This bug is still munching away",
                }
        main.core.storeNewTicket(td)

if __name__ == "__main__":
    unittest.main()
