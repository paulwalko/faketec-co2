# fatetec-co2

## BOM
* Faketec v1 PCBs. See TODO
* scd41 sensor

## Assembly
1. Push pins all the way through to fit the pcb and 2 nrf52 boards
1. Solder boost pads on nrf52 boards
1. Flash nrf52 boards and test. I like using a black one for the meshtastic board and red one for the sensing board.
1. Solder radio and resistors
1. Solder PCB, then both nrf52 boards
1. Solder the scd41 board

## Post-Assembly
1. Install library required for reading the scd41: `circup install adafruit_scd4x`
1. Plug in usb and connect to the node
1. Set serial to TODO
1. Set user pin to TODO
