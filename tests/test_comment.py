import unittest
from app.models import User, Post, Comment
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(content = 'content' )
        self.new_user = User(username = "Diana",fullname = "Diana",email = "diana@gmail.com", bio= "A girl", profile_pic_url="imageurl", password ="diana")
        self.new_post = Post(title = "Monday", description = "Tuesday")

        db.session.add(self.new_post)
        db.session.add(self.new_user)
        db.session.add(self.new_comment)
        db.session.commit()
        

    def tearDown(self):
        Comment.query.delete()
        Post.query.delete()
        User.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_get_comments(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(1)
        self.assertEqual(len(get_comments) == 1)
    
