# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QReader.exe", pos = wx.DefaultPosition, size = wx.Size( 500,280 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,280 ), wx.Size( 500,280 ) )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORZ_TEXT )
		self.m_tool2 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Open Image", wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_BUTTON ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Open Image", None )

		self.m_tool3 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Exit", wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_BUTTON ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Exit Program", None )

		self.m_tool4 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"About Us", wx.ArtProvider.GetBitmap( wx.ART_INFORMATION, wx.ART_BUTTON ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"About", None )

		self.m_toolBar1.Realize()

		bSizer2.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.Size( 200,200 ), 0 )
		self.m_bitmap1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_bitmap1.SetMinSize( wx.Size( 200,200 ) )
		self.m_bitmap1.SetMaxSize( wx.Size( 200,200 ) )

		fgSizer3.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		fgSizer4 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer4.SetMinSize( wx.Size( 280,-1 ) )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Log" ), wx.VERTICAL )

		sbSizer3.SetMinSize( wx.Size( 280,50 ) )
		self.m_richText1 = wx.richtext.RichTextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText1.SetMinSize( wx.Size( -1,50 ) )

		sbSizer3.Add( self.m_richText1, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( sbSizer3, 0, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Message" ), wx.VERTICAL )

		self.c_pesan = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.c_pesan, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button20 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Copy Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button20, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( sbSizer4, 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"DECODE", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button21.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_FRAME_ICON ) )
		gSizer2.Add( self.m_button21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button22.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_FRAME_ICON ) )
		gSizer2.Add( self.m_button22, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )


		fgSizer3.Add( fgSizer4, 0, 0, 5 )


		bSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.btnOpenOnToolClicked, id = self.m_tool2.GetId() )
		self.Bind( wx.EVT_TOOL, self.onExit, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.onAbout, id = self.m_tool4.GetId() )
		self.m_button20.Bind( wx.EVT_BUTTON, self.onCopy )
		self.m_button21.Bind( wx.EVT_BUTTON, self.decodeClick )
		self.m_button22.Bind( wx.EVT_BUTTON, self.clearMode )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnOpenOnToolClicked( self, event ):
		event.Skip()

	def onExit( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()

	def onCopy( self, event ):
		event.Skip()

	def decodeClick( self, event ):
		event.Skip()

	def clearMode( self, event ):
		event.Skip()


