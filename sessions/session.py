from brain import Brain


class UserSession:
    def __init__(self, uid, location: str = "50,5"):
        self.uid = str(uid)
        self.brain = Brain(location=location)

    def reply(self, to: str, locationUpdate=None):
        if locationUpdate is not None and type(locationUpdate) == "str":
            self.brain.location = locationUpdate
        return { "answer": self.brain.give_answer(to),
                 "sleep":  self.brain.wanna_sleep }


if __name__ == '__main__':
    test_session = UserSession(0)
    print(test_session.reply("происходит"))