from __future__ import print_function
import numpy as np
import cv2
import sys
import os

def print_process_bar(percent):
    cnt = 50
    print('['+('>'*int(percent*cnt+0.5)).ljust(cnt)+']%2d%s'%(int(percent*100),'%'), end='\r')

def video2img(video_file,save_dir,stride=1,resize=1,suffix='.png'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print('%s not exists, create it.'%save_dir)
    cap = cv2.VideoCapture(video_file)
    frame_cnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    save_idx = 0
    ret, frame = cap.read()
    r,c = frame.shape[:2]
    print('===============video2img=================')
    print('video_file:%s'%video_file)
    print('save_dir:%s'%save_dir)
    print('stride:%d'%stride)
    print('image size:(%dx%d)'%(c,r)+'  resize:%f to (%dx%d)'%(resize,int(c*resize),int(r*resize)))

    print('read %d frames, start converting...'%frame_cnt)
    whole_cnt = frame_cnt/stride
    while ret:
        cv2.imwrite(os.path.join(save_dir,'%06d%s'%(save_idx,suffix)),cv2.resize(frame,None,fx=resize,fy=resize))
        save_idx += 1
        for i in range(stride):
            ret, frame = cap.read()
        print_process_bar(float(save_idx)/whole_cnt)
    print('\nsave %d images in %s'%(save_idx,save_dir))

if __name__ == '__main__':
    if len(sys.argv)==2 and '-h' in sys.argv[1]:
        print('Usage: video2img.py video_file save_dir [stride] [resize] [suffix]')
    elif len(sys.argv)==3:
        video2img(sys.argv[1], sys.argv[2])
    elif len(sys.argv)==4:
        video2img(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    elif len(sys.argv)==5:
        video2img(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]))
    elif len(sys.argv)==6:
        video2img(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5])
    else:
        print('Usage: video2img.py video_file save_dir [stride] [resize] [suffix]')