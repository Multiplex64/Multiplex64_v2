/* 
Main script
Runs in a function on full page load, 
to avoid polluting global namespace
*/
document.addEventListener("DOMContentLoaded", function () {
  // Stuff that runs when the document fully loads
  const leftbarToggle = document.querySelectorAll("._leftbar-toggle");
  for (var i = 0; i < leftbarToggle.length; i++) {
    const toggleButton = leftbarToggle[i];
    toggleButton.addEventListener("click", function () {
      if (document.body.classList.contains("_leftbar-open")) {
        document.body.classList.remove("_leftbar-open");
      } else {
        document.body.classList.add("_leftbar-open");
      }
    });
  }
  // Script to be run every time new page is navigated to
  function load() {}
  // Navigate to a page without full reload
  window._goto = async function (loc, history = true) {};
  // Run load script on first page load
  load();
});
