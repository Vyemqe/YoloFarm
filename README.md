# YoloFarm - Agriculture 4.0

A project that integrates modern technology to agriculture. With the aim to boost efficiency in the workforce and production, several technologies are implemented, namely automation, Internet of Things (IOT), and Artificial Intelligence (AI) interference.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-brightgreen)](https://supabase.com/)
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
├── api/
│   ├── main.py                  # FastAPI bootstrap, serial worker
│   ├── routes.py                # HTTP endpoints (health, sensor-data, control-logs, pump control)
│   └── models/
│       └── api_models.py        # Pydantic request/response schemas
├── config/
│   └── settings.py              # Configuration (Adafruit, Supabase, thresholds)
├── gateway/
│   ├── dispatcher.py            # Observer pattern implementation
│   ├── gateway.py               # Core MQTT gateway
│   └── observer.py              # Abstract observer class
├── handlers/                    # MQTT message handlers
│   ├── base_handler.py          # Observer base class
│   ├── temperature_handler.py   # TEMP sensor → sensor_data table
│   ├── humidity_handler.py      # HUMIDITY sensor → sensor_data table
│   ├── moisture_handler.py      # MOISTURE sensor → sensor_data table
│   ├── pump_handler.py          # Pump control + control_logs logging
│   ├── fan_handler.py           # Fan control + control_logs logging
│   └── led_handler.py           # LED control + control_logs logging
├── models/
│   └── sensor_data.py           # Data structures
├── mqtt/
│   ├── client.py                # Singleton Adafruit MQTT client
│   └── topics.py                # Topic constants (6 feeds)
├── services/
│   ├── farm_service.py          # Device control interface
│   ├── serial_service.py        # Yolobit serial communication
│   └── automation_service.py    # Automation rules (temp thresholds)
├── utils/
│   └── logger.py                # Logging utilities
├── scripts/
│   ├── simulate_sensors.py      # Sensor data simulator
│   └── test_bridge_flow.py      # Bridge endpoint tests
├── app.py                       # Gateway entry point
├── api/main.py                  # FastAPI entry point
├── .env.example                 # Environment template
├── requirements.txt
└── README.md
```

## Quick Start
### Requirements
- **Python 3.12+** (or 3.8+ for gateway only)

### Environment Variables
This project reads environment variables from a `.env` file automatically.

Create `.env` at the project root:

```env
# Adafruit IO Configuration
AIO_USERNAME=your_adafruit_username
AIO_KEY=your_adafruit_key

# Supabase Configuration (for FastAPI bridge)
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# Automation Thresholds
TEMP_HIGH_THRESHOLD=37
TEMP_LOW_THRESHOLD=35

# Sensor & Device IDs
TEMPERATURE_SENSOR_ID=1
HUMIDITY_SENSOR_ID=2
MOISTURE_SENSOR_ID=3
PUMP_DEVICE_ID=1
FAN_DEVICE_ID=2
LED_DEVICE_ID=3

# Serial Port (for Yolobit)
SERIAL_PORT=COM3
SERIAL_BAUDRATE=9600

# FastAPI Config
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
```

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

### Running the Gateway

**MQTT Gateway (Adafruit IO):**
```bash
python app.py
```

This starts the MQTT gateway that:
- Connects to Adafruit IO
- Subscribes to all 6 feeds (bbc-temp, bbc-humidity, bbc-moisture, bbc-pump, bbc-fan, bbc-led)
- Processes sensor data and control actions
- Publishes automation commands based on temperature thresholds

### Running the FastAPI Bridge

**FastAPI REST API & Database Bridge:**
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

This starts the FastAPI server that:
- Persists sensor data and control logs to Supabase
- Communicates with Yolobit via serial port (COM3)
- Provides REST API endpoints for external integrations

**Recommended workflow for full demo:**

Terminal 1 - Start MQTT Gateway:
```bash
python app.py
```

Terminal 2 - Start FastAPI Bridge:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Terminal 3 - Run sensor simulator (optional):
```bash
python scripts/simulate_sensors.py --interval 2 --spike-every 6
```

### Testing the Bridge

**Run endpoint tests:**
```bash
python scripts/test_bridge_flow.py
```

**Verify Supabase persistence:**
- Query `/sensor-data/1` to see temperature readings
- Query `/sensor-data/2` to see humidity readings
- Query `/control-logs` to see control actions

**Check Adafruit Dashboard:**
- Verify feeds are receiving data
- Trigger control commands (pump ON/OFF) from dashboard
- Monitor device response on Yolobit

---

## Integration Architecture

```
Adafruit IO Feeds (6)
        ↓
   MQTT Gateway (app.py)
        ↓
   Message Handlers (6)
        ↓
   [Supabase] ← Persistence Layer
   [Serial] ← Com5
        ↓
   FastAPI Bridge (api/main.py)
        ↓
   REST API Endpoints
```

Data Flow:
1. **Adafruit → MQTT → Handlers → Supabase**: Sensor data persists to `sensor_data` table
2. **MQTT → Handlers → Supabase**: Control actions log to `control_logs` table
3. **Serial ← → Yolobit**: Two-way communication for device control
4. **HTTP → FastAPI → Database**: Query sensor history and control logs via REST API

---

## Known Limitations & Future Work

**Current Status:**
- ✅ All 6 Adafruit feeds implemented and tested (TEMP, HUMIDITY, MOISTURE, PUMP, FAN, LED)
- ✅ Sensor data persistence verified in Supabase
- ✅ FastAPI bridge running and responding to health checks
- ✅ MQTT gateway receiving all message types
- ⏳ Control logs: code ready; verify RLS policies and parent FK rows in Supabase
- ⏳ Yolobit serial integration: code ready; awaiting physical device on COM3

**Troubleshooting Control Logs Not Persisting:**
1. Verify parent rows exist in Supabase:
   ```sql
   SELECT * FROM users LIMIT 1;  -- Should return at least one row
   SELECT * FROM devices WHERE device_id IN (1, 2, 3);  -- Should return 3 rows
   ```

2. If empty, seed the tables:
   ```sql
   INSERT INTO users (user_id, email) VALUES (1, 'admin@farm.local') ON CONFLICT DO NOTHING;
   INSERT INTO devices (device_id, name) VALUES 
       (1, 'Pump'), (2, 'Fan'), (3, 'LED') ON CONFLICT DO NOTHING;
   ```

3. Check RLS policies on `control_logs` table — ensure anonymous/authenticated roles can INSERT.

---

## Concepts & Architecture

### What is an IoT Gateway?
A gateway is a network node that serves as the interface between IoT devices and the cloud. In this project:
- The Python MQTT gateway bridges Adafruit IO (cloud) with local devices (Yolobit)
- The FastAPI bridge extends the gateway to include database persistence and REST API access
- Both operate as middleware to translate protocols and store data

### Key Technologies

| Technology | Role |
|-----------|------|
| **Adafruit IO** | MQTT broker and dashboard for IoT visualization |
| **MQTT** | Lightweight publish/subscribe protocol for IoT |
| **Supabase** | PostgreSQL backend as a service for data persistence |
| **FastAPI** | Modern Python web framework for REST API |
| **Yolobit** | Microcontroller board for physical device control |
| **PySerial** | Python-to-serial communication |

### Design Patterns

**Observer Pattern:**
The codebase implements the Observer pattern for extensibility:
- `Observer` (abstract base class) defines message handler interface
- Concrete handlers (Temperature, Humidity, Pump, etc.) implement specific behaviors
- `Dispatcher` manages subscriptions and message routing
- New device types can be added by implementing the Observer interface

**Hysteresis Control:**
Automation prevents relay chatter by using hysteresis thresholds:
- `TEMP_HIGH_THRESHOLD`: Turn ON when temperature exceeds this value
- `TEMP_LOW_THRESHOLD`: Turn OFF when temperature falls below this value
- Prevents rapid ON/OFF cycling when temperature fluctuates around a single threshold

---

## Takeaways
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

## Supported Feeds (Adafruit MQTT)

| Feed | Type | Handler | Persistence | Device ID |
|------|------|---------|-------------|-----------|
| **bbc-temp** | Sensor (Float) | TemperatureHandler | sensor_data (ID=1) | N/A |
| **bbc-humidity** | Sensor (Float) | HumidityHandler | sensor_data (ID=2) | N/A |
| **bbc-moisture** | Sensor (Float) | MoistureHandler | sensor_data (ID=3) | N/A |
| **bbc-pump** | Control (ON/OFF, 0/1) | PumpHandler | control_logs | 1 |
| **bbc-fan** | Control (ON/OFF) | FanHandler | control_logs | 2 |
| **bbc-led** | Control (ON/OFF, 0/1) | LEDHandler | control_logs | 3 |

### FastAPI Bridge (MQTT-Supabase-Serial)

The bridge service enables:
- **MQTT → Database**: Subscribe to Adafruit feeds, persist sensor data and control logs to Supabase PostgreSQL
- **Serial ↔ API**: Communicate with Yolobit device via COM3 serial port
- **REST API**: Query sensors, control devices, audit control actions via HTTP

**Sensor Frame Format (from Yolobit):**
```
!TEMP:25.5#      # Temperature (°C)
!HUMIDITY:60#    # Humidity (%)
!SOIL:45#        # Soil moisture (%)
```

**Control Frame Format (to Yolobit):**
```
!PUMP:ON#        # Turn pump on
!PUMP:OFF#       # Turn pump off
```

**Database Schema:**
- `sensors`: Registered sensor definitions (TEMP, HUMIDITY, MOISTURE)
- `devices`: Registered control devices (PUMP, FAN, LED)
- `sensor_data`: Timestamped sensor readings with FK to sensors
- `control_logs`: Timestamped control actions with FK to devices and users
- `users`: User accounts for access control

#### API Endpoints

**Health Check:**
```
GET /health
Response: {"status": "healthy", "serial_connected": bool, "database_connected": bool}
```

**Query Sensor Data:**
```
GET /sensor-data/{sensor_id}?limit=20&offset=0
Response: [{"log_id": 1, "sensor_id": 1, "value": 25.5, "timestamp": "2024-01-01T12:00:00Z"}, ...]
```

**Query Control Logs:**
```
GET /control-logs?limit=20&offset=0
Response: [{"log_id": 1, "device_id": 1, "action": "ON", "timestamp": "2024-01-01T12:00:00Z"}, ...]
```

**Control Pump:**
```
POST /control/pump
Content-Type: application/json
Body: {"action": "ON"}  # or "OFF"
Response: {"success": true, "message": "Pump turned ON", "command_sent": "!PUMP:ON#"}
```

**MQTT Webhook (for custom integrations):**
```
POST /mqtt/webhook
Content-Type: application/json
Body: {"topic": "bbc-temp", "payload": "25.5"}
Response: {"status": "processed"}
```

---

---

## License
This project is developed for educational purposes as part of the **Multidisciplinary Project** course.

**Authors**: Nguyen Duc Gia Bao, Ho Huy Hung, Nguyen Duy Thai, Nguyen Minh Quan, Nguyen Bao Dat, Nguyen Thanh Huy.

**Institution**: Faculty of Computer Science and Engineering, Ho Chi Minh City University of Technology, VNU-HCM
