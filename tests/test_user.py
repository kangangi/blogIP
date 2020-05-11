import unittest
from app import db
from app.models import User

class TestUser(unittest.TestCase):
    '''
    Class that tests the User class
    '''

    def setUp(self):
        self.new_user = User(username = "Diana",fullname = "Diana",email = "diana@gmail.com", bio= "A girl", profile_pic_url="imageurl", password ="diana")
        db.session.add(self.new_user)
        db.session.commit()

    def tearDown(self):
        User.query.delete()
        db.session.commit()

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username, 'Diana')
        self.assertEquals(self.new_user.fullname, 'Diana')
        self.assertEquals(self.new_user.email, 'diana@gmail.com')
        self.assertEquals(self.new_user.bio, 'A girl')
        self.assertEquals(self.new_user.profile_pic_url, 'imageurl')
        self.assertTrue(self.new_user.verify_password('diana'))

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password 