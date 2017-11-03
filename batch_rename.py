import os
import sys

def batch_rename(filedir):
    idx = 0
    for f in sorted([x for x in os.listdir(filedir)]):
        os.rename(os.path.join(filedir,f),os.path.join(filedir,'%06d.'%idx+f.rsplit('.')[1]))
        idx+=1

if __name__ == '__main__':
    if len(sys.argv)<2 or '-h' in sys.argv[1]:
        print('Usage: batch_rename [datadir] [datadir2] ...')
    else:
        for i in range(1,len(sys.argv)):
            batch_rename(sys.argv[i])