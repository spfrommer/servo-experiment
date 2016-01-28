# Generates the standard error of the mean for current readings
import csv

def parse_currents(lines):
    column = []
    last_timestamp = float(lines[-1].split(" ")[0])
    for row in lines:
        entries = row.split(" ")
        timestamp = float(entries[0])
        # Get only the straight part of the run to match with the 
        # Regression in plotrun.sh
        if (timestamp >= 200 and timestamp <= last_timestamp - 200):
            column.append(float(entries[2]))
    return column

def get_mean(currents):
    current_sum = 0.0
    for current in currents:
        current_sum += current
    return current_sum / len(currents)

def std_dev(currents):
    mean = get_mean(currents)
    err_sqr_sums = 0.0
    for current in currents:
        err_sqr_sums += (current - mean) ** 2
    std_dev = err_sqr_sums / (len(currents) - 1)
    std_dev = std_dev ** 0.5
    return std_dev

def std_err_mean(currents):
    deviation = std_dev(currents)
    return deviation / (len(currents) ** 0.5)

def output_sem(weight, run):
    file_name = "processed/processed" + str(weight) + "-" + str(run)
    with open(file_name, "r") as file:
        currents = parse_currents(file.readlines())
        sem = std_err_mean(currents)
        print str(sem)


weights=[0, 85, 100, 125, 150, 175, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]

for run in range(0, 6):
    for weight in weights:
        # for the 750g weight only runs 0, 1, and 3 are available
        if weight == 750 and run not in [0, 1, 3]:
            continue
        output_sem(weight, run)
    print
