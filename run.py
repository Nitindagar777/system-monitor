from app import app
import logging
import os
from logging.handlers import RotatingFileHandler

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler('logs/system_monitor.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('System Monitor startup')

def main():
    try:
        # Run the application
        app.run(
            host='0.0.0.0',  # Allow external connections
            port=5000,       # Default Flask port
            debug=True,      # Enable debug mode for development
            use_reloader=True  # Auto-reload on code changes
        )
    except Exception as e:
        app.logger.error(f'Failed to start application: {str(e)}')
        raise

if __name__ == "__main__":
    main()