#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

from EngineGlobal import ImgActual
import EngineGlobal
import ImageFilter, Image

#PARTE 3
def mediana(event):
    img_out = ImgActual.ImagenActual.filter(ImageFilter.MedianFilter())
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ))

def guassiano(event):
    img_out = ImgActual.ImagenActual.filter(ImageFilter.GaussianBlur())
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ))
        
def media(event):
    img_out = ImgActual.ImagenActual.filter(ImageFilter.Kernel((3,3),(0.111111111,0.111111111,0.111111111,
                                                                      0.111111111,0.111111111,0.111111111,
                                                                      0.111111111,0.111111111,0.111111111)))
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ))

    
    
    
###############
def invertir(event):
    img_out= ImageChops.invert( ImgActual.img_gray )
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out )  )