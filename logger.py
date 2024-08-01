import logging
from flask_socketio import SocketIO
from datetime import datetime

COLOR_MAP = {
    'info': '\033[96m',  # Cyan
    'warning': '\033[93m',  # Yellow
    'error': '\033[91m',  # Red
    'success': '\033[92m',  # Green
    'reset': '\033[0m'  # Reset color
}

# Configure the root logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocketIOHandler(logging.Handler):
    def __init__(self, socketio):
        super().__init__()
        self.socketio = socketio

    # def emit_log(self, message, log_type='info'):
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     color = COLOR_MAP.get(log_type, '')
    #     colored_message = f"{color}[{timestamp}] [{log_type.upper()}] {message}{COLOR_MAP['reset']}"
    #     print(colored_message)
    #     self.socketio.emit('debug_log', {'timestamp': timestamp, 'message': message, 'type': log_type})

    def emit(self, record):
        log_entry = self.format(record)
        self.socketio.emit('debug_log', {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'message': record.getMessage(),
            'type': record.levelname.lower()
        })

def setup_logger(app):
    socketio = SocketIO(app)
    logger = logging.getLogger(__name__)
    
    # Add SocketIOHandler to the logger
    socket_handler = SocketIOHandler(socketio)
    logger.addHandler(socket_handler)
    
    return logger