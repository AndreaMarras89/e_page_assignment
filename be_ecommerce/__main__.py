"""Main Entrypoint."""

import argparse

import gunicorn.app.base
from gunicorn.glogging import Logger
from loguru import logger

from be_ecommerce.configuration import config


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    """Gunicorn Standalone Application."""

    def __init__(self, app, options=None):
        """Inits."""
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        """Loads the configration."""
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """Loads the Application."""
        return self.application


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=config.default_workers)
    parser.add_argument("--bind", type=str, default=f"0.0.0.0:{config.server_port}")
    parser.add_argument("--timeout", type=str, default=str(config.default_timeout))
    parser.add_argument("--local", dest="local", action="store_true")
    parser.set_defaults(local=False)
    args = parser.parse_args()

    options = {
        "bind": args.bind,
        "workers": args.workers,
        "timeout": args.timeout,
        "worker_class": "uvicorn.workers.UvicornWorker",
        "logger_class": Logger,
        "preload": True,
    }

    logger.info("Starting server")
    from be_ecommerce.app import app

    if args.local:
        logger.info("Starting server uvicorn")
        import uvicorn

        _, port = args.bind.split(":")
        uvicorn.run(
            "be_ecommerce.app:app",
            host="0.0.0.0",
            port=config.server_port,
            log_level=config.log_level,
            reload=True,
            workers=config.default_workers,
        )
    else:
        logger.info("Starting server gunicorn")
        StandaloneApplication(app, options).run()
