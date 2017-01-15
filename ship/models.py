from django.db import models
import datetime
# import time


class Department(models.Model):
    officer = models.CharField(max_length=250)
    department_name = models.CharField(max_length=500)
    department_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.department_name + ' - ' + self.officer


class Soldier(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    tag = models.CharField(max_length=250, default="0x00 0x00 0x00 0x00")
    soldier_name = models.CharField(max_length=250)

    def __str__(self):
        return self.soldier_name


class RecordManager(models.Manager):
    def create_singlerecord(self, compartment, tag_string):

        time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        all_soldiers = Soldier.objects.get(tag=tag_string)
        # soldier_name = 'Gibor'
        # for ship_soldier in all_soldiers:
        #     if ship_soldier.tag == tag_string:
        #         soldier_name = ship_soldier.soldier_name

        singlerecord = self.create(compartment=compartment, soldier_name=soldier_name, tag_string=tag_string, time_stamp=time_tag)
        return singlerecord


class SingleRecord(models.Model):
    time_stamp = models.CharField(max_length=250)
    soldier_name = models.CharField(max_length=250, default='ah sheli')
    tag_string = models.CharField(max_length=250, default='0x00 0x00 0x00 0x00')
    compartment = models.IntegerField(default=532)
    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    objects = RecordManager()






