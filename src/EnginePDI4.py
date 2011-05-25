#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''


import wx, EngineGlobal, cv
from EngineGlobal import ImgActual

def sobel(event):
    imgCV=EngineGlobal.pil2cv_L(ImgActual.img_gray)
    imgCV_salida=cv.CreateImage(cv.GetSize(imgCV), cv.IPL_DEPTH_32F, 1)
    cv.Zero(imgCV_salida)

    cv.Sobel(imgCV, imgCV_salida, 1, 0, 3)
    #Se normaliza la imagen para que se vea bien.
    cv.ConvertScaleAbs(imgCV_salida, imgCV)
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( EngineGlobal.cv2pil(imgCV) )  )
    

def robert(event):
    #TODO: NO IMPLEMENTADO
    pass
    

def canny(event):
    imgCV=EngineGlobal.pil2cv_L(ImgActual.img_gray)
    imgCV_salida=cv.CreateImage(cv.GetSize(imgCV), cv.IPL_DEPTH_8U, 1)
    cv.Zero(imgCV_salida)

    cv.Canny(imgCV, imgCV_salida, 50, 200)
    #Se normaliza la imagen para que se vea bien.
    cv.ConvertScaleAbs(imgCV_salida, imgCV)
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( EngineGlobal.cv2pil(imgCV) )  )


