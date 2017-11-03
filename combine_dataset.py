from __future__ import print_function
import cv2
import numpy as np
import sys
import os

img_size = (480,270)
save_dir = '/home/symao/data/skyseg'
# list of (data_dir, downsample, augment_rate)
data_dirs = [('/home/symao/data/NVIDIA-Aerial-Drone-Dataset/FPV/AT/GOPR2188',1, 0.3),
            ('/home/symao/data/NVIDIA-Aerial-Drone-Dataset/FPV/AT/GOPR2189',1, 3),
            ('/home/symao/data/NVIDIA-Aerial-Drone-Dataset/FPV/SFWA/360p',8, 0),
            ('/home/symao/data/NVIDIA-Aerial-Drone-Dataset/internet_pictures',1, 4)]
save_idx = 0

def img_diversity_illu(img):
    img = np.copy(img)
    illu_M_foo = []
    illu_M_foo.append(lambda x:np.ones(x.shape,dtype='uint8')*np.random.randint(30,50))
    illu_M_foo.append(lambda x:np.ones(x.shape,dtype='uint8')*np.random.randint(60,80))
    illu_M_foo.append(lambda x:np.ones(x.shape,dtype='uint8')*((np.ones(img.shape[1:],dtype='uint8').T*(np.linspace(np.random.randint(0,10), np.random.randint(30,60),img.shape[1])).astype('uint8')).T))
    illu_M_foo.append(lambda x:np.ones(x.shape,dtype='uint8')*((np.ones(img.shape[1:],dtype='uint8').T*(np.linspace(np.random.randint(50,90), np.random.randint(0,30),img.shape[1])).astype('uint8')).T))

    illu_foo = []
    illu_foo.append(lambda x,M:cv2.add(x,M))
    illu_foo.append(lambda x,M:cv2.subtract(x,M))
    return np.random.choice(illu_foo)(img,np.random.choice(illu_M_foo)(img))

def save_img(img_dir, label_dir, save_dir, downsample = 1, augment = 0):
    global save_idx
    saveimgdir = os.path.join(save_dir,'images')
    savelbldir = os.path.join(save_dir,'labels')
    if not os.path.exists(saveimgdir):
        os.makedirs(saveimgdir)
    if not os.path.exists(savelbldir):
        os.makedirs(savelbldir)

    fimglist = sorted([x for x in os.listdir(img_dir) if '.png' in x or '.jpg' in x])
    for i in range(0,len(fimglist),downsample):
        fimg = fimglist[i]
        if os.path.exists(os.path.join(label_dir,fimg)):
            img = cv2.resize(cv2.imread(os.path.join(img_dir,fimg)),img_size)
            lbl = cv2.resize(cv2.imread(os.path.join(label_dir,fimg)),img_size)
            cv2.imwrite(os.path.join(saveimgdir,'%06d.png'%save_idx),img)
            cv2.imwrite(os.path.join(savelbldir,'%06d.png'%save_idx),lbl)
            save_idx+=1
            print('saving...%d/%d'%(i+1,len(fimglist)), end='\r')
    print('')
    if augment>0:
        print('augmenting...')
        for i in range(0,len(fimglist),downsample):
            fimg = fimglist[i]
            if os.path.exists(os.path.join(label_dir,fimg)):
                img = cv2.resize(cv2.imread(os.path.join(img_dir,fimg)),img_size)
                lbl = cv2.resize(cv2.imread(os.path.join(label_dir,fimg)),img_size)
                temp_rate = augment
                while temp_rate>0:
                    if np.random.rand()<temp_rate:
                        aug_img = img_diversity_illu(img)
                        cv2.imwrite(os.path.join(saveimgdir,'%06d.png'%save_idx),aug_img)
                        cv2.imwrite(os.path.join(savelbldir,'%06d.png'%save_idx),lbl)
                        save_idx+=1
                    temp_rate-=1

if __name__ == '__main__':
    for data_dir,downsample,augment in data_dirs:
        save_img(os.path.join(data_dir,'images'),os.path.join(data_dir,'labels'),save_dir,downsample,augment)
    print('combine dataset finished. save %d images at %s'%(save_idx,save_dir))