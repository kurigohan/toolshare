from django.contrib.auth.models import User
from django.test import TestCase
from users.models import UserProfile
from sharecenter.models import Shed, Tool
from django.core.urlresolvers import reverse




class ToolModelTest(TestCase):
    user1 = User(username="tester1")
    profile1 = UserProfile(postal_code=14564, user=user1)
    user2 = User(username="tester2")
    profile2 = UserProfile(postal_code=14564, user=user2)
    user3 = User(username="tester3")
    profile3 = UserProfile(postal_code=14564, user=user3)

    def test_is_available_with_borrower(self):
        """
        Tool.is_available() should return false if it has a borrower.
        """
        tool = Tool(name="test", owner=self.profile1, borrower=self.profile2)
        self.assertEqual(tool.is_available(), False)

    def test_is_available_without_borrower(self):
        """
        Tool.is_available() should return true if it has no borrower.
        """
        tool = Tool(name="test", owner=self.profile1, borrower=None)
        self.assertEqual(tool.is_available(), True)

    def test_tool_borrow_with_existing_borrower(self):
        """
        borrow_tool should return false if the tool is already has a borrower
        """
        tool = Tool(name="test", owner=self.profile1, borrower=self.profile2)
        self.assertEqual(tool.borrow_tool(self.profile3), False)

    def test_tool_borrow_with_no_existing_borrower(self):
        """
        borrow_tool should return false if the tool is already has a borrower
        """
        tool = Tool(name="test", owner=self.profile1, borrower=None)
        self.assertEqual(tool.borrow_tool(self.profile2), True)



        
#class ToolViewTest(TestCase):

    #def test_tool_detail_with_id():



#class ShedViewTest(TestCase):
