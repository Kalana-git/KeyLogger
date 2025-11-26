# KeyLogger
This is a simple keylogger using python. It uses keyboard module in pynput library and logging module. The logging module sets up to write debugging information to a text file called "Keylog" with the format "timestamp: message"

# Usage
## Prerequisites
Download pynput using the following command
```bash
sudo apt install python3-pynput
```

Or run
```bash
pip install pynput
```

If the above command doesn't work try install in a virtual environment
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install pynput
```
```bash
python3 Keylogger.py
```

## Command
```bash
python3 Keylogger.py
```

## To exit
Press Esc key
