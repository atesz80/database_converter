import sys
import wx
import wx.lib.agw.ultimatelistctrl as ULC


class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Checkbox grid based on UltimateListCtrl Demo", size=(600,300))
        agwStyle = (ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | wx.LC_REPORT | wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL)
        self.mylist = mylist = ULC.UltimateListCtrl(self, wx.ID_ANY, agwStyle=agwStyle)

        mylist.InsertColumn(0,"", width=100)

        for col in range(1,25):
            col_num=str(col-1)
            if col==0:col_num=""
            mylist.InsertColumn(col,col_num, width=20)


        self.checkboxes = {}
        self.boxes=[]

        for day in range(7):
#            days=["Monday", "Sunday", "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday"]
            days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            mylist.InsertStringItem(day, str(days[day]))
            #index = mylist.InsertStringItem(1, "" + days[day])
            #mylist.SetStringItem(index, 1, "")


        for boxes in range(1,25):
            for index in range(7):
                day = days[index]
                hour = boxes-1
                name_of_checkbox = "{day}_{hour}".format(day=day, hour=hour)
                mylist.SetStringItem(index, boxes, "")
                self.checkBox = wx.CheckBox(mylist, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0,name=name_of_checkbox)
                #self.checkBox.SetValue(True) #Use this to check all boxes
                self.checkboxes[self.checkBox.GetId()] = index
                mylist.SetItemWindow(index, boxes, self.checkBox)
                self.boxes.append(self.checkBox)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mylist, 1, wx.EXPAND)
        button = wx.Button(self,-1,"Retrieve Data")
        sizer.Add(button)
        self.Bind(wx.EVT_CHECKBOX, self.OnChecked)
        self.Bind(wx.EVT_BUTTON, self.OnGetData)
        self.SetSizer(sizer)

    def OnChecked(self,event):
        clicked = event.GetEventObject()
        print (clicked.GetName())
        print (event.IsChecked())

    def OnGetData(self,event):
        day_dict = {}
        day_list = []
        for i in self.boxes:
            if i.IsChecked():
                n = i.GetName()
                day_dict[n]="Checked"
                day_list.append((n,"Checked"))
        print (day_dict)
        print (day_list)



app = wx.App()
frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()
app.MainLoop()