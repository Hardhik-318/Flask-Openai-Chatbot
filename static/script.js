document.addEventListener("DOMContentLoaded", () => {
  const inputField = document.querySelector(".text-area input");
  const sendBtn = document.querySelector(".send-btn");
  const chatArea = document.querySelector(".chat-area");
  let selectedMode = "ask";
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      selectedMode = this.getAttribute('data-mode');
    });
  });

  function getSelectedMode() {
    return selectedMode;
  }

  sendBtn.addEventListener("click", sendMessage);

  inputField.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  async function sendMessage() {
    const message = inputField.value.trim();
    const mode = getSelectedMode();

    if (!message) return;

    appendMessage("user", message);
    inputField.value = "";

    const loading = appendMessage("bot", "Typing...");

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, mode })
      });

      const data = await res.json();
      chatArea.removeChild(loading);
      appendMessage("bot", data.reply);
    } catch (err) {
      chatArea.removeChild(loading);
      appendMessage("bot", "Error: Could not get a response.");
    }
  }

  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;
    chatArea.appendChild(msg);
    chatArea.scrollTop = chatArea.scrollHeight;
    return msg;
  }
});
