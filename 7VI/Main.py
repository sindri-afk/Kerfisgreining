## Halda áfram með 6VI en láta unittestin virka
from User import User
from StudyBuddyConnect import StudyBuddyConnect
import unittest

# user = User("Sindri")
admin = StudyBuddyConnect()

class TestLogin(unittest.TestCase):
    def __init__(self, name=None):
        self.name = name
    def student_email(self):
        user = User()
        student_emils = [user.email()]
        self.assertTrue("@ru.is" in student_emils)

class TestNotifications(unittest.TestCase):
    def __init__(self):
        notifications_recieved = []

    
    def messaging_notification(self):
        Sender = User()

class TestMessages(unittest.TestCase):
    def __init__(self):
        pass



if __name__ == "__main__":
    unittest.main()
"""
__path__ attribute not found 
"""


