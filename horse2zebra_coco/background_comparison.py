from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_psnr as psnr
import matplotlib.pyplot as plt
import numpy as np
import cv2
from pdb import set_trace as st
horse2zebra=False
AttnGANFold='/home/xche6658/code/pytorch-CycleGAN-and-pix2pix/results/horse2zebra_coco/zebra_attnganX2-200_featloss_sparse1/test_200/images/'
if horse2zebra:
  suffix='_real_A_fake_B.png'
#  suffix='_fake_B.png'
  CycleGANFold='CycleGAN_fake_zebra/'
  segFold='segmentation_horse/'
  SourceFold='real_horse/'
else:# zebra2horse
  suffix='_real_A_fake_A.png'
 # suffix='_fake_A.png'
  CycleGANFold='CycleGAN_fake_horse/'
  segFold='segmentation_zebra/'
  SourceFold='real_zebra/'
CycleGANList=CycleGANFold+'list.txt'
segList = segFold + 'list.txt'
SourceList = SourceFold + 'list.txt'

CycleGANLListRead = open(CycleGANList)
segListRead = open(segList)
SourceListRead = open(SourceList)

fileCycle = CycleGANLListRead.readline()
fileSource = SourceListRead.readline()
fileseg = segListRead.readline()

sum_psnr_cycle=0
sum_psnr_attngan = 0
sum_ssim_cycle=0
sum_ssim_attngan=0
num_file=0
while (''!=fileCycle):
    # Read image 
    ImageCycle = cv2.imread(CycleGANFold + fileCycle[:-1])
    ImageSource = cv2.imread(SourceFold + fileSource[:-1])
    ImageAttnGAN= cv2.imread(AttnGANFold+fileSource[:12]+suffix)
    
    ImageSeg = 255 - cv2.imread(segFold+fileseg[:-1])
    err_psnr_cylce = psnr(ImageSource*ImageSeg, ImageCycle*ImageSeg)
    err_psnr_attngan = psnr(ImageSource*ImageSeg, ImageAttnGAN*ImageSeg)
    sum_psnr_cycle += err_psnr_cylce
    sum_psnr_attngan += err_psnr_attngan

    err_ssim_cylce = ssim(ImageSource*ImageSeg, ImageCycle*ImageSeg, multichannel=True)
    err_ssim_attngan = ssim(ImageSource*ImageSeg, ImageAttnGAN*ImageSeg, multichannel=True)
    sum_ssim_cycle += err_ssim_cylce
    sum_ssim_attngan += err_ssim_attngan
    num_file +=1

    fileCycle = CycleGANLListRead.readline()
    fileSource = SourceListRead.readline()
    fileseg = segListRead.readline()
#   fileAttnGAN = AttnGANListRead.readline()

ave_psnr_cycle = sum_psnr_cycle / num_file
ave_psnr_attn = sum_psnr_attngan / num_file
ave_ssim_cycle = sum_ssim_cycle / num_file
ave_ssim_attn = sum_ssim_attngan / num_file
print(AttnGANFold)
if horse2zebra:
  print('horse2zebra:')
else:
  print('zebra2horse:')
print('cycle averaged psnr:%f' % ave_psnr_cycle)
print('attngan averaged psnr:%f'% ave_psnr_attn)
print('cycle averaged ssim:%f' % ave_ssim_cycle)
print('attngan averaged ssim:%f'% ave_ssim_attn)


