(function () {
  const button = document.createElement("button");
  button.innerText = "💬 Chatta med Valonix";
  Object.assign(button.style, {
    position: "fixed",
    bottom: "20px",
    right: "20px",
    zIndex: "9999",
    padding: "14px 20px",
    backgroundColor: "#111",
    color: "#fff",
    border: "none",
    borderRadius: "30px",
    cursor: "pointer",
    fontSize: "1rem",
    fontWeight: "600",
    boxShadow: "0 6px 16px rgba(0,0,0,0.15)",
    transition: "all 0.3s ease",
  });
  document.body.appendChild(button);

  let iframeOpen = false;
  const iframe = document.createElement("iframe");
  iframe.src = "/"; // if same origin
  iframe.setAttribute("loading", "lazy");
  iframe.setAttribute("title", "Valonix Assistent");
  iframe.setAttribute("sandbox", "allow-scripts allow-same-origin allow-forms");

  Object.assign(iframe.style, {
    position: "fixed",
    bottom: "80px",
    right: "20px",
    width: "420px",
    height: "600px",
    border: "1px solid #ccc",
    borderRadius: "16px",
    boxShadow: "0 8px 24px rgba(0,0,0,0.2)",
    zIndex: "9998",
    display: "none",
    backgroundColor: "#fff",
    transition: "all 0.3s ease",
  });

  document.body.appendChild(iframe);

  button.addEventListener("click", () => {
    iframeOpen = !iframeOpen;
    iframe.style.display = iframeOpen ? "block" : "none";
  });

  // OPTIONAL: Close iframe when clicking outside
  document.addEventListener("click", (e) => {
    if (
      iframeOpen &&
      !iframe.contains(e.target) &&
      !button.contains(e.target)
    ) {
      iframe.style.display = "none";
      iframeOpen = false;
    }
  });
})();
