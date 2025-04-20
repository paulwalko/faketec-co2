import digitalio
import board

charge_status_pin = digitalio.DigitalInOut(board.CHARGE_STATUS) #Replace CHARGE_STATUS
charge_status_pin.direction = digitalio.Direction.INPUT

if charge_status_pin.value:  # Assuming high indicates charging
    print("Charging")
else:
    print("Not charging")
