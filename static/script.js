document.getElementById('send-button').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent form submission

    const input = document.getElementById('chat-input');
    const message = input.value;

    if (message.trim() !== '') {
        const chatBox = document.getElementById('chat-box');

        // Get current time for message timestamp
        const date = new Date();
        const hour = date.getHours();
        const minute = date.getMinutes();
        const strTime = hour + ":" + (minute < 10 ? "0" + minute : minute);

        // User message with image
        const userMessage = `
            <div class="d-flex justify-content-end mb-4">
                <div class="msg_cotainer_send" style="background: none;color:white;">${message}&emsp;<br><span class="msg_time_send">${strTime}</span></div>
                <div class="img_cont_msg">
                    <img src="../static/user_2.png" class="rounded-circle user_img_msg">
                </div>
            </div>
        `;

        chatBox.appendChild(document.createRange().createContextualFragment(userMessage));
        input.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;

        // AJAX request to get the bot response
        $.ajax({
            data: {
                msg: message,
            },
            type: "POST",
            url: "/get",
        }).done(function(data) {
            const botMessage = `
                <div class="d-flex justify-content-start mb-4">
                    <div class="img_cont_msg">
                        <img src="../static/bot_2.png" class="rounded-circle user_img">
                    </div>
                    <div class="msg_cotainer" style="background: none;color:white;">&emsp;${data}<br><span class="msg_time">&emsp;${strTime}</span></div>
                </div>
            `;

            chatBox.appendChild(document.createRange().createContextualFragment(botMessage));
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }
});

function showChat() {
    const chatContainer = document.getElementById('chat-container');
    const startButton = document.querySelector('.cta-button'); 
    const welcomeMessage = document.querySelector('.welcome-container'); 

    // Show the chat container
    chatContainer.style.display = 'flex';

    // Hide the welcome message container
    welcomeMessage.style.display = 'none';
}
