# System Monitoring Application

A real-time system resource monitoring tool built with Python and Flask.

## Features

### Real-time System Monitoring
- CPU usage and temperature monitoring
- Memory usage tracking (RAM and swap)
- Disk usage and I/O statistics
- Network interface monitoring
- Process management and monitoring
- System logs viewing

### User Interface
- Modern, responsive design
- Real-time updates using WebSocket
- Interactive charts and graphs
- Dark theme support
- Mobile-friendly layout

### Technical Features
- RESTful API endpoints
- WebSocket for real-time updates
- SQLite database for data persistence
- Modular architecture
- Error handling and logging

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Nitindagar777/system-monitor.git
   cd system-monitor
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure
```
system-monitor/
├── app/
│   ├── __init__.py
│   ├── systeminfo.py
│   ├── processinfo.py
│   ├── static/
│   │   └── css/
│   │       └── base.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── processes.html
│       ├── process_details.html
│       ├── network.html
│       ├── disks.html
│       └── logs.html
├── logs/
├── screenshot/
├── requirements.txt
├── run.py
└── README.md
```

## API Documentation

### REST API Endpoints

#### System Information
- `GET /api/system/info` - Get system information
- `GET /api/system/cpu` - Get CPU usage and temperature
- `GET /api/system/memory` - Get memory usage statistics
- `GET /api/system/disk` - Get disk usage and I/O statistics
- `GET /api/system/network` - Get network interface statistics

#### Process Management
- `GET /api/processes` - Get list of running processes
- `GET /api/processes/<pid>` - Get detailed process information
- `POST /api/processes/<pid>/terminate` - Terminate a process
- `POST /api/processes/<pid>/suspend` - Suspend a process
- `POST /api/processes/<pid>/resume` - Resume a suspended process

#### System Logs
- `GET /api/logs` - Get system logs
- `GET /api/logs/<log_type>` - Get specific type of logs
- `POST /api/logs/clear` - Clear log files

### WebSocket API

#### Events
- `system_update` - Real-time system information updates
- `process_update` - Real-time process information updates
- `network_update` - Real-time network statistics updates
- `disk_update` - Real-time disk usage updates
- `log_update` - New log entries

## Development

### Setting Up Development Environment
1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
```bash
# Check code style
flake8 app/

# Format code
black app/
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [psutil](https://github.com/giampaolo/psutil) - Python system and process utilities
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Chart.js](https://www.chartjs.org/) - JavaScript charting library
