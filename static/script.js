const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const chatMessages = document.getElementById("chatMessages");

const sessionId =
    "session-" + Date.now() + "-" + Math.random().toString(36).substring(2, 9);


function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message";
    } else {
        messageDiv.className = "bot-message";
    }

    const paragraph = document.createElement("p");
    paragraph.textContent = message;

    messageDiv.appendChild(paragraph);
    chatMessages.appendChild(messageDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


async function sendMessage(customMessage = null) {
    const message = customMessage || messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");
    messageInput.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        const data = await response.json();

        addMessage(data.response, "bot");

    } catch (error) {
        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );
        console.error(error);
    }
}


sendButton.addEventListener("click", function () {
    sendMessage();
});


messageInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});


document.querySelectorAll(".service-buttons button").forEach(function (button) {
    button.addEventListener("click", function () {
        sendMessage(button.textContent);
    });
});