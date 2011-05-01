#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 24/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''

import wx, sys
import VisorGUI

global frame_del_visor

if __name__ == '__main__':
    print (u"Hola Mundo!!")
    print (u"Usaré PIL (Python Imageing Library), OpenCV y wxPython para hacer este programa :)"+u"\n\n")
    
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_del_visor = VisorGUI.FrameVisor(None, -1, "")
    app.SetTopWindow(frame_del_visor)
    frame_del_visor.Show()
    app.MainLoop()
    
sys.exit()