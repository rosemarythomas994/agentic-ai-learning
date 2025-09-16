function sendMessage() {
  const input = document.getElementById('user-input');
  const msg = input.value;
  appendMessage('You', msg);
  input.value = '';

  fetch('http://localhost:5000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: msg })
  })
    .then(res => res.json())
    .then(data => appendMessage('Bot', data.response));
}

function appendMessage(sender, text) {
  const log = document.getElementById('chatlog');
  const msgDiv = document.createElement('div');
  msgDiv.textContent = `${sender}: ${text}`;
  log.appendChild(msgDiv);
}
