import unittest
# Creating unit tests.

# 1 Choose four distinct user stories.
## 1) As a user, I need to have the app send me a push notification not only when someone has sent me a message but also to keep me on track with my study schedule. 
## 2) As a user I want the app to be exclusive to Uni students
## 3) As a user I need to be able to send messages to other users
## 4) “As a Student, I want the app to recommend potential study partners or groups based on my university program and study preferences, so that I can quickly find study partners without extensive searching.

class User():
    def __init__(self, name=str, id=int, email=str, major=str):
        self.name = name 
        self.id = id
        self.email = email
        self.major = major 
    

class University():
    def __init__(self):
        pass 

    
## Task 1
class TestPushNotifications(unittest.TestCase):
    """
    This class takes in unittest.TestCase, it is designed to test the push notifications
    that the user receives.
    """

    def test_message_notif(self):
        """
        this method tests the systems ability to send the user push notification
        upon receiving a message, either from other users or even from the system Admin.
        >>> if message_received: 
                send.notif = True
            else:
                send.notif = False
        """

        valid_user = User(name="CR7", email="CR7@ru.is")
        invalid_user = User(name=None, email="CR7.is")
        """
        I created two users one who has the correct credentials and one who does not
        """
        
        valid_name = isinstance(valid_user.name, str) 
        valid_email = isinstance(valid_user.email, str) and "@" in valid_user.email and "ru.is" in valid_user.email

        invalid_email = isinstance(invalid_user.email, str) and "@" in invalid_user.email and "ru.is" in invalid_user.email
        invalid_name = isinstance(invalid_user.name, str)
        """
        Here I am outline-ing what is a valid name, which my only requirement is that the name is a string
        And what is a valid email, a valid university email must be a string have the "@" sign and contain the "ru.is" (it's a localized test just for HR students)
        """
        message_received = True
        send_notif = message_received and valid_name and valid_email
        """
        if the message is received, the name and email are valid then send notif is true 
        """
        self.assertTrue(send_notif, "Notification should be sent upon receiving a message")


        invalid_message_received = False
        send_notif_invalid = invalid_message_received and valid_name and valid_email
        self.assertFalse(send_notif_invalid)
        """
        Here I am just asserting False for the invalid user.
        """


## Task 2
class TestExclusivity(unittest.TestCase):
    """
    This class also takes in unittest.TestCase, it is designed to test the exclusivity the study buddy system provides.
    it has one function which specifically tests the access users have based on their credentials.
    """
    def test_access(self):
        """
        Test that the only ones who can access the system are the ones that the correct credentials
        """
        valid_user = User(name="CR7", id=2145332, email="CR7@ru.is")
        invalid_user = User(name="Sindri", id="not an integer", email="sindri@ru.is")

        """
        Here downbelow I am creating the valid and invalid access variables
        """
        valid_access = isinstance(valid_user.id, int) and isinstance(valid_user.name, str) and isinstance(valid_user.email, str) and "@" in valid_user.email and "ru.is" in valid_user.email if valid_user.name and valid_user.id and valid_user.email else False
        invalid_access = isinstance(invalid_user.id, int) and isinstance(invalid_user.name, str) and isinstance(invalid_user.email, str) and "@" in invalid_user.email and "ru.is" in invalid_user.email if invalid_user.name and invalid_user.id and invalid_user.email else False

        """
        Here I am outline-ing what is a valid name, which my only requirement is that the name is a string
        And what is a valid email, a valid university email must be a string have the "@" sign and contain the "ru.is" (it's a localized test just for HR students)
        Also the id that the users have must be an integer so that the accesss is indeed vlaid
        """
        self.assertTrue(valid_access)
        self.assertFalse(invalid_access)


class TestMessagingApplication(unittest.TestCase):

    def test_message_sending_and_receiving(self):
        """
        Here I am creating two users, the "sender" and the "receiver of the message"
        """
        sender = User(name="Sender", id=2145332, email="sender@example.com")
        receiver = User(name="Receiver", id=2223345, email="receiver@example.com")

        message_sent = False 

        valid_sender = isinstance(sender.id, int) and isinstance(sender.name, str) and isinstance(sender.email, str) and "@" in sender.email and "ru.is" in sender.email if sender.name and sender.id and sender.email else False
        valid_receiver = isinstance(receiver.id, int) and isinstance(receiver.name, str) and isinstance(receiver.email, str) and "@" in receiver.email and "ru.is" in receiver.email if receiver.name and receiver.id and receiver.email else False
        """
        Here I am just using the same basic authentification I used in the tets case before to check if the users
        have the right credentials
        """
        if valid_sender and valid_receiver:
            message_sent = True 
            self.assertTrue(message_sent)
        else: 
            self.assertFalse(message_sent)


class TestStudyBuddyMatchmaking(unittest.TestCase):


    def test_matchmaking(self):
        """
        Test if the app recommends potential study partners or groups based on major and study preferences.
        """
        student = User(name="Student", id=1, email="student@example.com", major="Computer Science")
        """
        this is my inital student who is looking for a study buddy
        """
        study_buddy_A = User(name="StudyBuddy A", id=256789, email="buddyA@ru.is", major="Math")
        study_buddy_B = User(name="StudyBuddy B", id=3987654, email="buddyB@ru.is", major="Business")
        study_buddy_C = User(name="StudyBuddy C", id=45748930, email="buddyC@ru.is", major="Computer Science")

        """
        three separate uses who could potentially be chosen as an ideal studybuddy for my student
        """
        
        recommended_partners = []
        for buddy in [study_buddy_A, study_buddy_B, study_buddy_C]:
            if buddy.major == student.major:
                recommended_partners.append(buddy.name)

        """
        the matchmaking process 😨
        """

        expected_partner = ["StudyBuddy C"]
        """vitum alveg að StudyBuddy C tekur kökuna því að ég bjó hann til þannig hann er expected partner"""
        self.assertEqual(recommended_partners, expected_partner)
    


if __name__ == "__main__":
    unittest.main()
