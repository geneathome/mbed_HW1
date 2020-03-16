# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '105000005.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
       data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

C0A880 = []
C0F9A0 = []
C0G640 = []
C0R190 = []    
C0X260 = []

for i in range(len(data)):
    if data[i]['WDSD'] == '-99.000' or data[i]['WDSD'] == '-999.000' :
        a = 0; 
    else: 
        if data[i]['station_id'] == 'C0A880':
            C0A880.append(data[i]['WDSD'])
        if data[i]['station_id'] == 'C0F9A0':
            C0F9A0.append(data[i]['WDSD'])
        if data[i]['station_id'] == 'C0G640':
            C0G640.append(data[i]['WDSD'])
        if data[i]['station_id'] == 'C0R190':
            C0R190.append(data[i]['WDSD'])
        if data[i]['station_id'] == 'C0X260':
            C0X260.append(data[i]['WDSD'])
            
if (len(C0A880) == 0):
    max_range_C0A880 = 'None'
else:
    max_range_C0A880 = float(max(C0A880))-float(min(C0A880))
    if max_range_C0A880 == 0:
        max_range_C0A880 = 'None'
    
if (len(C0F9A0) == 0):
    max_range_C0F9A0 = 'None'
else:
    max_range_C0F9A0 = float(max(C0F9A0))-float(min(C0F9A0))
    if max_range_C0F9A0 == 0:
        max_range_C0F9A0 = 'None'
    
if (len(C0G640) == 0):
    max_range_C0G640 = 'None'
else:
    max_range_C0G640 = float(max(C0G640))-float(min(C0G640))
    if max_range_C0G640 == 0:
        max_range_C0G640 = 'None'
    
if (len(C0R190) == 0):
    max_range_C0R190 = 'None'
else:
    max_range_C0R190 = float(max(C0R190))-float(min(C0R190))
    if max_range_C0R190 == 0:
        max_range_C0R190 = 'None'
    
if (len(C0X260) == 0):
    max_range_C0X260 = 'None'
else:
    max_range_C0X260 = float(max(C0X260))-float(min(C0X260))
    if max_range_C0X260 == 0:
        max_range_C0X260 = 'None'
#=======================================

# Part. 4
#=======================================
# Print result
C0A880_range = ['C0A880', str(max_range_C0A880)]
C0F9A0_range = ['C0F9A0', str(max_range_C0F9A0)]
C0G640_range = ['C0G640', str(max_range_C0G640)]
C0R190_range = ['C0R190', str(max_range_C0R190)]
C0X260_range = ['C0X260', str(max_range_C0X260)]

print([C0A880_range,C0F9A0_range,C0G640_range,C0R190_range,C0X260_range])
#========================================