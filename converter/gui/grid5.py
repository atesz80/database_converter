import wx, wx.grid as grd

TABLE = []

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, 0, "Database Converter", size=(600,500))
        self.CentreOnScreen()
        self.panel = MyPanel(self)
        self.grid = MyGrid(self.panel, tables=['test', 'test1'])

        self.save_button = MyButton(self.panel, label='Mentés')
        self.save_button.Bind(wx.EVT_BUTTON, self.SaveOnClicked)


        self.close_button = MyButton(self.panel, label='Bezárás')
        self.close_button.Bind(wx.EVT_BUTTON, self.CloseOnClicked)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        sizer.Add(self.save_button, 1, wx.EXPAND)
        sizer.Add(self.close_button, 1, wx.ALIGN_CENTER_HORIZONTAL)

        self.panel.SetSizer(sizer)
    
    def SaveOnClicked(self, event):
        clicked = event.GetEventObject()
        if TABLE == []: 
            popup = Popup(title='Hiba', label='Hibaüzenet')
            popup.Show()

    def CloseOnClicked(self, event):
        self.Close()


class MyButton(wx.Button): 
    def __init__(self, parent, label:str):
        super(MyButton, self).__init__(parent, label=label)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)    


class Popup(wx.Frame):
    def __init__(self, title, label):
           
        """Constructor"""

        self.frame = wx.Frame.__init__(self, None, title=title, size=(200,100))
        self.panel = wx.Panel(self)
        wx.StaticText(self.panel, label=label)
        self.button = MyButton(self.panel, label='Bezár')
        self.button.Bind(wx.EVT_BUTTON, self.OnClicked)

    
    def OnClicked(self, event):
        self.Close()

class MyGrid(grd.Grid):
    def __init__(self, parent, tables: list):
        grd.Grid.__init__(self, parent, 0, size=(600,425))
        self.tables = tables
        self.total_rows = len(self.tables) + 2
        self.CreateGrid(self.total_rows,2)
        self.RowLabelSize = 0
        self.ColLabelSize = 20

        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)

        # Table Headers

        self.SetColLabelSize(0)
        self.SetColSize(0, 500)

        self.SetCellSize(0, 0, 1, 2)
        self.SetCellValue(0, 0, "Tables")

        self.SetCellValue(1, 0, "Table")
        self.SetCellValue(1, 1, "Check")

        attr = grd.GridCellAttr()
        attr.SetEditor(grd.GridCellBoolEditor())
        attr.SetRenderer(grd.GridCellBoolRenderer())
        self.SetColAttr(1,attr)
        self.SetColSize(1,100)
        #attr.SetReadOnly(True)

        for index, table in enumerate(tables):
            print(table)
            self.SetCellValue(index + 2, 0, table)

        self.Bind(grd.EVT_GRID_CELL_LEFT_CLICK,self.onMouse)
        self.Bind(grd.EVT_GRID_SELECT_CELL,self.onCellSelected)
        self.Bind(grd.EVT_GRID_EDITOR_CREATED, self.onEditorCreated)

        self.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        self.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )


        # sizer.Add(self.myGrid2, 1, wx.TOP|wx.ALIGN_CENTRE, 2)
        # sizer.Add(button_refresh, 1, wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTRE, 50)

        # self.panel.SetSizer(sizer)
        # self.panel.SetSize((500,400))
        # self.SetSize((500,400))
        # self.panel.Layout()
                
        # button = MyButton(self, label='Mentés', pos=wx.Point(20, 40))
        # button.Bind(wx.EVT_BUTTON, self.OnClicked)

    def onKeyDown(self,evt):
        if evt.KeyCode == wx.WXK_UP:
            if self.GridCursorRow > 0:
                self.DisableCellEditControl()
                self.MoveCursorUp(False)
        elif evt.KeyCode == wx.WXK_DOWN:
            if self.GridCursorRow < (self.NumberRows-1):
                self.DisableCellEditControl()
                self.MoveCursorDown(False)
        elif evt.KeyCode == wx.WXK_LEFT:
            if self.GridCursorCol > 0:
                self.DisableCellEditControl()
                self.MoveCursorLeft(False)
        elif evt.KeyCode == wx.WXK_RIGHT:
            if self.GridCursorCol < (self.NumberCols-1):
                self.DisableCellEditControl()
                self.MoveCursorRight(False)
        else:
            evt.Skip()

    def onMouse(self, evt: grd.GridEvent):
        if evt.Col == 1:
            wx.CallLater(100,self.toggleCheckBox)
        evt.Skip()

    def toggleCheckBox(self):
        self.cb.Value = not self.cb.Value
        self.afterCheckBox(self.cb.Value)

    def onCellSelected(self, evt: grd.GridEvent):
        if evt.Col == 1:
            wx.CallAfter(self.EnableCellEditControl)
        evt.Skip()

    def onEditorCreated(self, evt: grd.GridEvent):
        if evt.Col == 1:
            self.cb = evt.Control
            self.cb.WindowStyle |= wx.WANTS_CHARS
            self.cb.Bind(wx.EVT_KEY_DOWN,self.onKeyDown)
            self.cb.Bind(wx.EVT_CHECKBOX,self.onCheckBox)
        evt.Skip()

    def onCheckBox(self,evt):
        self.afterCheckBox(evt.IsChecked())

    def afterCheckBox(self, isChecked):
        if isChecked:
            TABLE.append(self.GetCellValue(self.GridCursorRow, 0))
        
        else:
            TABLE.remove(self.GetCellValue(self.GridCursorRow, 0))

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        #self.SetTopWindow(frame)
        return True

MyApp(0).MainLoop()