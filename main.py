from flask import Flask
from routes import register_blueprints
from logger import Logger
import time
import threading
from datetime import datetime

app = Flask(__name__)
logger = Logger(app)

# Register blueprints
register_blueprints(app)

def log_time():
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.emit_log(f"Current time: {current_time}")
        time.sleep(10)

if __name__ == '__main__':
    time_logger_thread = threading.Thread(target=log_time)
    time_logger_thread.daemon = True
    time_logger_thread.start()

if __name__ == '__main__':
    app.run(debug=True)


