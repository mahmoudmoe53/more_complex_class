from lib.complex_class import *

def test_my_friends_birthdays_is_init_instance():
    friends = my_friends({})
    result = friends.birthdays
    assert isinstance(result, dict)

def test_update_birthdays_changes_self_birthdays():
    friends = my_friends({"Harry": "1998-07-05", "Alice": "1970-03-02", "David": "1994-11-02", "Lucy": "1982-07-05", "Michael": "2001-12-05"})
    friends.update_birthdays("Alice", "1997-03-02")
    result = friends.birthdays
    assert result == {"Harry": "1998-07-05", "Alice": "1997-03-02", "David": "1994-11-02", "Lucy": "1982-07-05", "Michael": "2001-12-05"}

def test_upcoming_birthdays_return_correctly():
    friends = my_friends({"Harry": "1998-07-05", "Alice": "1997-03-02", "David": "1994-11-02", "Lucy": "1982-07-05", "Michael": "2001-12-05"})
    result = friends.upcoming_birthdays()
    assert result == "Upcoming birthdays: David Michael"