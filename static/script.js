document.addEventListener("DOMContentLoaded", function () {
  const aiContent = document.getElementById("ai-content");

  const loadingMessages = [
    "Reading the stars ✨",
    "Taking my bull for a walk 🐂",
    "Consulting with Warren Buffett 💼",
    "Analyzing market sentiment 📊",
    "Checking crystal ball 🔮",
    "Trading with the dolphins 🐬",
    "Studying candlestick patterns 📈",
    "Mining market wisdom 💎",
    "Brewing stock potions 🧪",
    "Time traveling to see futures 🚀",
  ];

  function updateLoadingMessage() {
    const loadingMessage = document.querySelector(".loading-message");
    let currentIndex = 0;

    function rotateMessage() {
      loadingMessage.style.opacity = "0";

      setTimeout(() => {
        loadingMessage.textContent = loadingMessages[currentIndex];
        loadingMessage.style.opacity = "1";
        currentIndex = (currentIndex + 1) % loadingMessages.length;
      }, 300);
    }

    // Initial message
    loadingMessage.textContent = loadingMessages[0];

    // Start rotating messages
    return setInterval(rotateMessage, 555);
  }

  // Start the loading animation
  const messageInterval = updateLoadingMessage();

  // Simulate content loading (replace this with your actual API call)
  fetch("/get-ai-insight")
    .then((response) => response.text())
    .then((content) => {
      // Clear the loading animation
      clearInterval(messageInterval);

      const container = document.getElementById("ai-content");
      container.innerHTML = '<span class="blinking-dot"></span>';

      // Type out the content
      let index = 0;
      function typeWriter() {
        if (index < content.length) {
          const currentText = container.innerHTML;
          container.innerHTML =
            content.substring(0, index + 1) +
            '<span class="blinking-dot"></span>';
          index++;
          setTimeout(typeWriter, 30);
        }
      }

      typeWriter();
    })
    .catch((error) => {
      clearInterval(messageInterval);
      document.getElementById(
        "ai-content"
      ).innerHTML = `<div class="error">Error loading AI insights: ${error.message}</div>`;
    });
});

// Theme toggle functionality
function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
}

document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("themeToggle");
  themeToggle.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    setTheme(currentTheme === "dark" ? "light" : "dark");
  });
});
