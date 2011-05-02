#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import EngineGlobal, Image
from EngineGlobal import ImgActual


#--Filtros
def rgb2grises(event):
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( ImgActual.img_gray )  )
    
def rgb2r(event):
    s = ImgActual.ImagenActual.split()
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( s[0] ) )
    
def rgb2g(event):
    s = ImgActual.ImagenActual.split()
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( s[1] )  )
    
def rgb2b(event):
    s = ImgActual.ImagenActual.split()
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( s[2] ), )
    
    
    
    
    
    
def rgb2hsl(event):#############
    global img_out
    vector = list( img.getdata() )
    vector_out = []#Forzar lista y no tupla
    for pixel in vector:
        vector_out.append( colorsys.rgb_to_hls( *[ x/255.0 for x in pixel ]) )
        
    imagen_out= wx.EmptyImage(img.size[0], img.size[1])
    #imagen_out.SetData( struct.pack('i'*len(vector_out)*3,  vector_out) )
    
    im2=Image.new('HSL', img.size)
    
    
    
    
    



        