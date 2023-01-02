# Panda Digital Mini-Dashboard

The main goal of this project is to create a digital dashboard containing the data missing in the original dashboard, for example engine revs, water temperature and so on.
Data are retrived from OBD2 and processed from Raspberry pi and displayed in an external 1.8" TFT display, placed in the watch case.

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
