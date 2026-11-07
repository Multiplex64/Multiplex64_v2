document.addEventListener("DOMContentLoaded", function () {
  const leftbarToggle = document.querySelectorAll('._leftbar-toggle')
  for (var i = 0; i < leftbarToggle.length; i++) {
    const toggleButton = leftbarToggle[i]
    toggleButton.addEventListener("click", function () {
        if (document.body.classList.contains("_leftbar-open")) {
            document.body.classList.remove("_leftbar-open");
        } else {
            document.body.classList.add("_leftbar-open");
        }
    })
  }
});