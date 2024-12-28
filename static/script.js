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

  // Configure marked.js options
  marked.setOptions({
    gfm: true,
    breaks: true,
    headerIds: true,
    mangle: false,
    sanitize: false,
    smartLists: true,
    smartypants: true,
    highlight: function (code, lang) {
      if (lang && hljs.getLanguage(lang)) {
        return hljs.highlight(code, { language: lang }).value;
      }
      return hljs.highlightAuto(code).value;
    },
  });

  fetch("/get-ai-insight")
    .then((response) => response.text())
    .then((content) => {
      clearInterval(messageInterval);

      const container = document.getElementById("ai-markdown");
      let index = 0;
      let currentContent = "";

      function typeWriter() {
        if (index < content.length) {
          currentContent += content[index];
          // Parse the markdown and add the blinking cursor
          container.innerHTML =
            marked.parse(currentContent) + '<span class="blinking-dot"></span>';

          // Highlight any code blocks that were just added
          container.querySelectorAll("pre code").forEach((block) => {
            hljs.highlightElement(block);
          });

          index++;
          setTimeout(typeWriter, 30);
        } else {
          // Final render with the complete content
          container.innerHTML =
            marked.parse(content) +
            '<span class="blinking-dot content-loaded"></span>';

          // Highlight all code blocks one final time
          container.querySelectorAll("pre code").forEach((block) => {
            hljs.highlightElement(block);
          });
        }
      }

      typeWriter();
    })
    .catch((error) => {
      clearInterval(messageInterval);
      document.getElementById(
        "ai-markdown"
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

// Stock recommendations filtering
document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".filters .filter-btn");
  const newsCards = document.querySelectorAll(".news-card");

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      // Remove active class from all buttons
      filterButtons.forEach((btn) => btn.classList.remove("active"));
      // Add active class to clicked button
      button.classList.add("active");

      const filter = button.textContent.trim().toLowerCase();

      newsCards.forEach((card) => {
        const newsType = card
          .querySelector(".news-type")
          .textContent.trim()
          .toLowerCase();

        if (filter === "all") {
          card.style.display = "flex";
        } else if (filter === "buy calls" && newsType === "buy call") {
          card.style.display = "flex";
        } else if (filter === "market news" && newsType === "market news") {
          card.style.display = "flex";
        } else if (filter === "analysis" && newsType === "analysis") {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    });
  });
});
