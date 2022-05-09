import unittest
from app.models import Comment, User, Pitch
from app import db

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the class
    '''

    def setUp(self):
      self.user_example = User(username = 'Example', password = 'passcode', email = 'passcode@yahoo.com')
      self.new_pitch = Pitch(category = 'Business',title='My Business ',pitch='It sis intresting to run a business..', user= self.user_example)
      self.new_comment = Comment(comment='Nice pitch ',pitch=self.new_pitch,user= self.user_example)
      
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Nice pitch')
        self.assertEquals(self.new_comment.user,self.user_example)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)