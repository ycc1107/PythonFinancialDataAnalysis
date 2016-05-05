# main panel
# cheng.yan

import wx
import wx.grid as gridlib

class RandomPanel(wx.Panel):
    def __init__(self, parent, color):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(color)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        topSplitter = wx.SplitterWindow(self)
        hSplitter = wx.SplitterWindow(topSplitter)

        panelOne = RandomPanel(hSplitter, "blue")
        panelTwo = RandomPanel(hSplitter, "red")
        self.createDataGrid(panelOne)

        hSplitter.SplitVertically(panelOne, panelTwo)
        hSplitter.SetSashGravity(0.2)

        panelThree = RandomPanel(topSplitter, "green")
        topSplitter.SplitHorizontally(hSplitter, panelThree)
        topSplitter.SetSashGravity(0.5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSplitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def createDataGrid(self, midPanel):
        dataGrid = gridlib.Grid(midPanel)
        dataGrid.CreateGrid(12,8)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(dataGrid, 1, wx.EXPAND)
        midPanel.SetSizer(sizer)



class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='OPTION TRADING/BACKTESTING SYSTEM',
                          size=(1000,800),
                          style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        panel = MainPanel(self)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()