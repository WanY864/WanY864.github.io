/* Accept resize messages only from one of our embedded prototype frames. */
(function () {
  const frames = Array.from(document.querySelectorAll("iframe[data-hci-prototype]"));
  if (!frames.length) return;
  window.addEventListener("message", function (event) {
    if (!event.data || event.data.type !== "hci-prototype:resize") return;
    const frame = frames.find(function (frame) { return frame.contentWindow === event.source; });
    if (!frame) return;
    const height = event.data.height;
    if (typeof height !== "number" || !Number.isFinite(height) || height < 300 || height > 2400) return;
    frame.style.height = Math.ceil(height) + "px";
  });
  frames.forEach(function (frame) {
    function askForHeight() {
      if (frame.contentWindow) frame.contentWindow.postMessage({ type: "hci-prototype:measure" }, "*");
    }
    frame.addEventListener("load", askForHeight);
    askForHeight();
  });
})();
