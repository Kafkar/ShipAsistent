from flask import Flask
from routes import register_blueprints
from logger import  setup_logger
import time
import threading
from datetime import datetime
import configparser
from modu  les/nmea_thread import NMEAThread


app = Flask(__name__)
logger = setup_logger(app)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Register blueprints
register_blueprints(app)

def log_time():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Current time: {current_time}")
        logger.warning(f"something is wrong")
        time.sleep(10)

if __name__ == '__main__':
    time_logger_thread = threading.Thread(target=log_time)
    time_logger_thread.daemon = True
    time_logger_thread.start()

if __name__ == '__main__':
    if config.getboolean('Modules', 'nmea_enabled', fallback=False):
    nmea_thread = NMEAThread(logger)
    nmea_thread.start()
    logger.info("NMEA thread started")
    app.run(debug=True)


