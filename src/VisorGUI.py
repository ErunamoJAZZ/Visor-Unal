'''
Created on 24/02/2011

@author: Carlos Daniel Sanchez Ramirez <ErunamoJAZZ>
@web: https://github.com/ErunamoJAZZ/Visor-Unal
'''
import wx

class FrameVisor(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameVisor.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.tab_imagenes = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.notebook_1_pane_1 = wx.Panel(self.tab_imagenes, -1)
        self.panel_Imagen = wx.Panel(self.notebook_1_pane_1, -1)
        self.button_guadar_imagen = wx.Button(self.notebook_1_pane_1, -1, "Guardar como...")
        self.button_cerrar_imagen = wx.Button(self.notebook_1_pane_1, -1, "Cerrar")
        
        self.__barra_de_menu()
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameVisor.__set_properties
        self.SetTitle("Visor - Carlos Daniel Sanchez Ramirez")
        self.SetSize((400, 500))
        self.SetMinSize((400,500))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameVisor.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.panel_Imagen, 13, wx.EXPAND, 5)
        sizer_3.Add(self.button_guadar_imagen, 0, 0, 36)
        sizer_3.Add(self.button_cerrar_imagen, 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_2)
        self.tab_imagenes.AddPage(self.notebook_1_pane_1, "tab1")
        sizer_1.Add(self.tab_imagenes, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
        
    def __barra_de_menu(self):
                # Menu Bar
        self.frame_del_visor_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        abrir = wxglade_tmp_menu.Append(wx.NewId(), "Abrir", "", wx.ITEM_NORMAL)
        
        salir = wxglade_tmp_menu.Append(wx.NewId(), "Salir", "", wx.ITEM_NORMAL)
        
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Archivo")
        
        wxglade_tmp_menu = wx.Menu()
        gris = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> Grises", "", wx.ITEM_NORMAL)
        
        r = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> R", "", wx.ITEM_NORMAL)
        
        g = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> G", "", wx.ITEM_NORMAL)
        
        b = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> B", "", wx.ITEM_NORMAL)
        
        hsi = wxglade_tmp_menu.Append(wx.NewId(), "RGB -> HSI", "", wx.ITEM_NORMAL)
        
        rgb = wxglade_tmp_menu.Append(wx.NewId(), "HSI -> RGB", "", wx.ITEM_NORMAL)
        
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "Filtros")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Acerca de...", "", wx.ITEM_NORMAL)
        self.frame_del_visor_menubar.Append(wxglade_tmp_menu, "...")
        self.SetMenuBar(self.frame_del_visor_menubar)
        # Menu Bar end

        
        

# end of class FrameVisor