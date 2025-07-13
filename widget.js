(function () {
  const button = document.createElement("button");
  button.innerText = "💬 Chatta med Valonix";
  Object.assign(button.style, {
    position: "fixed",
    bottom: "20px",
    right: "20px",
    zIndex: "9999",
    padding: "12px 18px",
    backgroundColor: "#111",
    color: "#fff",
    border: "none",
    borderRadius: "30px",
    cursor: "pointer",
    fontSize: "1rem",
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
  });
  document.body.appendChild(button);

  let iframeOpen = false;
  const iframe = document.createElement("iframe");
  iframe.src = "/widget.html";
  iframe.setAttribute("loading", "lazy");
  iframe.setAttribute("sandbox", "allow-scripts allow-same-origin allow-forms");

  // Responsiv storlek baserat på skärm
  function updateIframeSize() {
    const isMobile = window.innerWidth <= 600;
    Object.assign(iframe.style, {
      position: "fixed",
      bottom: "70px",
      right: "20px",
      width: isMobile ? "90%" : "600px",
      height: isMobile ? "500px" : "700px",
      border: "1px solid #ccc",
      borderRadius: "12px",
      boxShadow: "0 4px 16px rgba(0,0,0,0.2)",
      zIndex: "9998",
      display: "none",
      backgroundColor: "#fff",
    });
  }

  // Init och på resize
  updateIframeSize();
  window.addEventListener("resize", updateIframeSize);

  document.body.appendChild(iframe);

  button.addEventListener("click", () => {
    iframeOpen = !iframeOpen;
    iframe.style.display = iframeOpen ? "block" : "none";
  });
})();
