const chatInput = document.querySelector('#chat-input');
const sendBtn = document.querySelector('#send-btn');
const micBtn = document.querySelector('#mic-btn');
const chatContainer = document.querySelector('.chat-container');

let userTxt = null;

let chatNum = 0;

const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

const createElement = (html, className) => {
    const chatDiv = document.createElement("div");
    chatDiv.classList.add("chat", className);
    chatDiv.innerHTML = html;
    return chatDiv;
};

const getchatResponse = async (incomingChatDiv) => {    
    chatNum += 1;
    const pElement = document.createElement("p");

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
                number: chatNum
            })
    }

    try {
        const response = await (await fetch("http://127.0.0.1:5000/chat-response", requestOptions)).json();
        pElement.textContent = response.response;
    } catch (err) {
        console.log(err)
        pElement.textContent = "Desculpa, mas eu não entendi sua pergunta, poderia repetir de novo, por favor?";
    }
    
    await sleep(1000)
    incomingChatDiv.querySelector(".typing-animation").remove();
    incomingChatDiv.querySelector(".chat-details").appendChild(pElement);
}

const showTypingAnimation = () => {
    const html = `
        <div class="chat-content">
            <div class="chat-details">
                <img src="UI/images/chatbot.jpg" alt="user-img">
                <div class="typing-animation">
                    <div class="typing-dot" style="--delay: 0.2s"></div>
                    <div class="typing-dot" style="--delay: 0.3s"></div>
                    <div class="typing-dot" style="--delay: 0.4s"></div>
                </div>
            </div>
            <span class="material-symbols-outlined">content_copy</span>
        </div>`;

    const incomingChatDiv = createElement(html, "incoming");
    chatContainer.appendChild(incomingChatDiv);
    getchatResponse(incomingChatDiv);
};

const handleOutgoingChat = () => {
    userTxt = chatInput.value.trim();
    if (userTxt == "") {
        return;
    }
    const html = `
                <div class="chat-content">
                    <div class="chat-details">
                        <img src="UI/images/user.jpg" alt="user-img">
                        <p>${userTxt}</p>
                    </div>
                </div>`;
    const outgoingChatDiv = createElement(html, "outgoing");
    chatContainer.appendChild(outgoingChatDiv);
    chatInput.value = "";
    setTimeout(showTypingAnimation, 500);
};

const handleVoiceInput = async() => {
    try {
        const response = await (await fetch("http://127.0.0.1:5000/input")).json();
        chatInput.value = response.input;
        await sleep(500);
        handleOutgoingChat();
    } catch (err) {
        console.log(err)
    }
}

sendBtn.addEventListener("click", handleOutgoingChat);
document.addEventListener("keydown", (event) => {
    if (event.key == "Enter") {
        handleOutgoingChat();
    }
});

micBtn.addEventListener("click", handleVoiceInput);