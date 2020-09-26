from brain import Brain

class UserSession:
    def __init__(self, uid, location: str = "50,5"):
        self.uid = str(uid)
        self.brain = Brain(location=location)

    def reply(self, to: str, locationUpdate=None):
        if locationUpdate is not None and type(locationUpdate) == "str":
            self.brain.location = locationUpdate
        return self.brain.give_answer(to)

if __name__ == '__main__':
    test_session = UserSession(0)
    print(test_session.reply("происходит"))