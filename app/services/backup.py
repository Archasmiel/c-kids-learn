from flask import Flask
from datetime import datetime
import threading, os, time, shutil
from ..config import current_cfg as cfg
from .logger import logger


# Infinite loop for backuping database
def backup_loop():
    cfg.BACKUP_PATH.mkdir(parents=True, exist_ok=True)
    logger.info('Checked backup dir for existance.')

    while True:
        if os.path.exists(cfg.DB_PATH):
            try:
                timestamp_time = datetime.now().strftime("%H-%M-%S")
                current_dir = cfg.BACKUP_PATH / datetime.now().strftime("%Y-%m-%d")
                current_dir.mkdir(exist_ok=True)
                
                backup_file = current_dir / f'backup-{timestamp_time}.db'
                shutil.copy2(cfg.DB_PATH, backup_file)
                logger.backup(f'Created - {backup_file}.')
            except Exception as e:
                logger.backup(f'Failed - {e}.')
        else:
            logger.backup(f'Failed - database file absent.')
        time.sleep(cfg.BACKUP_INTERVAL)


def register(app: Flask):
    logger.info('Launching backup process...')
    threading.Thread(target=backup_loop, daemon=True).start()
