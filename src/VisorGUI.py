# -*- encoding: utf-8 -*-
'''
Created on 24/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''
import wx
import VisorEngine


class FrameVisor(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_imagenes = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.panel_imagen1 = wx.Panel(self.notebook_imagenes, -1)
        self.panel_para_img = wx.Panel(self.panel_imagen1, -1)
        self.bitmap_1 = wx.StaticBitmap(self.panel_para_img, -1)
        VisorEngine.loadAll(self)
        
        # Menu Bar
        self.__barra_de_menu()
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxFrame.__set_properties
        self.SetTitle("Visor - Carlos Daniel Sanchez Ramirez")
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
        self.Bind(wx.EVT_MENU, VisorEngine.openImage, abrir)
        salir = wxglade_tmp_menu.Append(wx.NewId(), "Salir", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.salir, salir)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Archivo")
        
        wxglade_tmp_menu = wx.Menu()
        gris = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> Grises", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.rgb2grises, gris)
        r = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> R", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.rgb2r, r)
        g = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> G", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.rgb2g, g)
        b = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> B", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.rgb2b, b)
        hsi = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> HSI", "", wx.ITEM_NORMAL)
        
        rgb = wxglade_tmp_menu.Append(wx.NewId(), "HSI -> RGB", "", wx.ITEM_NORMAL)
        
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros")
        
        wxglade_tmp_menu = wx.Menu()
        invertir = wxglade_tmp_menu.Append(wx.NewId(), "Invertit grises", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.invertir, invertir)
        umbral = wxglade_tmp_menu.Append(wx.NewId(), "Umbral", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.init_umbral, umbral)
        umbral_bin = wxglade_tmp_menu.Append(wx.NewId(), "Umbral binario", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.init_umbral_bin, umbral_bin)
        sum = wxglade_tmp_menu.Append(wx.NewId(), "Suma/resta", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.suma, sum)
        mult = wxglade_tmp_menu.Append(wx.NewId(), u"Multiplicación/División", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VisorEngine.multipli, mult)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros 2")
        
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
        self.bitmap_1.SetBitmap(img)
        self.SetSize(self.bitmap_1.GetSizeTuple())
        self.Center()
        
    def mostrarFiltro(self, imagen, umbral=False):
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
        self.Bind(wx.EVT_MENU, VisorEngine.saveImagen, save)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Archivo")

        self.SetMenuBar(self.frame_del_visor_menubar)
        # Menu Bar end    
    
    def _eventos(self):
        self.slid.Bind(wx.EVT_COMMAND_SCROLL, self._umbral)
        
    def _umbral(self, event):
        '''
        Hace los cambios en la imagen, devuelve un bitmap, y lo actualiza.
        '''
        self.bitmap_1.SetBitmap( VisorEngine.umbral( self.slid.GetValue() )  )
        
    def saveImagen(self,event):
        self.bitmap_1
        
        
