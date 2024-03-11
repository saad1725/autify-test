function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    // Display user message
    var userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerHTML = "<strong>You:</strong> " + userInput;
    chatBox.appendChild(userMessage);

    // Send user input to server for processing (AJAX request)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/generate_code/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Display server response
            var serverResponse = JSON.parse(xhr.responseText);
            var botMessage = document.createElement("div");
            botMessage.className = "bot-message";
            botMessage.innerHTML = "<strong>Response:</strong> " + serverResponse.generated_code;
            chatBox.appendChild(botMessage);

            // Scroll to bottom of chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    };
    var formData = "description=" + encodeURIComponent(userInput);
    xhr.send(formData);

    // Clear user input field
    document.getElementById("user-input").value = "";
}

function saveFeedback() {
    var feedbackInput = prompt("Please enter your feedback:");
    if (feedbackInput !== null && feedbackInput.trim() !== "") {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/feedback/", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                alert("Feedback saved successfully!");
            }
        };
        var formData = "feedback=" + encodeURIComponent(feedbackInput);
        xhr.send(formData);
    } else {
        alert("Feedback cannot be empty!");
    }
}
function viewLogs() {
            // Redirect to the logs file
            window.location.href = "../static/feedback.log";
        }