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
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  });
  document.body.appendChild(button);

  let open = false;
  const iframe = document.createElement("iframe");
  iframe.src = "index.html";
  Object.assign(iframe.style, {
    position: "fixed",
    bottom: "70px",
    right: "20px",
    width: "400px",
    height: "600px",
    border: "none",
    borderRadius: "16px",
    boxShadow: "0 6px 20px rgba(0,0,0,0.2)",
    zIndex: "9998",
    display: "none"
  });
  document.body.appendChild(iframe);

  button.addEventListener("click", () => {
    open = !open;
    iframe.style.display = open ? "block" : "none";
  });
})();
