#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

from EngineGlobal import ImgActual

#PARTE 3
def histograma(event):
    global img_out
    img_out = img.convert('L')
    padre.mostrarFiltro( EngineGlobal.pilToBitmap( imhist(img_out )  ), imhist(img_out )  )


def median(event):
    global img_out
    img_out = img.filter(ImageFilter.MedianFilter())
    padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ), img_out )

