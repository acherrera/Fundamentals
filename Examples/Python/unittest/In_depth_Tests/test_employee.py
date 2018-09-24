"""
Testing the employee class
"""

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClasse(cls):
        # Runs as the very beginning
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        # Runs at the very end
        print('tearDownClass')

    # Needs to have this exact name
    def setUp(self):
        # Will run before every test
        self.emp_1 = Employee('Anthony', 'Herrera', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # Needs to have this exact name
    def tearDown(self):
        # Will run after every test - not used here
        # Could delete files that is created during the tests
        pass

    def test_email(self):
        # Testing Email
        self.assertEqual(self.emp_1.email, 'Anthony.Herrera@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        # Testing name change functionality
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Herrera@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')


    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Anthony Herrera')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Herrera')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """
        Test the call without the success being tied to the website being up
        Mocked object is a fake object. We can assign fake values to this fake
        object
        """

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Herrera/May')
            self.assertEqual(schedule, 'Success')


            # Testing with False and emp_2
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()
