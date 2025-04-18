import adafruit_scd4x
import alarm
import board
import busio
import digitalio
import time

i2c = busio.I2C(board.P0_11, board.P1_04)
uart = busio.UART(board.P0_20, board.P0_22, baudrate=38400, timeout=0)

usr = digitalio.DigitalInOut(board.P1_00)
usr.direction = digitalio.Direction.OUTPUT

scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()


# press for 1 second to wake up mesh and let mesh startup
usr.value = False
time.sleep(1)
usr.value = True
time.sleep(30)

# double tap to send userinfo
usr.value = False
time.sleep(0.5)
usr.value = True
time.sleep(0.5)
usr.value = False
time.sleep(0.5)
usr.value = True
time.sleep(30)

# send co2
while True:
    if scd4x.data_ready:
        s = str('{ "co2_ppm": %d }' % scd4x.CO2)
        print(s)
        print()
        uart.write(bytes(s, 'ascii'))

        # let mesh send data
        time.sleep(30)

        # hold for 5s to shut down mesh
        usr.value = False
        time.sleep(6)
        usr.value = True

        # deep sleep for 5 minutes, and account for drift
        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 5 - 100)
        alarm.exit_and_deep_sleep_until_alarms(time_alarm)
    time.sleep(5)

