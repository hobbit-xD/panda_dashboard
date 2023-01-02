# Panda Digital Mini-Dashboard

A digital dashboard using Python, a Raspberry Pi 4, vehicle's On Board Diagnostics (OBD-II) Port and displaying data in an external 1.8" TFT display, placed in the watch case.

## Motivation

The main goal of this project is to create a digital dashboard containing the data missing in the original dashboard, for example engine revs, water temperature and so on.

## Display wiring

| Dsiplay | Raspberry Pi 4 |
|---------|----------------|
| VCC     | 3,3V (1)       |
| GND     | GND (6)        |
| CS      | GPIO 8 (24)    |
| RESET   | GPIO 27 (13)   |
| A0      | GPIO 25 (22)   |
| SDA     | GPIO 10 (19)   |
| SCK     | GPIO 11 (23)   |
| LED     | GPIO 18 (12)   |

## Button Wiring

| Button | Raspberry Pi 4 |
|--------|----------------|
| VCC    | 3,3V (17)      |
| PIN    | GPIO 15 (10)   |


## Hardware

- Raspberry Pi 4
- Touchscreen Display of your choice.
- Bluetooth ELM327 OBD-II Device
