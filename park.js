// Wait for the content to load
document.addEventListener("DOMContentLoaded", () => {
    // Toggle the "Read More" content visibility
    const readMoreButtons = document.querySelectorAll(".read-more");
  
    readMoreButtons.forEach(button => {
      button.addEventListener("click", () => {
        const targetId = button.getAttribute("data-target");
        const moreText = document.getElementById(targetId);
  
        if (moreText.style.display === "none" || moreText.style.display === "") {
          moreText.style.display = "block";
          button.textContent = "Read Less";
        } else {
          moreText.style.display = "none";
          button.textContent = "Read More";
        }
      });
    });
  
    // Contact form submission handling
    const contactForm = document.getElementById("contactForm");
    const formResponse = document.getElementById("formResponse");
  
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      formResponse.textContent = "Sending message...";
  
      // For demonstration, simulate a short delay before showing a successful message.
      setTimeout(() => {
        formResponse.textContent = "Thank you for your message!";
        contactForm.reset();
      }, 1000);
    });
  });