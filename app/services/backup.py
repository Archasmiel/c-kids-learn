import os
import shutil
import threading
import time
from datetime import datetime as dt, timezone as tz

from flask import Flask
from .logger import logger
from ..config import current_cfg as cfg

db_path = cfg.INSTANCE_DIR / 'app.db'
stop_event = threading.Event()


# Infinite loop for database backup
def backup_loop(stop: threading.Event) -> None:
    while not stop.is_set():
        if os.path.exists(db_path):
            try:
                now = dt.now(tz.utc)
                date_dir = cfg.BACKUP_DIR / now.strftime("%Y-%m-%d")
                filename = f'backup-{now.strftime("%H-%M-%S")}.db'

                date_dir.mkdir(exist_ok=True)
                backup_path = date_dir / filename
                shutil.copy2(db_path, backup_path)
                logger.backup(f'Created - {backup_path}.')
            except Exception as e:
                logger.backup(f'Failed - {e}.')
        else:
            logger.backup(f'Failed - database file absent.')
        time.sleep(cfg.BACKUP_INTERVAL)


def register(app: Flask):
    app.backup_stop = stop_event
    t = threading.Thread(target=backup_loop, args=(stop_event,), daemon=True)
    logger.info('Launching backup process...')
    t.start()

    @app.teardown_appcontext
    def _shutdown(_exc):
        stop_event.set()
