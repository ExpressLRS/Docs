// Turns the git_info dates (<span class="timeago" datetime=...>) into "3 months ago"
document$.subscribe(function() {
  var rtf = new Intl.RelativeTimeFormat(document.documentElement.lang || "en", { numeric: "auto" })
  var units = [["year", 31536000], ["month", 2592000], ["week", 604800], ["day", 86400], ["hour", 3600], ["minute", 60]]
  document.querySelectorAll(".md-source-file .timeago[datetime]").forEach(function(el) {
    var secs = (Date.parse(el.getAttribute("datetime")) - Date.now()) / 1000
    for (var i = 0; i < units.length; i++) {
      if (Math.abs(secs) >= units[i][1] || i === units.length - 1) {
        el.textContent = rtf.format(Math.round(secs / units[i][1]), units[i][0])
        break
      }
    }
  })
})
