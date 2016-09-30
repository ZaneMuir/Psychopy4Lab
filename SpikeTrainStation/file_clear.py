#!/usr/bin/env python
#encoding: utf-8

import os, sys, re



def data_modify(raw_data):
    return re.split(r'\t',re.split(r'\n',raw_data)[1])[2]
    # return raw_data

cwdir = os.getcwd()
cwdir_son = os.listdir(cwdir) # get files in the current directory
channel_file = []

session_no = 0
channel_no = 0

for item in cwdir_son:
    if os.path.isdir(item):
        if re.match(r'.*?[s|S]\d',item) is not None:
            session_no = re.findall(r'.*?[s|S](\d)', item)[0]
            source_dir = os.path.join(cwdir,item)
            channel_file = os.listdir(source_dir)
            print channel_file
            for channel in channel_file:
                if re.match(r'P', channel) is None:
                    continue
                print source_dir, channel
                channel_no = re.findall(r'PSTH Ch(.*?)\.txt',channel)[0]
                target_dir = os.path.join(cwdir,'ch_'+channel_no)
                if not os.path.isdir(target_dir):
                    os.mkdir(target_dir)
                f_source = open(os.path.join(source_dir,channel),'r')
                f_target = open(os.path.join(target_dir,session_no+'.txt'),'w')
                f_target.write(data_modify(f_source.read()))
                f_source.close()
                f_target.close()
