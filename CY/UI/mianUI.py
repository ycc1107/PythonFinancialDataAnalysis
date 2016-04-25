# main panel
# cheng.yan

import wx

class UIMain(wx.Frame):
    def __init__(self, parent,id):
        wx.Frame.__init__(self,parent,id,'Main',size = (1000,600))
        panel = wx.Panel(self)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = UIMain(parent = None, id = -1)
    frame.Show()
    app.MainLoop()