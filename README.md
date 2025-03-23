# fatetec-co2
* This is heavily based on gargomoma's faketec v2 board, plus an additional board to gather data (or do anything else) and send it over the mesh via serial. In the photo below, the bottom board is running meshtastic while the top board is running circuit python.
* Every 30 minutes, the circuitpython board wakes up the mesh board, triggers userinfo, sends sensor readings, then shuts down the mesh board and deep sleeps for 30 more minutes.
* With a 2500 mah battery, this can go 4-5 days.

![image](https://github.com/user-attachments/assets/278707ab-374d-4448-8f25-4301c8a08ccd)


## BOM
* Faketec v2
* scd41 sensor

## Assembly
1. Push pins all the way through to fit the pcb and 2 nrf52 boards
1. Solder boost pads on nrf52 boards
1. Flash nrf52 boards and test. I like using a black one for the meshtastic board and red one for the circuit python board.
1. Solder radio and ADC resistors
1. Solder PCB, then both nrf52 boards
1. Solder the scd41 board

## Post-Assembly (meshastic board)
1. Plug in usb to meshtastic board
1. Set user pin to 32
1. Set Device role to `CLIENT_MUTE`. (This doesn't really matter that much since we're controlling power externally).
1. Configure serial settings:
  1. Toggle 'Serial enabled' and 'Echo enabled'
  1. RX: 20, TX: 22.
  1. Serial mode: `TEXTMSG`
1. Set the primary channel to something other than the default, and the above serial settings will spam it quite a bit.

## Post-Assembly (circuitpython board)
1. Plug in usb to circuitpythong board and mount it
1. Install library required for reading the scd41: `circup install adafruit_scd4x`
1. Copy the `co2_nicenano.py` file to the board

## Verify
1. Unplug cables, then plug in usb to meshtastic board and monitor the serial output
1. After 30s, it should send out a userinfo message
1. After 30 more seconds, it should send out a co2 reading then shutdown.
  1. For full verification, you need a second node to receive the message that shares the channel with this node.

## Links
* main faketec project: https://github.com/gargomoma/fakeTec_pcb/tree/main
* scd41 board: https://www.aliexpress.us/item/3256807392920746.html
