from brain import Brain


class UserSession:
    def __init__(self, uid, location: str = "50,5"):
        self.uid = str(uid)
        self.brain = Brain(location=location)

    def reply(self, to: str, location_update=None):
        if location_update is not None and location_update is str:
            self.brain.location = location_update
        return self.brain.give_answer(to)


if __name__ == '__main__':
    test_session = UserSession(0)
    print(test_session.reply("происходит"))
