<!-- BANNER IMAGE -->
<!-- Replace URL with your actual banner image -->
<div align="center">


  <h1>psniff🔍</h1>
  <h3>Advanced Network Monitoring & Security Analysis Tool</h3>
</div>


## Features ✨
- Real-time network traffic monitoring
- Port scan detection & threat alerts
- DNS query logging & analysis
- Protocol breakdown (TCP/UDP/ICMP)
- Connection tracking & statistics
- Cross-platform support (Windows/Linux/macOS)
- Customizable whitelists & thresholds

## Installation 💻

### Prerequisites
- Python 3.8+
- Npcap (Windows) / libpcap (Linux)

```bash
# Clone repository
git clone https://github.com/DharanisxX/psniff.git
cd psniff

# Install dependencies
pip install -r requirements.txt
```

### Linux Setup
```bash
# Install libpcap
sudo apt-get install libpcap-dev

# Run with privileges
sudo python3 psniff.py -i eth0
```

### Windows Setup

- Install [Npcap](https://npcap.com)
- Run Command Prompt as Admin:

```cmd
python psniff.py -i "Ethernet"
```

## Usage 🚀

Basic command structure:
```bash
sudo python3 psniff.py -i [interface]
```
Example with common interface names:
```bash
# Linux wireless interface
sudo python3 psniff.py -i wlp2s0

# Windows Ethernet
python psniff.py -i "Ethernet 2"
```

## Configuration ⚙️

Edit the `CONFIG` section in the code:
```python
CONFIG = {
    "CHECK_INTERVAL": 5,      # Stats refresh rate (seconds)
    "SCAN_THRESHOLD": 15,     # SYN packets/min for alerts
    "DNS_THRESHOLD": 50,      # DNS queries/min limit
    "WHITELISTED_IPS": [],    # Trusted IP addresses
    "LOG_FILE": "psniff.log"# Log file path
}
```
