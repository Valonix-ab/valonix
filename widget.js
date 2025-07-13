(function () {
  const iframe = document.createElement("iframe");
  iframe.src = "https://valonix.onrender.com";
  iframe.style.position = "fixed";
  iframe.style.bottom = "20px";
  iframe.style.right = "20px";
  iframe.style.width = "350px";
  iframe.style.height = "500px";
  iframe.style.border = "none";
  iframe.style.borderRadius = "12px";
  iframe.style.zIndex = "99999";
  iframe.style.boxShadow = "0 0 16px rgba(0,0,0,0.2)";
  document.body.appendChild(iframe);
})();
