from datetime import datetime

class my_friends:
    def __init__(self, birthdict):
        self.birthdays = birthdict

    def update_birthdays(self, name, newBirthday):
        self.birthdays.update({name : newBirthday})



    def upcoming_birthdays(self):
        today = datetime.now()
        thisMonth = today.month
        upcomingBirthdays = "Upcoming birthdays: "

        for entry in self.birthdays:
            targetDate = datetime.strptime(self.birthdays[entry], "%Y-%m-%d")
            if (targetDate.month - thisMonth <= 4 and targetDate.month - thisMonth >= 0):
                upcomingBirthdays += f"{entry} "
        upcomingBirthdays = upcomingBirthdays.strip()
        return upcomingBirthdays
    
    def age_appropriate(self):
        today = datetime.now() #2024-10-09
        thisMonth = today.month #10
        thisYear = today.year #2024
        upcomingBirthdays = [] #["David", "Michael"]
        ages = "These people will turn: "



        for entry in self.birthdays:
            targetDate = datetime.strptime(self.birthdays[entry], "%Y-%m-%d")
            if (targetDate.month - thisMonth <= 4 and targetDate.month - thisMonth >= 0):
                upcomingBirthdays.append(entry)
        

        for name in upcomingBirthdays:
            for entry in self.birthdays:
                if name == entry:
                    targetyear = datetime.strptime(self.birthdays[entry], "%Y-%m-%d")
                    person_age = thisYear - targetyear.year 
                    ages += f"{name}: {person_age} "
        
        return ages.strip()
                

#cycle throught the self.birthday and find Michael and David date of birth and subtract the year of birth from todays year 2024
# "Harry": "1998-07-05", "Alice": "1997-03-02", "David": "1994-11-02", "Lucy": "1982-07-05", "Michael": "2001-12-05"

        
    
    
    