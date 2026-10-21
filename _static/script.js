document.addEventListener("DOMContentLoaded", function () {
  leftbarToggle = document.querySelectorAll('._leftbar-toggle')
  for (var i = 0; i < leftbarToggle.length; i++) {
    toggleButton = leftbarToggle[i]
    toggleButton.addEventListener("click", function () {
        if (document.body.classList.contains("_leftbar")) {
            document.body.classList.remove("_leftbar");
        } else {
            document.body.classList.add("_leftbar");
        }
    })
  }
});