import wx
app = wx.App()
win = wx.Frame(None,title='simple app')
loadButton = wx.Button(win, label='Open')
saveButton = wx.Button(win, label='Save')

win.Show()
app.MainLoop()
