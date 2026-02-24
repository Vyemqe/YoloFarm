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
├── src/
│   ├── gateway.py    # Sample Python Gateway
│   └── prog_data.py  # Sending data to AIO server
├── README.md
└── requirements.txt
```

## Quick Start
### Requirements
- **Python 3.8+**

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

**Note:** Remember to deactivate the virtual environment before quitting!
```bash
deactivate
```

### Takeaways
1. **Python IoT Gateway:** The sample program is located at `src/gateway.py`, which simulates the connection between the Python gateway and the Adafruit IO server. To run the program, issue the command:
```python
# Lower version Python
python src/gateway.py

# Python 3 if supported. Check with `which python3`
python3 src/gateway.py
```

2. **Sending data to AIO server:** The sample program is located at `src/prog_data.py`, which is an extended version of the file `src/gateway.py`. Key changes:
- **Library:**
    - Sending random data to the AIO server by `import random`.
    - Data is sent periodically (e.g. 30 seconds each) using `import time`.
- The `while True:` loop now periodically sends data besides listening to the server. When there are changes in the Dashboard, the results are also sent back to the Gateway.

---

## License
This project is developed for educational purposes as part of the **Multidisciplinary Project** course.

**Authors**: Nguyen Duc Gia Bao, Ho Huy Hung, Nguyen Duy Thai, Nguyen Minh Quan, Nguyen Bao Dat, Nguyen Thanh Huy.

**Institution**: Faculty of Computer Science and Engineering, Ho Chi Minh City University of Technology, VNU-HCM
