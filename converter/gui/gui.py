import wx

class MyFrame(wx.Frame):

    def __init__(self, parent:wx.Window, title: str, size: wx.Size = (600, 400)):
        super(MyFrame, self).__init__(parent, title=title, size=size)
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
            super(MyPanel, self).__init__(parent)

            # gridsizer = wx.GridSizer(4, 2, 2, 2)
            # for i in range(1, 8):
            #      gridsizer.Add((wx.CheckBox(self)), 0, wx.EXPAND)
            #      self.SetSizer(gridsizer)


            text = MyStaticText(self, label = 'Text', pos=wx.Point(250, 10))

            gridsizer = MyGridSizer(rows=2)
            text = MyStaticText(self, label = 'Text', pos=wx.Point(250, 10))
            checkbox = MyCheckBox(self, label = '', name = 'Text')
            checkbox.Bind(wx.EVT_CHECKBOX, self.OnChecked)
            print(checkbox)
            gridsizer.Add(checkbox, 0)
            gridsizer.Add(text, 0)
            self.SetSizer(gridsizer)
            button = MyButton(self, label='Mentés', pos=wx.Point(20, 30))
            button.Bind(wx.EVT_BUTTON, self.OnClicked)



    def OnChecked(self, event):
        clicked = event.GetEventObject()
        print(clicked.GetName())
        print(event.IsChecked())

    
    def OnClicked(self, event):
        clicked = event.GetEventObject()
        print('Clicked')


class MyGridSizer(wx.GridSizer):
    def __init__(self, rows:int, cols:int = 2, vgap:int = 2, hgap:int = 2)->None:
        super(MyGridSizer, self).__init__(rows=rows, cols=cols, vgap=vgap, hgap=hgap)

class MyCheckBox(wx.CheckBox): 
    def __init__(self, parent, label, name):
        super(MyCheckBox, self).__init__(parent, label=label, name=name)

class MyStaticText(wx.StaticText): 
    def __init__(self, parent, label:str, pos:wx.Point):
        super(MyStaticText, self).__init__(parent, label=label, pos=pos)

class MyButton(wx.Button): 
    def __init__(self, parent, label:str, pos:wx.Point):
        super(MyButton, self).__init__(parent, label=label, pos=pos)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title='Database Converter')
        self.frame.Show()

        return True