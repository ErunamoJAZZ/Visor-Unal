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
        self.guardar = wx.Button(self.panel_imagen1, -1, "Guardar como...")
        self.cerrar = wx.Button(self.panel_imagen1, -1, "cerrar")
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
        self.SetSize((400, 500))
        self.SetMinSize((400,500))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_para_img = wx.BoxSizer(wx.HORIZONTAL)
        sizer_para_img.Add(self.bitmap_1, 0, 0, 0)
        self.panel_para_img.SetSizer(sizer_para_img)
        sizer_2.Add(self.panel_para_img, 10, wx.EXPAND, 0)
        sizer_3.Add(self.guardar, 0, 0, 0)
        sizer_3.Add(self.cerrar, 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.panel_imagen1.SetSizer(sizer_2)
        self.notebook_imagenes.AddPage(self.panel_imagen1, "tab1")
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
        
    def mostrarFiltro(self, imagen):
        ImagenPopUp( imagen ).Show()


# end of class FrameVisor

####################
# Imagen de filtro #
####################
class ImagenPopUp(wx.Frame):
    def __init__(self, img):
        '''
        img=imagen en bitmap que se mostrará en una ventana aparte.
        '''
        wx.Frame.__init__(self, wx.GetApp().TopWindow,
                           title="imagen  -  MWAHAHAHA!!", 
                           style=wx.DEFAULT_FRAME_STYLE)

        self.bitmap_1 = wx.StaticBitmap(self, -1 , img)
        self.SetMinSize( self.bitmap_1.GetSizeTuple() )
        self.Center()
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.bitmap_1, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        

