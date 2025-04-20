import adafruit_scd4x
import alarm
#import analogio
import board
import busio
import digitalio
import time

#i2c = busio.I2C(board.P0_11, board.P1_04)
#uart = busio.UART(board.P0_20, board.P0_22, baudrate=38400, timeout=0)
#
#usr = digitalio.DigitalInOut(board.P1_00)
#usr.direction = digitalio.Direction.OUTPUT
#
#scd4x = adafruit_scd4x.SCD4X(i2c)
#scd4x.start_periodic_measurement()

# detect button
timer = digitalio.DigitalInOut(board.P1_06)
while True:
  timer.direction = digitalio.Direction.INPUT
  always_on = not timer.value

# get volts
# https://github.com/meshtastic/firmware/blob/master/src/Power.cpp#L291
#vpin = analogio.AnalogIn(board.P0_31)
#while True:
#  operativeAdcMultiplier = 2.0
#  AREF_VOLTAGE = 3.0 
#  BATTERY_SENSE_RESOLUTION_BITS = 12
#  BATTERY_SENSE_SAMPLES = 15
#
#  volts = 0
#  for i in range(BATTERY_SENSE_SAMPLES):
#      volts += vpin.value
#  volts = vpin.value / BATTERY_SENSE_SAMPLES
#
#  volts = operativeAdcMultiplier * ((1000 * AREF_VOLTAGE) / pow(2, BATTERY_SENSE_RESOLUTION_BITS)) * volts;
#  volts = volts / 1024
#  print(str('v: %3.2f' % volts))
#  time.sleep(1)
#
## press for 1 second to wake up mesh and let mesh startup
#usr.value = False
#time.sleep(1)
#usr.value = True
#time.sleep(30)
#
## double tap to send userinfo
#usr.value = False
#time.sleep(0.5)
#usr.value = True
#time.sleep(0.5)
#usr.value = False
#time.sleep(0.5)
#usr.value = True
#time.sleep(30)
#
## send co2
#while True:
#    if scd4x.data_ready:
#        #s = str('{ "co2_ppm": %d }' % scd4x.CO2)
#        volts = v.value * 4.20 * 2 / 65535
#        s = str('{ "co2_ppm": %d, "volts": %5.2f }' % (scd4x.CO2, volts))
#        print(s)
#        print()
#        uart.write(bytes(s, 'ascii'))
#
#        # let mesh send data
#        time.sleep(30)
#
#        # hold for 5s to shut down mesh
#        usr.value = False
#        time.sleep(6)
#        usr.value = True
#
#        # deep sleep for 5 minutes, and account for drift
#        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60 * 5 - 100)
#        alarm.exit_and_deep_sleep_until_alarms(time_alarm)
#    time.sleep(5)
#
