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
    
    