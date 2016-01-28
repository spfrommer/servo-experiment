from sys import *
import os
import shutil
import glob
import re

# the timestamp the Arduino sends on its first reading
# this value will be subtracted from all subsequent readings
# to make the first reading have a timestamp zero
start_time = -1

def process_reading(reading, output_file):
    global start_time
    raw_data = re.split('\D*', reading);
    raw_time = int(raw_data[1])
    raw_pos = int(raw_data[2])
    raw_cur = int(raw_data[3])
    if start_time == -1:
        start_time = raw_time
    millis = raw_time - start_time
    degrees = int((180 - (raw_pos - 56) / 2.95) / 1.176)
    amps = 0.025909 * raw_cur - 13.2434742
    output_file.write(str(millis) + ' ' + str(degrees) + ' ' + str(amps) + '\n');

if os.path.exists('processed'):
    shutil.rmtree('processed')
os.mkdir('processed')
raw_files = glob.glob('raw/raw*.txt')

for raw_file in raw_files:
    raw_text = open(raw_file, 'r').read()
    trials = re.split('DONE POSITIONING\n|POSITIONING WITH REVSPEED:.*\n', raw_text)
    for trial_num, trial in enumerate(trials):
        with open('processed/processed' + raw_file[7:-4] + '-' + str(trial_num) + '.txt', 'w+') as output_file:
            start_time = -1
            readings = re.split('\n', trial.strip());
            for reading in readings:
                process_reading(reading, output_file)
