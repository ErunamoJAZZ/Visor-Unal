# -*- encoding: utf-8 -*-
'''
Created on 28/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import Image,wx,os
import colorsys
import ImageChops


#def_umbral= lambda i, v: i

def loadAll(_padre):
    global padre
    padre=_padre
    
def openImage(event):
    global img, img_gray, def_umbral
    
    
    dlg = wx.FileDialog(None, message="Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.OPEN | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        img = Image.open( unicode( path.replace('\\','/')  )  ).convert('RGB')
        dlg.Destroy()
        
        #Aquí se carga la imagen en el GUI
        #padre.bitmap_1= wx.StaticBitmap(padre.panel_para_img, -1, pilToBitmap( img ))
        padre.cargarImg(pilToBitmap( img ))
        img_gray = img.convert('L')

def saveImagen(event):
    global img_out
    dlg = wx.FileDialog(None, message="Guarde la imagen",
                        defaultDir=os.getcwd(), defaultFile="",
                        style=wx.SAVE | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        img_out.save( unicode( path.replace('\\','/')  )  )
        dlg.Destroy()



#--Filtros
def rgb2grises(event):
    global img_out
    img_out = img.convert('L')
    padre.mostrarFiltro( pilToBitmap( img_out )  )
    
def rgb2r(event):
    global img_out
    s = img.split()
    img_out = s[0]
    padre.mostrarFiltro( pilToBitmap( s[0] )  )
    
def rgb2g(event):
    global img_out
    s = img.split()
    img_out = s[1]
    padre.mostrarFiltro( pilToBitmap( s[1] )  )
    
def rgb2b(event):
    global img_out
    s = img.split()
    img_out = s[2]
    padre.mostrarFiltro( pilToBitmap( s[2] )  )
    
def rgb2hsl(event):#############
    global img_out
    vector = list( img.getdata() )
    vector_out = []#Forzar lista y no tupla
    for pixel in vector:
        vector_out.append( colorsys.rgb_to_hls( *[ x/255.0 for x in pixel ]) )
        
    imagen_out= wx.EmptyImage(img.size[0], img.size[1])
    #imagen_out.SetData( struct.pack('i'*len(vector_out)*3,  vector_out) )

#--Filtros 2
def invertir(event):
    global img_out
    img_out= ImageChops.invert( img.convert('L') )
    padre.mostrarFiltro( pilToBitmap( img_out )  )

def init_umbral(event):
    global def_umbral
    def_umbral = lambda i, val_um: 0 if i < val_um else i
    padre.mostrarFiltro( pilToBitmap( img_gray ), True  )

def init_umbral_bin(event):
    global def_umbral
    def_umbral = lambda i, val_um: 0 if i < val_um else 255
    padre.mostrarFiltro( pilToBitmap( img_gray ), True  )
    
def umbral(valor_umbral ):
    '''
    recibe un valor para el umbral, y devuelve el bitmap correspondiente.
    '''
    global img_out
    img_out=img_gray.point(lambda i: def_umbral(i, valor_umbral) )
    return pilToBitmap( img_out )
    
def suma(event):
    global img_out    
    dlg = wx.TextEntryDialog(None,u"Introduzca el valor a SUMAR o RESTAR [-14, por ejemplo]:",'Suma','')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = int(dlg.GetValue() )
            if dato > 255: raise ValueError
            img_out = img_gray.point(lambda i: i + dato )
            padre.mostrarFiltro( pilToBitmap( img_out )  )
            
        except ValueError:
            print(u'>> Error, introduzca un número, y Válido')    

def multipli(event):
    global img_out    
    dlg = wx.TextEntryDialog(None, u"Introduzca el valor a Multiplicar [2, ó 0.5 para dividir por 2]:", u'Multiplicación',  '')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = int(dlg.GetValue() )
            if dato > 255: raise ValueError
            img_out=img_gray.point(lambda i: i * dato )
            padre.mostrarFiltro( pilToBitmap( img_out )  )
            
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