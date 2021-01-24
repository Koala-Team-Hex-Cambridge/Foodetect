import re
from emailScanner import FileLocation

# will change this to store user information as part of profile
# account credentials
class UserProfile:
    def __init__(self, givenPassword, givenEmail):
        self.password = givenPassword
        self.emailAddress = givenEmail
        provider = re.split("[@  .]", givenEmail)
        self.emailProvider = provider[1]

    def get_provider():
        return self.emailProvider

    def get_password():
        return self.password


userTest = UserProfile("testName", "testName@gmail.com")

FileLocation(
    getattr(userTest, "emailAddress"),
    getattr(userTest, "emailProvider"),
    getattr(userTest, "password"),
)
