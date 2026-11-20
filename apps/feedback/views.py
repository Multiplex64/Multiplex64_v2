from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you! Your feedback has been submitted successfully."
            )
            return redirect("feedback:index")
    else:
        form = FeedbackForm()

    return render(request, "feedback/feedback.html", {"form": form})
