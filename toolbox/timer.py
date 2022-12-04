import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer():
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and record the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def last_elapsed_time(self):
        """Return the last elapsed time when the timer was started and stopped"""

        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        return f"{self._elapsed_time:0.4f} seconds"