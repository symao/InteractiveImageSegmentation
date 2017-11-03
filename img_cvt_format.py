import os
import sys
import cv2

def img_cvt_format(filedir,suffix='.png'):
    idx = 0
    for f in sorted([x for x in os.listdir(filedir)]):
        cv2.imwrite(os.path.join(filedir,f.rsplit('.')[0]+suffix), cv2.imread(os.path.join(filedir,f)))
        os.remove(os.path.join(filedir,f))

if __name__ == '__main__':
    if (len(sys.argv)==2 and '-h' in sys.argv[1]) or len(sys.argv)<3:
        print('Usage: rename_dir [datadir] [siffix]')
    else:
        img_cvt_format(sys.argv[1],sys.argv[2])
