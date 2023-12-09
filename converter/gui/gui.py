import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
            super(MyPanel, self).__init__(parent)

            # gridsizer = wx.GridSizer(4, 2, 2, 2)
            # for i in range(1, 8):
            #      gridsizer.Add((wx.CheckBox(self)), 0, wx.EXPAND)
            #      self.SetSizer(gridsizer)

            gridsizer = MyGridSizer(rows=2)
            text = MyStaticText(self, label = 'Text')
            checkbox = MyCheckBox(self, label = '', name = 'Text')
            checkbox.Bind(wx.EVT_CHECKBOX, self.OnChecked)
            print(checkbox)
            gridsizer.Add(checkbox, 0)
            gridsizer.Add(text, 0)
            self.SetSizer(gridsizer)

    def OnChecked(self,event):
        clicked = event.GetEventObject()
        print(clicked.GetName())
        print(event.IsChecked())


class MyGridSizer(wx.GridSizer):
    def __init__(self, rows:int, cols:int = 2, vgap:int = 2, hgap:int = 2)->None:
        super(MyGridSizer, self).__init__(rows=rows, cols=cols, vgap=vgap, hgap=hgap)

class MyCheckBox(wx.CheckBox): 
    def __init__(self, parent, label, name):
        super(MyCheckBox, self).__init__(parent, label=label, name=name)

class MyStaticText(wx.StaticText): 
    def __init__(self, parent, label:str):
        super(MyStaticText, self).__init__(parent, label=label)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title='Database Converter')
        self.frame.Show()

        return True