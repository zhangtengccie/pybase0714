import datetime
import os
import time

now = datetime.datetime.now()
now_format = now.strftime('%Y-%m-%d_%H-%M-%S')
str_now = str(now_format).replace(' ', '_').split('.')[0].replace(':', '-')
file_name = 'save_fivedayago_time_' + now_format + '.txt'
file = open(file_name, 'w')
file.close()
before_5day = now - datetime.timedelta(days=5)
str_before_five = str(before_5day).replace(' ', '_').split('.')[0].replace(':', '-')
os.rename('save_fivedayago_time_' + str_now + '.txt', 'save_fivedayago_time_' + str_before_five + '.txt')
