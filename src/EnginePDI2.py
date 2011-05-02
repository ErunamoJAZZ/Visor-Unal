#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 1/05/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import wx, ImageChops, EngineGlobal
from EngineGlobal import ImgActual

#--Filtros 2
def invertir(event):
    img_out= ImageChops.invert( ImgActual.img_gray )
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out )  )

def init_umbral_bin(event):
    global def_umbral
    dlg = wx.TextEntryDialog(None, u'Introduzca el valor máximo del umbral (El otro lo puede saignar dinamicamente)', u'Umbral Binario',  '')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = int(dlg.GetValue() )
            if 0 > dato > 255: raise ValueError
            def_umbral = lambda i, val_um1, val_um2=dato: 0 if val_um1 < i < val_um2  else 255
            ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( ImgActual.img_gray ), True  )
            
        except ValueError:
            print(u'>> Error, introduzca un número, y Válido')


def init_umbral(event):
    global def_umbral
    def_umbral = lambda i, val_um: 0 if i < val_um else 255
    ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( ImgActual.img_gray ), True  )
    
def umbral(valor_umbral ):
    '''
    recibe un valor para el umbral, y devuelve el bitmap correspondiente.
    '''
    img_out=ImgActual.img_gray.point(lambda i: def_umbral(i, valor_umbral) )
    return EngineGlobal.pilToBitmap( img_out )
    
def suma(event):
    dlg = wx.TextEntryDialog(None,u"Introduzca el valor a SUMAR o RESTAR [-14, por ejemplo]:",'Suma','')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = int(dlg.GetValue() )
            if dato > 255: raise ValueError
            img_out = ImgActual.img_gray.point(lambda i: i + dato )
            ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ), img_out  )
            
        except ValueError:
            print(u'>> Error, introduzca un número, y Válido')    

def multipli(event):   
    dlg = wx.TextEntryDialog(None, u"Introduzca el valor a Multiplicar [2, ó 0.5 para dividir por 2]:", u'Multiplicación',  '')
    if dlg.ShowModal() == wx.ID_OK:
        try:
            dato = float(dlg.GetValue() )
            if dato > 255: raise ValueError
            img_out=ImgActual.img_gray.point(lambda i: int(i * dato )  )
            ImgActual.padre.mostrarFiltro( EngineGlobal.pilToBitmap( img_out ), img_out  )
            
        except ValueError:
            print(u'>> Error, introduzca un número, y Válido')    



