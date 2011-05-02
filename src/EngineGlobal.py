#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import Image, wx, cv, os



class ImagenActual():
    '''
    Guarda la imagen actual y su versión en escala de grises.
    Estas imagenes están en formato PIL.
    Guarda tambien el Frame padre, para poder montar las imagenes
    en ventanas.
    '''
    def SetPadre(self, padr):
        self.padre = padr
    
    def SetImagenActual(self, imgAct):
        self.ImagenActual = imgAct
        self.img_gray = imgAct.convert('L')
   
   
    def openImage(self, event):
        dlg = wx.FileDialog(None, message=u"Seleccione un archivo de texto",
                                    defaultDir=os.getcwd(), defaultFile=".txt",
                                    style=wx.OPEN | wx.CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.ImagenActual = Image.open( unicode( path.replace('\\','/')  )  ).convert('RGB')
            dlg.Destroy()
            
            #Aquí se carga la imagen en el GUI
            #padre.bitmap_1= wx.StaticBitmap(padre.panel_para_img, -1, pilToBitmap( ImagenActual< ))
            self.padre.cargarImg(pilToBitmap( self.ImagenActual ))
            self.img_gray = self.ImagenActual.convert('L')



ImgActual = ImagenActual()






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



#==============================================================

'''
Pseudo implementación de la función imhist() de matlab.
'''
def imhist(imgPIL, acumulativo=False):
    '''
    imhist(imgPIL) -> (histImgPIL, histCV, AvgSdv)
    Resibe una imagen tipo PIL, y retorna una Tupla.
    Donde histImPIL es la imagen del histograma,
    histCV es el histograma crudo que hace OpenCV,
    y AvgSdv es una tupla con el valor medio y 
    la desviación estandar.
    '''
    
    def drawHistogram(histograma, scaleX=1.0, scaleY=1.0):
        '''
        Dibuja una imagen para el histograma calculado
        '''
        #rescara el numero máximo de valores en el historial.
        (_, histMax, _, _) = cv.GetMinMaxHistValue(histograma)
        
        #crea la imagen base, y la pone negra.
        imgHist= cv.CreateImage( (scaleX*256, scaleY*64) , 8, 1)
        cv.Zero(imgHist)
        
        
        #dibuja todo el histograma
        for pix in range(0,255):
            histValue = cv.QueryHistValue_1D(histograma, pix)
            nextValue = cv.QueryHistValue_1D(histograma, pix+1)
            
            #Los puntos en python se representan como tuplas :)
            pt1 = (pix*scaleX, 64*scaleY)
            pt2 = (pix*scaleX+scaleX, 64*scaleY)
            pt3 = (pix*scaleX+scaleX, (64-nextValue*64/histMax)*scaleY)
            pt4 = (pix*scaleX, (64-histValue*64/histMax)*scaleY)
            
            #se hace una lista de tuplas
            pts = [pt1, pt2, pt3, pt4]
            
            #se dubuja con el color 255
            cv.FillConvexPoly(imgHist, pts, 255)
        
        #finalmente, se retorna la imagen(imgCV) del histograma ya dibujado.    
        return imgHist
    
    def drawHistogramAccum(histograma, scaleX=1.0, scaleY=1.0):
        '''
        Dibuja una imagen del histograma acumulativo calculado
        '''
        #rescara el numero máximo de valores en el historial.
        #(_, histMax, _, _) = cv.GetMinMaxHistValue(histograma)
        #Una lista con los valore del histograma acumulado
        newHist=[]
        acumulacion=0.0
        for i in range(0,256):
            acumulacion = acumulacion + cv.QueryHistValue_1D(histograma, i)
            newHist.append(acumulacion)
        #para obtener el tamaño máximo luego con sort
        aux=[]
        aux[:]= newHist[:]
        aux.sort()
        histMax= aux[-1]
        
        
        #crea la imagen base, y la pone negra.
        imgHist= cv.CreateImage( (scaleX*256, scaleY*64) , 8, 1)
        cv.Zero(imgHist)
        
        
        #dibuja todo el histograma
        for pix in range(0,255):
            histValue = newHist[pix] #(histograma, pix)
            nextValue = newHist[pix+1]#cv.QueryHistValue_1D(histograma, pix+1)
            
            #Los puntos en python se representan como tuplas :)
            pt1 = (pix*scaleX, 64*scaleY)
            pt2 = (pix*scaleX+scaleX, 64*scaleY)
            pt3 = (pix*scaleX+scaleX, (64-nextValue*64/histMax)*scaleY)
            pt4 = (pix*scaleX, (64-histValue*64/histMax)*scaleY)
            
            #se hace una lista de tuplas
            pts = [pt1, pt2, pt3, pt4]
            
            #se dubuja con el color 255
            cv.FillConvexPoly(imgHist, pts, 255)
        
        #finalmente, se retorna la imagen(imgCV) del histograma ya dibujado.    
        return imgHist
    
    #===================
    #creación del histograma vacío (es como un array)
    rangos = [[0,255]]
    hist = cv.CreateHist([256], cv.CV_HIST_ARRAY, rangos, 1)
    
    #pasar de pil a cv
    src= pil2cv_L(imgPIL)
        
    #calculando el histograma
    cv.CalcHist([cv.GetImage(src)] , hist, 0)  
    
    #=== FINAL ===
    #retorna Tupla (imgPIL, histCV, AvgSdv), este ultimo, es el valor medio y la desviación estandar
    if not acumulativo:
        return (cv2pil( drawHistogram(hist,2,5) ), hist, cv.AvgSdv(cv.GetImage(src)))
    else:
        return (cv2pil( drawHistogramAccum(hist,2,5) ), hist, cv.AvgSdv(cv.GetImage(src)))
            
#==============================================================