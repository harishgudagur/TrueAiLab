const sessionId = localStorage.getItem("sessionId")
    || crypto.randomUUID()

localStorage.setItem(
    "sessionId",
    sessionId
)

async function sendMessage() {

    const input =
        document.getElementById(
            "message"
        )

    const message =
        input.value.trim()

    if (!message) return

    const chatBox =
        document.getElementById(
            "chat-box"
        )

    chatBox.innerHTML += `
        <div class="message user">
            ${message}
        </div>
    `

    input.value = ""

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        sessionId,
                        message
                    })
                }
            )

        const data =
            await response.json()

        chatBox.innerHTML += `
            <div class="message bot">
                ${data.reply}
            </div>
        `

        chatBox.scrollTop =
            chatBox.scrollHeight

    } catch (error) {

        chatBox.innerHTML += `
            <div class="message bot">
                Error connecting to server.
            </div>
        `
    }
}