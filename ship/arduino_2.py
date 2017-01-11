import serial
from django.db import models
from ship.models import Department, Soldier, SingleRecord, RecordManager
import datetime
import time

arduinoDataMega = serial.Serial('com7', 9600)


# time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # '2006-10-25 14:30:59'
compartmentMega = 522

while True:
    while arduinoDataMega.inWaiting() == 0:
        pass  # do nothing
    soldier_tag_Mega = arduinoDataMega.readline().decode('utf-8').strip('\r\n')
    print(soldier_tag_Mega)
    record_for_db_Mega = SingleRecord.objects.create_singlerecord(compartmentMega, soldier_tag_Mega)  # , time_tag


