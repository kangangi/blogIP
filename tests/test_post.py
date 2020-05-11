import unittest
from app import db
from app.models import Post, User

class TestPost(unittest.TestCase):
    '''
    Class used to test the post
    '''

    def setUp(self):
        self.new_user = User(username = "Diana",fullname = "Diana",email = "diana@gmail.com", bio= "A girl", profile_pic_url="imageurl", password ="diana")
        self.new_post = Post(title = "Monday", description = "Tuesday")
        db.session.add(self.new_post)
        db.session.add(self.new_user)
        db.session.commeit()

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

