# Log Anomaly Detector (Python)

A backend utility built using Python to analyze application logs and detect anomalous patterns such as error spikes and suspicious login failures.

## Features
- Counts and monitors ERROR-level logs
- Detects abnormal error spikes using rule-based thresholds
- Identifies repeated failed login attempts (possible brute-force attacks)
- Generates clear console alerts for system administrators

## Tech Stack
- Python
- Basic pattern matching
- Dictionary-based frequency analysis

## How It Works
1. Application logs are read as input
2. Logs are analyzed to establish normal behavior
3. Rule-based thresholds detect anomalies
4. Alerts are generated for abnormal patterns

## Use Cases
- Backend system monitoring
- Security anomaly detection
- Pre-crash system alerting

## How to Run
```bash
python main.py
