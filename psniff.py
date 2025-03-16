#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================== DEPENDENCIES ======================
import argparse
import sys
import time
from collections import defaultdict
from datetime import datetime
import signal
import platform
from scapy.all import *
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)  
