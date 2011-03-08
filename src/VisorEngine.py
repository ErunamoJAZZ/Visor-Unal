# -*- encoding: utf-8 -*-
'''
Created on 28/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import Image,wx,os
import colorsys
import ImageChops




def loadAll(_padre):
    global padre
    padre=_padre
    
def openImage(event):
    global img
    
    dlg = wx.FileDialog(None, message="Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.OPEN | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        img = Image.open( unicode( path.replace('\\','/')  )  )
        dlg.Destroy()
        
        #Aquí se carga la imagen en el GUI
        #padre.bitmap_1= wx.StaticBitmap(padre.panel_para_img, -1, pilToBitmap( img ))
        padre.cargarImg(pilToBitmap( img ))

def saveImagen(event):
    pass


#--Filtros
def rgb2grises(event):
    padre.mostrarFiltro( pilToBitmap( img.convert('L') )  )
    
def rgb2r(event):
    s = img.split()
    padre.mostrarFiltro( pilToBitmap( s[0] )  )
    
def rgb2g(event):
    s = img.split()
    padre.mostrarFiltro( pilToBitmap( s[1] )  )
    
def rgb2b(event):
    s = img.split()
    padre.mostrarFiltro( pilToBitmap( s[2] )  )
    
def rgb2hsl(event):
    vector = list( img.getdata() )
    vector_out = []#Forzar lista y no tupla
    for pixel in vector:
        vector_out.append( colorsys.rgb_to_hls( *[ x/255.0 for x in pixel ]) )
        
    imagen_out= wx.EmptyImage(img.size[0], img.size[1])
    #imagen_out.SetData( struct.pack('i'*len(vector_out)*3,  vector_out) )

#--Filtros 2
def invertir(event):
    i= ImageChops.invert( img.convert('L') )
    padre.mostrarFiltro( pilToBitmap( i )  )

def umbral(event):
    dlg = wx.TextEntryDialog(None, u"Introduzca el umbral de 0~255:",
                       'Umbral',  '100')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = int(dlg.GetValue() )
            if dato > 255: raise ValueError
            
            
        except ValueError:
            print(u'>> Error, introduzca un número, y Válido')    




'''
PIL Image to wx.Image.
from: http://wiki.wxpython.org/WorkingWithImawx.Bitmap("/home/erunamo/Documentos/Universidad/VA/lena.jpg", wx.BITMAP_TYPE_ANY)ges
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