'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import Image
import wx
import cv



'''
PIL Image to wx.Image.
@from: http://wiki.wxpython.org/WorkingWithImages
'''
#copy/paste para manejar imagenes PIL & wxImage
def bitmapToPil(bitmap):
    return imageToPil(bitmapToImage(bitmap))

def bitmapToImage(bitmap):
    return wx.ImageFromBitmap(bitmap)

def pilToBitmap(pil):
    return imageToBitmap(pilToImage(pil))

def pilToImage(pil):
    image = wx.EmptyImage(pil.size[0], pil.size[1])
    image.SetData(pil.convert('RGB').tostring())
    return image

def imageToPil(image):
    pil = Image.new('RGB', (image.GetWidth(), image.GetHeight()))
    pil.fromstring(image.GetData())
    return pil

def imageToBitmap(image):
    return image.ConvertToBitmap()
#Fin del copy/paste


'''
PIL Image to OpenCV
'''
def pil2cv_L(imgPIL):
    imgCV = cv.CreateImageHeader(imgPIL.size, cv.IPL_DEPTH_8U, 1)
    cv.SetData(imgCV, imgPIL.tostring() )
    return imgCV

def cv2pil(imgCV):
    imgPIL = Image.fromstring('L', cv.GetSize(imgCV), imgCV.tostring() )
    return imgPIL

