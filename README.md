# YoloFarm - Agriculture 4.0

A project that integrates modern technology to agriculture. With the aim to boost efficiency in the workforce and production, several technologies are implemented, namely automation, Internet of Things (IOT), and Artificial Intelligence (AI) interference.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-orange)](LICENSE)

## Overview

### 1. Python IoT Gateway Implementation
- Libraries installation for Adafruit IO server.
- Python programs implementation using **MQTTClient** (Message Queuing Telemetry Transport) function.
- Program validation with Dashboard.

### 2. Sending data to Adafruit IO
- Create a sample Feed.
- Graphical visualisation on Dashboard.
- Sending data programming: from Gateway to Feed.

---

## Project Structure
```
.
├── config/
│   └── settings.py              # Adafruit IO parameters
├── gateway/
│   ├── dispatcher.py            # Observer implementation
│   ├── gateway.py               # Core Python gateway
│   └── observer.py              # Abstract class
├── handlers                     # Subclasses of Observer/
│   ├── base_handler.py          # Direct subclass
│   ├── pump_handler.py          # Inherited subclass
│   └── temperature_handler.py   # Inherited subclass
├── models/
│   └── sensor_data.py           # Additional data structures
├── mqtt/
│   ├── client.py                # Singleton MQTT Client
│   └── topics.py                # Name of devices to be subscribed
├── services/
│   └── farm_service.py          # Optional services
├── utils/
│   └── logger.py
├── app.py                       # App entry point
├── README.md
└── requirements.txt
```

## Quick Start
### Requirements
- **Python 3.8+**

### Environment Variables
This project reads environment variables from a `.env` file automatically.

Create `.env` at the project root:

```env
AIO_USERNAME=your_adafruit_username
AIO_KEY=your_adafruit_key
TEMP_HIGH_THRESHOLD=37
TEMP_LOW_THRESHOLD=35
```

You can still set variables manually in terminal if needed.

### Environment Setup
1. **Clone the GitHub repository:**
```bash
git clone github.com/Vyemqe/YoloFarm
cd YoloFarm
```

2. **Setup the virtual environment:**
```bash
python -m venv venv/
```

3. **Virtual environment activation:**
```bash
source venv/bin/activate
```

4. **Download requirements:**
```bash
pip install -r requirements.txt
```

5. **Create `.env` file** (if you do not have one already):
```bash
cp .env.example .env
```

PowerShell (Windows):

```powershell
Copy-Item .env.example .env
```

Or create manually with the variables listed in **Environment Variables** above.

**Note:** Remember to deactivate the virtual environment before quitting!
```bash
deactivate
```

### Takeaways
**Python IoT Gateway:** The sample program is located at `gateway/gateway.py`, which simulates the connection between the Python gateway and the Adafruit IO server. To run the program, issue the command:
```python
# Run the gateway application
python app.py
```

### Sensor Simulation (End-to-End test without real devices)
Use the simulator to publish temperature and humidity data into Adafruit IO feeds (`bbc-temp`, `bbc-humidity`).

```bash
python scripts/simulate_sensors.py --interval 2 --spike-every 6
```

Useful options:

- `--interval`: time between publishes (seconds)
- `--spike-every`: every N ticks, generate a spike above threshold
- `--count`: total ticks to send (`0` means run forever)

### Automation behavior
- Gateway checks temperature in `TemperatureHandler`.
- Rule uses hysteresis:
	- If `temperature > TEMP_HIGH_THRESHOLD` -> publish `ON` to `bbc-pump`
	- If `temperature < TEMP_LOW_THRESHOLD` -> publish `OFF` to `bbc-pump`
- This prevents command spam when value fluctuates around one threshold.

---

## License
This project is developed for educational purposes as part of the **Multidisciplinary Project** course.

**Authors**: Nguyen Duc Gia Bao, Ho Huy Hung, Nguyen Duy Thai, Nguyen Minh Quan, Nguyen Bao Dat, Nguyen Thanh Huy.

**Institution**: Faculty of Computer Science and Engineering, Ho Chi Minh City University of Technology, VNU-HCM
