"""Shared in-memory store for ClimateFarm MVP."""
from typing import List, Dict

# Weather forecasts
weather: List[Dict] = []

# Soil moisture readings
soil: List[Dict] = []

# Alerts generated
alerts: List[Dict] = []

# Farmers registry
farmers: List[Dict] = []
