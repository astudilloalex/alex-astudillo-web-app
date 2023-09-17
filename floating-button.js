// Create chat button.
const chatContainer = document.createElement("div");
chatContainer.id = "alex-astudillo-chat-container";
chatContainer.style.display = "none"; // When open page display none.
chatContainer.style.position = "fixed";
chatContainer.style.bottom = "20px";
chatContainer.style.right = "20px";
chatContainer.style.backgroundColor = "#ffffff";
chatContainer.style.border = "1px solid #ccc";
chatContainer.style.width = "300px";
chatContainer.style.height = "400px";
chatContainer.style.zIndex = "10000";

const chatContent = document.createElement("div");
chatContent.innerHTML = `
<h2>Chat en vivo</h2><p>Bienvenido al chat en vivo...</p>
<div id="chat-messages" style="height: 300px; overflow-y: scroll;"></div>
<input type="text" id="message-input" placeholder="Escribe tu mensaje..." style="width: 80%; padding: 5px;">
<button id="send-button" style="width: 18%;">Enviar</button>
`;

// Add event to send messages
const chatMessages = chatContent.querySelector('#chat-messages');
const messageInput = chatContent.querySelector('#message-input');
const sendButton = chatContent.querySelector('#send-button');

const apiUrl = 'https://yourapi.com/send';
sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message) {
        const messageElement = document.createElement('p');
        messageElement.textContent = `Cliente: ${message}`;
        chatMessages.appendChild(messageElement);

        // Send message to REST API
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            // Show response to the customer.
            const responseElement = document.createElement('p');
            responseElement.textContent = `Servidor: ${data.response}`;
            chatMessages.appendChild(responseElement);
        })
        .catch(error => {
            console.error('Error al enviar/recibir el mensaje:', error);
        });

        messageInput.value = '';
    }
});

chatContainer.appendChild(chatContent);

// Add close button to the chat.
const closeButton = document.createElement("button");
closeButton.textContent = "Cerrar";
closeButton.addEventListener("click", () => {
  chatContainer.style.display = "none";
});

chatContainer.appendChild(closeButton);

// Add open button to the chat.
const chatButton = document.createElement("button");
chatButton.textContent = "Abrir Chat";
chatButton.style.position = "fixed";
chatButton.style.bottom = "20px";
chatButton.style.right = "20px";
chatButton.style.backgroundColor = "blue";
chatButton.style.color = "white";
chatButton.style.padding = "10px 20px";
chatButton.style.borderRadius = "5px";
chatButton.style.zIndex = "9999";

chatButton.addEventListener("click", () => {
  chatContainer.style.display = "block";
});

// Validate token
// Use backend for this validation
const expectedToken = 'your-token-here';
// Validate allowed hosts.
const allowedDomains = ["127.0.0.1"];
// Get the current domain.
const currentDomain = window.location.hostname;
console.log(currentDomain);
if (allowedDomains.includes(currentDomain)) {
  // Add the floating button to the body
  document.body.appendChild(chatButton);
  document.body.appendChild(chatContainer);
} else {
  console.error("domain-not-allowed");
}
