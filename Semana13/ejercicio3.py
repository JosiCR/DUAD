from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year


        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        return years
    

def only_adults(func):
    def wrapper(*args, **kwargs):

        for arg in args:
            if isinstance(arg, User):
                if arg.age < 18:
                    raise Exception("user is not an adult")
                
        for value in kwargs.values():
            if isinstance(value, User):
                if value.age < 18:
                    raise Exception("user si not an adult")
                
        return func(*args, **kwargs)
    return wrapper

@only_adults
def register_user(user):
    print(f"user of age {user.age} registered successfully")


adult = User(date(2000, 1, 1))
minor = User(date(2010, 1, 1))

register_user(adult)
register_user(minor)