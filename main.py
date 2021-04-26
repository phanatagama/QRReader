import QRReader,wx
from PIL import Image
from pyzbar.pyzbar import decode

class Reader(QRReader.MyFrame):
	"""docstring for Reader"""
	def __init__(self, arg):
		QRReader.MyFrame.__init__(self,None)
		icon = wx.EmptyIcon()
		icon.CopyFromBitmap(wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_FRAME_ICON ))
		self.SetIcon(icon)

	def imageResizer(self,pathfile):
		self.maxsize = 200
		img = wx.Image(pathfile,wx.BITMAP_TYPE_ANY)

		# Scale rasio gambar
		W = img.GetWidth()
		H = img.GetHeight()
		if W>H:
			NewW = self.maxsize
			NewH = self.maxsize * H / W
		else:
			NewH = self.maxsize
			NewW = self.maxsize * W / H
		return img.Scale(NewW,NewH)

	def btnOpenOnToolClicked( self, event ):
		with wx.FileDialog(self, "Open img file", wildcard="IMG files (*.JPG;*.JPEG;*.PNG;*.BMP)|*.JPG;*.JPEG;*.PNG;*.BMP", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return

			self.clearMode(event)
			pathname = fileDialog.GetPath()
			self.m_statusBar1.SetStatusText(pathname)
			self.pathfile = pathname
			try:
				self.m_bitmap1.SetBitmap(wx.BitmapFromImage(self.imageResizer(self.pathfile)))
			except Exception as e:
				self.m_richText1.SetValue(str(e))
		event.Skip()

	def decodeClick(self,event):
		try:
			message = decode(Image.open(self.pathfile))[0][0].decode('utf-8')
			self.c_pesan.SetValue(message)
			self.m_richText1.SetValue('Decode Successfull!!!')
		except Exception as e:
			self.m_richText1.SetValue("Failed, please input a valid image\n"+str(e))

	def onCopy(self, event):
		clipdata = wx.TextDataObject()
		clipdata.SetText(self.c_pesan.GetValue())
		wx.TheClipboard.Open()
		wx.TheClipboard.SetData(clipdata)
		wx.TheClipboard.Close()

	def clearMode(self, event):
		self.c_pesan.SetValue('')
		self.m_richText1.SetValue('')
		self.m_statusBar1.SetStatusText('')
		self.pathfile = None
		self.m_bitmap1.SetBitmap(wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ))

	def onAbout(self,event):
		wx.MessageDialog(None, "Created by Cahyadi Setia Phanatagama",'About Us', wx.OK|wx.ICON_INFORMATION).ShowModal()

	def onExit(self,event):
		exit()

app = wx.App(False)
frame = Reader(None)
frame.Show(True)
app.MainLoop()