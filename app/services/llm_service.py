def generate_response(
    context,
    history,
    question
):

    if not context.strip():
        return {
            "reply":
            "I could not find enough information in the knowledge base.",
            "tokens": 0
        }

    summary = context.split(".")[0]

    reply = f"""
Based on the knowledge base:

{summary}.
"""

    return {
        "reply": reply.strip(),
        "tokens": 0
    }