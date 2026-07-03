"""Application entry point for CareerPilot AI."""

from app.core.logging import configure_logging


def main() -> None:
    """Initialize application-level services."""

    configure_logging()


if __name__ == "__main__":
    main()
