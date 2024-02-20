from knowledge.request_context import RequestContext
from .session import UserSession

sessions = {}
sessionIDs = set()


def __create_session_id__(offset=0):
    global sessionIDs

    sid = str(len(sessionIDs) + offset)
    if sid in sessionIDs:
        return __create_session_id__(offset + 1)
    else:
        sessionIDs.add(sid)
        return str(sid)


def session_exists(sessionID):
    global sessionIDs
    sessionID = str(sessionID)
    return sessionID in sessionIDs


def get_session(sid):
    sid = str(sid)
    assert session_exists(sid)
    return sessions[sid]


def create_session(location="50,50", session_id=None):

    if session_id is None:
        session_id = __create_session_id__()

    session_id = str(session_id)

    session = UserSession(session_id, location=location)
    sessionIDs.add(session_id)

    global sessions
    sessions[session_id] = session

    return session_id


def reply(sid, input_text) -> RequestContext:
    sid = str(sid)
    if not session_exists(sid):
       return None
    else:
       return get_session(sid).reply(input_text)


if __name__ == '__main__':
    s1 = create_session(session_id=123)
    s2 = create_session()

    print(sessionIDs)
    print(sessions)

    print(s1, reply(s1, "спой"))
    print(s2, reply(s2, "ещё"))
    print(s1, reply(s1, "ещё"))
    print(s1, reply(s2, "пока"))