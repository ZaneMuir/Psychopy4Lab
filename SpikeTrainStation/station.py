#!/usr/bin/env python
#encoding: utf-8

#
#
#

import os, sys, re
import spike_filter 
#  import spike_filter.spike_filter(in_file, t_step=1.0,limit=99999,out_file=None) --> dict


def getChannel(working_dir=os.getcwd()):
    channel_files = []
    for item in os.listdir(working_dir):
        if re.match(r'ch_\d{1,2}',item):
            channel_files.append(item)
    return channel_files

def getSession(ch_file,working_dir=os.getcwd()):
    ch_dir = os.path.join(working_dir,ch_file)
    session_files = []
    for item in os.listdir(ch_dir):
        if re.match(r'\d{1,2}\.txt',item):
            session_files.append(item)
    return session_files

if __name__ == '__main__':
    channels = getChannel()
    for each_channel in channels:
        sessions = getSession(each_channel)

        for each_session in sessions:
            spike_filter.spike_filter(os.path.join(os.path.join(os.getcwd(),each_channel),each_session),out_file=os.path.join(os.path.join(os.getcwd(),each_channel),os.path.splitext(each_session)[0]+'.csv'))
