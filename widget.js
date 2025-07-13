(function () {
    const button = document.createElement("button");
    button.innerText = "💬 Chat with Valonix";
    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.zIndex = "9999";
    button.style.padding = "10px 15px";
    button.style.backgroundColor = "#4A90E2";
    button.style.color = "#fff";
    button.style.border = "none";
    button.style.borderRadius = "5px";
    button.style.cursor = "pointer";
    document.body.appendChild(button);

    let iframeOpen = false;
    const iframe = document.createElement("iframe");
    iframe.src = "https://valonix.onrender.com";
    iframe.style.position = "fixed";
    iframe.style.bottom = "70px";
    iframe.style.right = "20px";
    iframe.style.width = "350px";
    iframe.style.height = "500px";
    iframe.style.border = "1px solid #ccc";
    iframe.style.borderRadius = "10px";
    iframe.style.zIndex = "9998";
    iframe.style.display = "none";
    document.body.appendChild(iframe);

    button.addEventListener("click", () => {
        iframeOpen = !iframeOpen;
        iframe.style.display = iframeOpen ? "block" : "none";
    });
})();
