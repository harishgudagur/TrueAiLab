sessions = {}


def add_message(session_id, role, message):

    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": role,
        "message": message
    })

    sessions[session_id] = sessions[session_id][-6:]


def get_history(session_id):

    return sessions.get(
        session_id,
        []
    )