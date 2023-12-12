import wx, wx.grid as grd
from converter import Converter
from db import query

global table
table = []


class MyFrame(wx.Frame):

    """ Az alkalmazás ablakának implementálása """

    def __init__(self, parent):

        """ Konstruktor """

        wx.Frame.__init__(self, parent, 0, "Database Converter", size=(600,500))
        self.CentreOnScreen()
        self.panel = MyPanel(self)
        
        oQuery = query.Queries()
        self.grid = MyGrid(self.panel, tables=oQuery.get_tablenames())

        self.save_button = MyButton(self.panel, label='Save')
        self.save_button.Bind(wx.EVT_BUTTON, self.SaveOnClicked)

        self.close_button = MyButton(self.panel, label='Close')
        self.close_button.Bind(wx.EVT_BUTTON, self.CloseOnClicked)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        sizer.Add(self.save_button, 1, wx.EXPAND)
        sizer.Add(self.close_button, 1, wx.ALIGN_CENTER_HORIZONTAL)

        self.panel.SetSizer(sizer)
    
    def SaveOnClicked(self, event):

        """ A Mentés gomb eseménykezelő metódusa """

        if table == []: 
            popup = MyPopup(title='Error', label='Please, choose one at least!')
            popup.Show()

        else:
            oConverter = Converter(tables=table)
            oConverter.converter()

    def CloseOnClicked(self, event):

        """ A Bezárás gomb eseménykezelő metódusa """

        self.Close()

class MyPopup(wx.Frame):

    """ Felugró ablak osztálya hibaüzenethez """

    def __init__(self, title, label):
           
        """ Konstructor """

        self.frame = wx.Frame.__init__(self, None, title=title, size=(200,100))
        self.panel = MyPanel(self)
        self.error_message = wx.StaticText(self.panel, label=label, pos=wx.Point(15, 20))

        self.close_button = wx.Button(self.panel, label='Close', pos=wx.Point(50, 50))
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClicked)


    def OnClicked(self, event):

        """ Bezárás gomb eseménykezelő metódusa """

        self.Close()


class MyButton(wx.Button):

    """ Gomb osztálya """

    def __init__(self, parent, label:str):

        """ Konstruktor """

        super(MyButton, self).__init__(parent, label=label)


class MyPanel(wx.Panel):

    """ Panel osztálya """

    def __init__(self, parent):

        """ Konstruktor """

        super(MyPanel, self).__init__(parent)    


class MyGrid(grd.Grid):

    """ A táblázat osztálya az adatbázis táblák listázásához. """

    def __init__(self, parent, tables: list) -> None:

        """ Konstruktor """

        grd.Grid.__init__(self, parent, 0, size=(600,425))

        self.tables = tables
        self.total_rows = len(self.tables) + 1
        self.CreateGrid(self.total_rows, 2)
        self.RowLabelSize = 0
        self.ColLabelSize = 20

        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)

        self.SetColLabelSize(0)
        self.SetColSize(0, 500)

        self.SetCellSize(0, 0, 1, 2)
        self.SetCellValue(0, 0, "Tables")

        attr_header= grd.GridCellAttr()
        self.SetRowAttr(0,attr_header)
        attr_header.SetReadOnly(True)

        attr_table_column= grd.GridCellAttr()
        self.SetColAttr(0,attr_table_column)
        attr_table_column.SetReadOnly(True)

        attr_checkbox_column = grd.GridCellAttr()
        attr_checkbox_column.SetEditor(grd.GridCellBoolEditor())
        attr_checkbox_column.SetRenderer(grd.GridCellBoolRenderer())
        self.SetColAttr(1, attr_checkbox_column)
        self.SetColSize(1,100)

        for index, table in enumerate(tables):
            self.SetCellValue(index + 1, 0, table)

        self.Bind(grd.EVT_GRID_CELL_LEFT_CLICK,self.onMouse)
        self.Bind(grd.EVT_GRID_SELECT_CELL,self.onCellSelected)
        self.Bind(grd.EVT_GRID_EDITOR_CREATED, self.onEditorCreated)

        self.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        self.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

    def onMouse(self, evt: grd.GridEvent) -> None:

        """ Egéresemény eseménykezelő metódusa """

        if evt.Col == 1:
            wx.CallLater(100,self.toggleCheckBox)

        evt.Skip()

    def toggleCheckBox(self) -> None:

        """ Checkbox állapotának változtatásához """

        self.cb.Value = not self.cb.Value
        self.afterCheckBox(self.cb.Value)

    def onCellSelected(self, evt: grd.GridEvent) -> None:

        """ Cella kijelölés kezelése """

        if evt.Col == 1:
            wx.CallAfter(self.EnableCellEditControl)

        evt.Skip()

    def onEditorCreated(self, evt: grd.GridEvent) -> None:

        """ Checkbox megjelenítéséhez """

        if evt.Col == 1:
            self.cb = evt.Control
            self.cb.WindowStyle |= wx.WANTS_CHARS
            self.cb.Bind(wx.EVT_CHECKBOX,self.onCheckBox)

        evt.Skip()

    def onCheckBox(self, evt: grd.GridEvent) -> None:

        """ Checkbox eseménykezelő metódusa """

        self.afterCheckBox(evt.IsChecked())

    def afterCheckBox(self, isChecked: bool) -> None:

        """ A metódus a checkbox állapotának vizsgálatához """

        if isChecked:
            table.append(self.GetCellValue(self.GridCursorRow, 0))
        
        else:
            table.remove(self.GetCellValue(self.GridCursorRow, 0))

class MyApp(wx.App):

    """ Az osztály felhasználói felület inicializálásához szükséges. """

    def OnInit(self):

        """ A metódus az inicializáláshoz """

        frame = MyFrame(None)
        frame.Show(True)
        return True