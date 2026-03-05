document.addEventListener("click", function (e) {
    var btn = e.target.closest("a.md-button--primary");
    if (!btn) return;
    var url = btn.getAttribute("href");
    if (!url || !url.includes("/raw/")) return;
    e.preventDefault();
    var filename = url.split("/").pop() || "SKILL.md";
    // Rewrite GitHub raw URL to jsDelivr CDN (supports CORS)
    var cdnUrl = url
        .replace("https://github.com/", "https://cdn.jsdelivr.net/gh/")
        .replace("/raw/main/", "@main/");
    fetch(cdnUrl)
        .then(function (r) { return r.blob(); })
        .then(function (blob) {
            var a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(a.href);
        });
});
