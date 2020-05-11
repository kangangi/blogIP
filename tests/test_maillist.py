import unittest
from app import db
from app.models import MailList

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.new_mail= MailList(email = "diana@gmail.com")
        db.session.add(new_mail)
        db.session.commit()

    def tearDown(self):
        MailList.query.delete()
    
    def test_is_instance(self):
       self.assertTrue(isinstance(self.new_mail, MailList))

    def test_save_mail(self):
        self.new_comment.save_mail()
        self.assertTrue(len(MailList.query.all())>0)


