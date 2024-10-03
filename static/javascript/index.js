 // Array of rotating messages
const messages = [
    "questions to ask",
    "story to share",
    "ideas to share"
];

let currentIndex = 0;

function rotateText() {
    const rotatingTextElement = document.getElementById('rotatingText');
    rotatingTextElement.style.visibility = 'hidden'; // Hide the text before reappearing

    setTimeout(() => {
        // Update the text and trigger the typing animation
        rotatingTextElement.textContent = messages[currentIndex];
        rotatingTextElement.style.visibility = 'visible'; // Make it visible
        rotatingTextElement.style.animation = 'none'; // Reset animation

        // Trigger retyping by forcing reflow
        rotatingTextElement.offsetHeight; // Trigger reflow

        // Start typing animation
        rotatingTextElement.style.animation = 'typing 3s steps(30, end) forwards, blink 0.7s step-end infinite';

        // Increment the index and reset if at the end of the array
        currentIndex = (currentIndex + 1) % messages.length;
    }, 100); // Delay to ensure smooth reset
}

// Initial call to set the first message
rotateText();

// Change the text every 5 seconds
setInterval(rotateText, 5000);