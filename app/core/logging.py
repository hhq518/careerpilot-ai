"""Reusable logging configuration for the application."""

import logging


DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(level: int = logging.INFO) -> None:
    """Configure application-wide logging."""

    logging.basicConfig(level=level, format=DEFAULT_LOG_FORMAT)
