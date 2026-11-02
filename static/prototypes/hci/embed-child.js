/* Resizes each HCI mockup inside its script-only sandboxed iframe. */
(function () {
  if (window.parent === window) return;
  const main = document.querySelector("main.wrap");
  if (!main) return;
  let lastHeight = 0;
  function reportHeight() {
    const height = Math.ceil(main.getBoundingClientRect().height + main.offsetTop + 2);
    if (!Number.isFinite(height) || height < 300 || height === lastHeight) return;
    lastHeight = height;
    window.parent.postMessage({ type: "hci-prototype:resize", height: height }, "*");
  }
  if (typeof ResizeObserver === "function") new ResizeObserver(reportHeight).observe(main);
  window.addEventListener("resize", reportHeight);
  window.addEventListener("load", reportHeight);
  window.addEventListener("message", function (event) {
    if (event.source !== window.parent || !event.data || event.data.type !== "hci-prototype:measure") return;
    lastHeight = 0;
    reportHeight();
  });
  reportHeight();
})();
