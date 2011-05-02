# -*- encoding: utf-8 -*-
'''
Created on 24/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''
import wx, os
import VisorEngine, EngineGlobal
import EnginePDI1, EnginePDI2, EnginePDI3, EnginePDI4
from EngineGlobal import ImgActual


class FrameVisor(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_imagenes = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.panel_imagen1 = wx.Panel(self.notebook_imagenes, -1)
        self.panel_para_img = wx.Panel(self.panel_imagen1, -1)
        self.bitmap_1 = wx.StaticBitmap(self.panel_para_img, -1)
        ImgActual.SetPadre(self)
        
        # Menu Bar
        self.__barra_de_menu()
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxFrame.__set_properties
        self.SetTitle(u"Visor - Carlos Daniel Sanchez Ramirez")
        self.SetSize((400, 200))
        self.SetMinSize((400, 200))
        self.Center()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_para_img = wx.BoxSizer(wx.HORIZONTAL)
        sizer_para_img.Add(self.bitmap_1, 0, 0, 0)
        self.panel_para_img.SetSizer(sizer_para_img)
        sizer_2.Add(self.panel_para_img, 10, wx.EXPAND, 0)
        self.panel_imagen1.SetSizer(sizer_2)
        self.notebook_imagenes.AddPage(self.panel_imagen1, "imagen")
        sizer_1.Add(self.notebook_imagenes, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def __barra_de_menu(self):
                # Menu Bar
        self.frame_del_visor_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        abrir = wxglade_tmp_menu.Append(wx.NewId(), "Abrir", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, ImgActual.openImage, abrir)
        salir = wxglade_tmp_menu.Append(wx.NewId(), "Salir", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.salir, salir)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Archivo")
        
        
        #PARTE 1
        wxglade_tmp_menu = wx.Menu()
        gris = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> Grises", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI1.rgb2grises, gris)
        r = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> R", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI1.rgb2r, r)
        g = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> G", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI1.rgb2g, g)
        b = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> B", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI1.rgb2b, b)
        hsi = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> HSI", "", wx.ITEM_NORMAL)
        
        rgb = wxglade_tmp_menu.Append(wx.NewId(), "HSI -> RGB", "", wx.ITEM_NORMAL)
        
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros 1")
        
        
        #PARTE 2
        wxglade_tmp_menu = wx.Menu()
        invertir = wxglade_tmp_menu.Append(wx.NewId(), "Invertit grises", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI2.invertir, invertir)
        umbral = wxglade_tmp_menu.Append(wx.NewId(), "Umbral", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI2.init_umbral, umbral)
        umbral_bin = wxglade_tmp_menu.Append(wx.NewId(), "Umbral binario", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI2.init_umbral_bin, umbral_bin)
        sum = wxglade_tmp_menu.Append(wx.NewId(), "Suma/resta", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI2.suma, sum)
        mult = wxglade_tmp_menu.Append(wx.NewId(), u"Multiplicación/División", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, EnginePDI2.multipli, mult)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros 2")
        
        
        #PARTE 3
        wxglade_tmp_menu = wx.Menu()
        histo = wxglade_tmp_menu.Append(wx.NewId(), "Histograma", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.histograma, histo)
        histoAcum = wxglade_tmp_menu.Append(wx.NewId(), "Histograma Acumulativo", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, histoAcum)
        #
        media = wxglade_tmp_menu.Append(wx.NewId(), "Media", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, media)
        mediana = wxglade_tmp_menu.Append(wx.NewId(), "Mediana", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.median, mediana)
        gauss = wxglade_tmp_menu.Append(wx.NewId(), "Gauss", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, gauss)
        #
        uniforme = wxglade_tmp_menu.Append(wx.NewId(), "Uniforme Local", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, uniforme)
        uniforme2 = wxglade_tmp_menu.Append(wx.NewId(), "Uniforme Global", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, uniforme2)
        exponencial = wxglade_tmp_menu.Append(wx.NewId(), "Exponencial", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, exponencial)
        rayleigh = wxglade_tmp_menu.Append(wx.NewId(), "Rayleigh", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, rayleigh)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros 3")
        
        #FIN
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Acerca de...", "", wx.ITEM_NORMAL)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "...")
        
        self.SetMenuBar(self.frame_del_visor_menubar)
        # Menu Bar end

 
    def eventos(self):
        pass

    def salir(self, event):
        self.Close()
        
    def cargarImg(self, img):
        ''' Recibe img como Bitmap. ''' 
        self.bitmap_1.SetBitmap(img)
        self.SetSize(self.bitmap_1.GetSizeTuple())
        self.Center()
        ImgActual.SetImagenActual(EngineGlobal.bitmapToPil( img ))
        
    def mostrarFiltro(self, imagen, umbral=False):
        ''' Resibe imagen en Bitmap. '''
        ImagenPopUp( imagen, umbral ).Show()


# end of class FrameVisor

####################
# Imagen de filtro #
####################
class ImagenPopUp(wx.Frame):
    def __init__(self, img, slider=False):
        '''
        img=imagen en bitmap que se mostrará en una ventana aparte.
        '''
        wx.Frame.__init__(self, wx.GetApp().TopWindow,
                           title="imagen  -  MWAHAHAHA!!", 
                           style=wx.DEFAULT_FRAME_STYLE)

        
        self.bitmap_1 = wx.StaticBitmap(self, -1 , img)
        x,y = self.bitmap_1.GetSizeTuple()
        self.SetMinSize( (x,y+70) )
        self.Center()
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.bitmap_1, 0, 0, 0)
        #Si se pide el slider, se pone
        if slider:
            self.slid= wx.Slider(self, -1, 0, 0, 255)
            sizer_1.Add(self.slid, 0, wx.EXPAND, 0)
            self._eventos()
        
        self.__barra_de_menu()
        self.SetSizer(sizer_1)
        self.Layout()
        
    def __barra_de_menu(self):
        # Menu Bar
        self.frame_del_visor_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        save = wxglade_tmp_menu.Append(wx.NewId(), "Guardar", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.saveImagen, save)
        load = wxglade_tmp_menu.Append(wx.NewId(), "Cargar como imagen principal", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.loadImgPrincipal, load)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Archivo")

        self.SetMenuBar(self.frame_del_visor_menubar)
        # Menu Bar end    
    
    def _eventos(self):
        self.slid.Bind(wx.EVT_COMMAND_SCROLL, self._umbral)
        
    def _umbral(self, event):
        '''
        Hace los cambios en la imagen, devuelve un bitmap, y lo actualiza.
        '''
        self.bitmap_1.SetBitmap( EnginePDI2.umbral( self.slid.GetValue() )  )
        
    def saveImagen(self,event):        
        dlg = wx.FileDialog(None, message="Guarde la imagen",
                        defaultDir=os.getcwd(), defaultFile="",
                        style=wx.SAVE | wx.CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            EngineGlobal.bitmapToPil( self.bitmap_1.GetBitmap() ).save( unicode( path.replace('\\','/')  )  )
            dlg.Destroy()
    
    def loadImgPrincipal(self, event):
        '''Carga la imagen de esta ventana como principal, y luego cierra esta. ''' 
        wx.GetApp().TopWindow.cargarImg( self.bitmap_1.GetBitmap() )#EngineGlobal.pilToBitmap(self.img_PIL) )
        self.Close()



######################
# Ventana Histograma #
######################
class HistFrame(wx.Frame):
    def __init__(self, img):
        '''
        img=imagen en PIL que se mostrará en una ventana aparte.
        '''
        wx.Frame.__init__(self, wx.GetApp().TopWindow,
                           title="Histograma  -  MWAHAHAHA!!", 
                           style=wx.DEFAULT_FRAME_STYLE)
        
        #(self.imgHist, self.histCV) = VisorEngine.imhist(img)
        self.imgHist = wx.StaticBitmap(self, -1, wx.Bitmap("/home/erunamo/yes.jpg", wx.BITMAP_TYPE_ANY))
        
        self.__lateral()
        self.__menus()
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __lateral(self):
        self.label_1 = wx.StaticText(self, -1, "Propiedades del Histograma", style=wx.ALIGN_RIGHT)
        self.panel_1 = wx.Panel(self, -1)
        self.label_2 = wx.StaticText(self, -1, u"Máximo", style=wx.ALIGN_CENTRE)
        self.maximo = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.label_3 = wx.StaticText(self, -1, "Minimo")
        self.minimo = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.label_4 = wx.StaticText(self, -1, "Media")
        self.media = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.label_5 = wx.StaticText(self, -1, u"Desviación estandar")
        self.desvEstandar = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        
    def __menus(self):
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Salir", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Menu")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        
    def __set_properties(self):
        #Datos del histograma aquí se modifican
        self.maximo.SetValue('01')
        self.minimo.SetValue('02')
        self.media.SetValue('03')
        self.desvEstandar.SetValue('04')
        
    def __do_layout(self):
        # begin wxGlade: HistFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        sizer_2.Add(self.imgHist, 0, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

#=================================================================     
