## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

```python
# EXAMPLE
class my_friends:

    def __init__(self, birthdays):
        #parameters: friends birthdays as a dictionary
        
    def update_birthdays(self, name, birthday):
        #parameters: friends name and updated birthday
        #side effects: updating self.birthdays

    def update_name(self, name, new_name):
        #parameters: the old name and adding the new name
        #side effects: replacing the old name with the new name

    def upcoming_birthdays(self):
        #parameters: dates from dictionary and from datetime.today()
        #side effects: this will give us list of upcoming birthdays
        #return: which birthdays are upcoming

    def age_appropriate(self):
        #side effects: this will tell us the ages for the upcoming birthdays
        #return: tells us to buy age appropriate card for each person
    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
