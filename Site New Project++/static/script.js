// script.js
document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll("main section");
    const navLinks = document.querySelectorAll("nav ul li a:not([href='/logout'])");
  
    navLinks.forEach(link => {
      link.addEventListener("click", function(event) {
        event.preventDefault();
        sections.forEach(section => section.style.display = "none");
        document.querySelector(this.getAttribute("href")).style.display = "block";
      });
    });
  
    sections[0].style.display = "block";
  });
  