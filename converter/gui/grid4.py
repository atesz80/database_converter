import wx
import wx.grid as gridlib

class MyForm(wx.Frame):

    def __init__(self)->None:

        """ Konstructor """

        wx.Frame.__init__(self, parent=None, title="Database Converter")
        self.panel = wx.Panel(self)

        # button_refresh = wx.Button(self.panel, id=wx.ID_ANY, label='Refresh')
        # button_refresh.Bind(wx.EVT_BUTTON, self.refresh)

        self.myGrid = gridlib.Grid(self.panel)
        self.myGrid.CreateGrid(3, 3)

        self.myGrid.SetRowLabelSize(0)
        self.myGrid.SetColLabelSize(0)

        # Table Headers

        self.myGrid.SetColLabelSize(0)
        self.myGrid.SetCellSize(0, 0, 1, 3)
        self.myGrid.SetCellValue(0, 0, "Tables")

        self.myGrid.SetCellValue(1, 0, "#")
        self.myGrid.SetCellValue(1, 1, "Table")
        self.myGrid.SetCellValue(1, 2, "Check")

        attr = gridlib.GridCellAttr()
        attr.SetReadOnly(True)
        for i in range(2, total_rows, 1):
        
            # Table Content

            self.myGrid.SetCellValue(i, 0, f"{i-1}")
            self.myGrid.SetCellValue(i, 1, "users")

            # Checkbox

            crbool = wx.grid.GridCellBoolRenderer()
            cebool = wx.grid.GridCellBoolEditor()
            self.myGrid.SetCellRenderer(i, 2, crbool)
            self.myGrid.SetCellEditor(i, 2, cebool)
            self.SetColAttr(2,attr)
            self.SetColSize(2,20)
            self.Bind(self.myGrid.EVT_GRID_CELL_LEFT_CLICK,self.onMouse)
            self.Bind(self.myGrid.EVT_GRID_SELECT_CELL,self.onCellSelected)
            self.Bind(self.myGrid.EVT_GRID_EDITOR_CREATED, self.onEditorCreated)

            # self.myGrid.SetRowAttr(i, attr)

        # self.myGrid.SetRowLabelSize(80)
        # self.myGrid.SetRowLabelValue(0, "")
        # self.myGrid.SetRowLabelValue(1, "")
        # self.myGrid.SetRowLabelValue(2, "2")

        # for i in range(3):
        #     self.myGrid.SetColSize(i, 60)

#        self.myGrid1.SetColLabelValue(0, "")
#        self.myGrid1.SetColLabelValue(1, "Yesterday")
#        self.myGrid1.SetColLabelValue(2, "")
#        self.myGrid1.SetColLabelValue(3, "")
#        self.myGrid1.SetColLabelValue(4, "Today")
#        self.myGrid1.SetColLabelValue(5, "")

        # self.myGrid.SetColLabelSize(0)
        # self.myGrid.SetCellSize(0, 0, 1, 3)
        # self.myGrid.SetCellValue(0, 0, "Tables")

        # self.myGrid.SetCellValue(1, 0, "#")
        # self.myGrid.SetCellValue(1, 1, "Table")
        # self.myGrid.SetCellValue(1, 2, "Check")
        #self.myGrid.SetCellSize(1, 0, 1, 2)
        # self.myGrid.SetCellSize(1, 0, 3, 4)
        # self.myGrid.SetCellSize(1, 0, 5, 6)

        # self.myGrid.SetCellValue(2, 0, "1")
        # self.myGrid.SetCellValue(2, 1, "users")
        # crbool = wx.grid.GridCellBoolRenderer()
        # cebool = wx.grid.GridCellBoolEditor()
        # self.myGrid.SetCellRenderer(2, 2, crbool)
        # self.myGrid.SetCellEditor(2, 2, cebool)
        # self.myGrid.SetCellValue(2, 2, '1')


        self.myGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        self.myGrid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
        # ******************************* #

        # self.myGrid2 = gridlib.Grid(self.panel)
        # self.myGrid2.CreateGrid(2, 6)

        # for i in range(6):
        #     self.myGrid2.SetColSize(i, 60)

        # self.myGrid2.SetColLabelValue(0, "")
        # self.myGrid2.SetColLabelValue(1, "Yesterday")
        # self.myGrid2.SetColLabelValue(2, "")
        # self.myGrid2.SetColLabelValue(3, "")
        # self.myGrid2.SetColLabelValue(4, "Today")
        # self.myGrid2.SetColLabelValue(5, "")

        # self.myGrid2.SetCellValue(0, 0, "Treasury")
        # self.myGrid2.SetCellValue(0, 1, "Volatility")
        # self.myGrid2.SetCellValue(0, 2, "Cash")
        # self.myGrid2.SetCellValue(0, 3, "Treasury")
        # self.myGrid2.SetCellValue(0, 4, "Volatility")
        # self.myGrid2.SetCellValue(0, 5, "Cash")

        # self.myGrid2.SetRowLabelSize(60)
        # self.myGrid2.SetRowLabelValue(0, "")
        # self.myGrid2.SetRowLabelValue(1, "2")

        # self.myGrid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        # self.myGrid2.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
        # ****************************** #

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.myGrid, 1, wx.TOP|wx.ALIGN_CENTRE, 2)
        # sizer.Add(self.myGrid2, 1, wx.TOP|wx.ALIGN_CENTRE, 2)
        # sizer.Add(button_refresh, 1, wx.RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTRE, 50)

        self.panel.SetSizer(sizer)
        self.panel.SetSize((500,400))
        self.SetSize((500,400))
        self.panel.Layout()


    def onMouse(self,evt):
        if evt.Col == 1:
            wx.CallLater(100,self.toggleCheckBox)
        evt.Skip()

    def toggleCheckBox(self):
        self.cb.Value = not self.cb.Value
        self.afterCheckBox(self.cb.Value)

    def onCellSelected(self,evt):
        if evt.Col == 1:
            wx.CallAfter(self.EnableCellEditControl)
        evt.Skip()

    def onEditorCreated(self,evt):
        if evt.Col == 1:
            self.cb = evt.Control
            self.cb.WindowStyle |= wx.WANTS_CHARS
            self.cb.Bind(wx.EVT_KEY_DOWN,self.onKeyDown)
            self.cb.Bind(wx.EVT_CHECKBOX,self.onCheckBox)
        evt.Skip()

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

    def onCheckBox(self,evt):
        self.afterCheckBox(evt.IsChecked())

    def afterCheckBox(self,isChecked):
        print('afterCheckBox',self.GridCursorRow,isChecked)

class MyApp(wx.App):

    def __init__(self):
        super(MyApp, self).__init__()


    def OnInit(self):
        self.frame = MyForm()
        self.frame.Show()
        return True
    
if __name__ == "__main__":
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()