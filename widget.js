(function () {
  const button = document.createElement("button");
  button.setAttribute("aria-label", "Chatta med Valonix");

  // Ikonbild från Render-länk
  const img = document.createElement("img");
  img.src = "https://valonix.onrender.com/static/logo.png";
  img.alt = "Valonix logotyp";
  Object.assign(img.style, {
    width: "60%",
    height: "60%",
    objectFit: "contain",
    display: "block",
    margin: "auto",
  });

  button.appendChild(img);

  // Knappstil – nu mindre och mer kompakt
  Object.assign(button.style, {
    position: "fixed",
    bottom: "20px",
    right: "20px",
    zIndex: "9999",
    padding: "0",
    width: "50px",
    height: "50px",
    backgroundColor: "#000",
    border: "none",
    borderRadius: "12px",
    cursor: "pointer",
    overflow: "hidden",
    transition: "transform 0.2s ease, box-shadow 0.2s ease",
    boxShadow: "0 6px 20px rgba(0, 0, 0, 0.25)",
  });

  // Hover-effekt
  button.addEventListener("mouseenter", () => {
    button.style.transform = "scale(1.08)";
    button.style.boxShadow = "0 10px 24px rgba(0, 0, 0, 0.35)";
  });

  button.addEventListener("mouseleave", () => {
    button.style.transform = "scale(1)";
    button.style.boxShadow = "0 6px 20px rgba(0, 0, 0, 0.25)";
  });

  document.body.appendChild(button);

  // Iframe
  let iframeOpen = false;
  const iframe = document.createElement("iframe");
  iframe.src = "/widget.html";
  iframe.setAttribute("loading", "lazy");
  iframe.setAttribute("sandbox", "allow-scripts allow-same-origin allow-forms");

  function updateIframeSize() {
    const isMobile = window.innerWidth <= 600;
    Object.assign(iframe.style, {
      position: "fixed",
      bottom: "80px",
      right: "20px",
      width: isMobile ? "90%" : "600px",
      height: isMobile ? "500px" : "700px",
      border: "1px solid #ccc",
      borderRadius: "12px",
      boxShadow: "0 4px 24px rgba(0,0,0,0.3)",
      zIndex: "9998",
      display: iframeOpen ? "block" : "none",
      backgroundColor: "#fff",
    });
  }

  updateIframeSize();
  window.addEventListener("resize", updateIframeSize);
  document.body.appendChild(iframe);

  // Toggle widget
  button.addEventListener("click", () => {
    iframeOpen = !iframeOpen;
    updateIframeSize();
  });
})();
