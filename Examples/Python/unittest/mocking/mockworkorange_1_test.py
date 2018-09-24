"""
Testing the mockworkorange function
"""

from unittest import TestCase, mock, main
from mockworkorange_1 import work_on


class TestWorkingMockingModule(TestCase):

    def test_using_context_manager(self):
        # This is essectially just building the wrapper by hand
        with mock.patch('mockworkorange_1.os') as mocked_os:
            work_on()
            mocked_os.getcwd.asser_called_once()


    # Use the built-in wrapper. Passed as 'mocked_os' automatically
    @mock.patch('mockworkorange_1.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.asser_called_once()

    def test_using_return_value(self):
        """ Don't need the 'as' keyword """
        with mock.patch('mockworkorange_1.os.getcwd', return_value='testing'):
            # Because os.getcwd should return testing now and that value is
            # returned by the function
            assert work_on() == 'testing'


if __name__ == '__main__':
    main()
