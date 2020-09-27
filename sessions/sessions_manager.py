from .session import UserSession

sessions = {}
sessionIDs = set()


def __createSessionID__(offset=0):
    global sessionIDs

    sid = str(len(sessionIDs) + offset)
    if sid in sessionIDs:
        return __createSessionID__(offset + 1)
    else:
        sessionIDs.add(sid)
        return str(sid)


def sessionExists(sessionID):
    global sessionIDs
    sessionID = str(sessionID)
    return sessionID in sessionIDs


def getSession(sid):
    sid = str(sid)
    if not sessionExists(sid):
        return None
    else:
        return sessions[sid]


def createSession(location="50,5", sessionID=None):

    if sessionID is None:
        sessionID = __createSessionID__()

    sessionID = str(sessionID)

    session = UserSession(sessionID, location=location)
    sessionIDs.add(sessionID)

    global sessions
    sessions[sessionID] = session

    return sessionID


def reply(sid, input_text):
    sid = str(sid)
    if not sessionExists(sid):
       return "idk"
    else:
       return getSession(sid).reply(input_text)


if __name__ == '__main__':
    s1 = createSession(sessionID=123)
    s2 = createSession()

    print(sessionIDs)
    print(sessions)

    print(s1, reply(s1, "спой"))
    print(s2, reply(s2, "ещё"))
    print(s1, reply(s1, "ещё"))
    print(s1, reply(s2, "пока"))