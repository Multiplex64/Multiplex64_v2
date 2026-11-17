import logging
import time

logger = logging.getLogger("request_logger")

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Start timer before processing the request
        start_time = time.monotonic()

        # 2. Extract client IP (handles reverse proxies like Nginx)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(",")[0].strip()
        else:
            client_ip = request.META.get("REMOTE_ADDR")

        # 3. Pass request down to the view and capture the response
        response = self.get_response(request)

        # 4. Calculate total processing duration in milliseconds
        duration_ms = (time.monotonic() - start_time) * 1000

        # 5. Identify authenticated user if available
        user = (
            request.user.username
            if hasattr(request, "user") and request.user.is_authenticated
            else "Anonymous"
        )

        # 6. Log the structured details
        logger.info(
            f"[{request.method}] {request.get_full_path()} | "
            f"Status: {response.status_code} | "
            f"Duration: {duration_ms:.2f}ms | "
            f"User: {user} | "
            f"IP: {client_ip}"
        )

        return response