from proj.user_task import user_input
from nose.tools import raises


class TestUserTask:
    def test_user_input_without_weekday(self):
        assert user_input("CALL U1 India 13:00:00 14:30:00") == "13:00:00"

    def test_user_input_with_weekday(self):
        assert user_input("Email - U1 - India - 13:30:00 14:30:00 Tuesday and Thursday") == "Tuesday 13:30:00"

    @raises(ValueError)
    def test_user_input_incorrect_format(self):
        user_input("Incorrect String")
