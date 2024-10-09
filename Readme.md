## 1. The Problem

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


## 2. Class Interface

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

## 3. Examples Tests


``` python
# EXAMPLE
def test_my_friends_birthdays_is_init_instance():
    #checks if self.birthdays is initialised

def test_update_birthdays_changes_self_birthdays():
    #runs update birthdays and checks if self.birthdays changes

def test_upcoming_birthdays_return_correctly():
    #runs upcoming_birthdays and checks the return

def test_age_appropriate_return_correctly():
    #runs age_appropriate and checks the return
```