const chatBox = document.getElementById("chat-box");
const input = document.getElementById("question");

function addMessage(role, text) {
    const div = document.createElement("div");
    div.className = role === "user" ? "text-right mb-2" : "text-left mb-2";
    div.innerHTML = `<div class="inline-block bg-${role === "user" ? "blue" : "gray"}-200 p-2 rounded-lg">${text}</div>`;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    saveToHistory(role, text);
}

function sendMessage() {
    const question = input.value.trim();
    if (!question) return;

    addMessage("user", question);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("bot", data.answer);
    });
}

// LocalStorage Chat History
function saveToHistory(role, text) {
    const history = JSON.parse(localStorage.getItem("chat") || "[]");
    history.push({ role, text });
    localStorage.setItem("chat", JSON.stringify(history));
}

function loadHistory() {
    const history = JSON.parse(localStorage.getItem("chat") || "[]");
    for (const msg of history) {
        addMessage(msg.role, msg.text);
    }
}

// Load previous chats on page load
window.onload = loadHistory;
