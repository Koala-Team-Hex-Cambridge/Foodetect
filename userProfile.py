# will change this to store user information as part of profile
# account credentials
class userProfile:
    def __init__(self, givenPassword, givenUsername):
        self.password = givenPassword
        self.username = givenUsername
        provider = re.split("[@  .]", username)
        self.providerName = provider[1]
