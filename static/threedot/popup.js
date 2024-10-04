document.addEventListener("DOMContentLoaded", () => {
  const threeDotButton = document.querySelectorAll(".three-dot");

  threeDotButton.forEach((button) => {
    button.addEventListener("click", (event) => {
      // Close other popups
      const popups = document.querySelectorAll(".popup");
      popups.forEach((popup) => {
        if (popup !== button.nextElementSibling) {
          popup.style.display = "none";
        }
      });

      // Toggle the current popup
      const popup = button.nextElementSibling;
      popup.style.display = popup.style.display === "block" ? "none" : "block";
    });
  });

  // Close the popup if clicked outside of it
  window.addEventListener("click", (event) => {
    const popups = document.querySelectorAll(".popup");
    popups.forEach((popup) => {
      if (
        !popup.contains(event.target) &&
        !popup.previousElementSibling.contains(event.target)
      ) {
        popup.style.display = "none";
      }
    });
  });
});
