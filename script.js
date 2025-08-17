const form = document.getElementById("form");
const input = document.getElementById("input");
const chat = document.getElementById("chat");

form.addEventListener("submit", async e => {
  e.preventDefault();
  const msg = input.value.trim();
  if (!msg) return;
  append("You", msg);
  input.value = "";
  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    append("GenAI", data.reply);
  } catch {
    append("GenAI", "❌ Network error. Try again.");
  }
});

function append(sender, text) {
  const p = document.createElement("p");
  p.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chat.appendChild(p);
  chat.scrollTop = chat.scrollHeight;
}
