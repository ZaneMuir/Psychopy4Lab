#!/usr/bin/env python
#encoding: utf-8

import os
import sys
import re

session_duration = 300
cycle_length = 30
diff_value = 1.0

# to count the number of the spikes in specific time fragment
# input:
## train - spike train in tuple or list
## sesseion_length - valid session duration
## cycle - repeated pattern time duration
## diff - differentiation in time
def counter(train,session_length,cycle,diff):
  cursor = 0.0
  counter = {}
  for item in train:
    while cursor < float(item):
      cursor += diff
    try:
      counter[cursor%cycle] += 1
    except KeyError:
      counter[cursor%cycle] = 1
  return counter

# read raw spike train data from system argument
f = open(sys.argv[1],'r')
data = f.read()
f.close()

# split every channel into dict 'trains' in the form of list, with structure of : {"ch_name":["time_1",...,"time_n"]}
train_raw = re.split(r'\n',data)
trains = {}
for channel in train_raw:
  temp = re.split(r',',channel)
  if temp[0] == '': # remove empty line
    continue
  trains[temp[0]] = temp[1:]

# process counter function, restore results into dict 'result', with structure of : {"ch_name":[results]}
result = {}
for channel,train in trains.items():
  result[channel] = counter(train, session_duration, cycle_length, diff_value)
  print channel, result[channel] # preview in console

# output result into ./{ch_name}.csv
dir_path = os.path.split(sys.argv[1])[0]
for channel, count in result.items():
  f = open(os.path.join(dir_path,channel+'.csv'),'w')
  f.write(channel+',\n')
  for key,item in count.items():
    f.write(str(key)+','+str(item)+'\n')
  f.close()
  print 'export',channel
print 'ok'
