#!/usr/bin/env python
#coding: utf-8

import pygtk
pygtk.require('2.0')
import gtk
import urllib,socket,time,threading,gobject,os
import libs.http
import modules.sites.sites
gobject.threads_init()
class updateWidgit(threading.Thread):
	def __init__(self, widget,data=None,):
		super(updateWidgit, self).__init__()
		self.widget = widget
		self.data = data
	def run(self):
		self.updateItem()

		self.showMessage('Find finshed!')
	def updateItem(self):
		siteDm = modules.sites.sites.sites(self.data,self.updateSiteDoamin)
		siteDm.getSameIpSites()

	 
	def updateSiteDoamin(self,url):
		self.widget.append([str(url),''])
 		# gobject.idle_add(self.widget.insert_at_cursor,'\n')

 	def showMessage(self,msg):
 		os.system('notify-send "Notify:" "%s"'%msg)

	def __del__(self):
		pass
class mainApp():
	def __init__(self):

		self.builder = gtk.Builder()
		self.builder.add_from_file('ui/main.glade')
		self.builder.connect_signals(self)
		self.win = self.builder.get_object('window_main')
		self.win.set_resizable(False)
		self.win.show()
		self.init_domain()
		
	def init_domain(self):
		self.list_view = self.builder.get_object('list_view')
		self.viewcolumnUrl = gtk.TreeViewColumn('地址',gtk.CellRendererText(),text=0)
		self.viewcolumnUrl.set_min_width(250)
		self.viewcolumnTitle = gtk.TreeViewColumn('标题',gtk.CellRendererText(),text=1)
		self.listStore = gtk.ListStore(str,str)
		self.list_view.set_model(self.listStore)
		self.list_view.append_column(self.viewcolumnUrl)
		self.list_view.append_column(self.viewcolumnTitle)

	#btn find event
	def btn_find_clicked_event(self,widget,data=None):
		self.listStore.clear()
		self.txt_url = self.builder.get_object('txt_url')
		url = self.txt_url.get_text()
		upTd = updateWidgit(self.listStore,url)
		upTd.start()

	def gtk_main_quit(self,widget,data=None):
		gtk.main_quit()

	#start with here
	def run(self):
		gtk.main()
		
def main():
	app = mainApp()
	app.run()

if __name__ == '__main__':
	main()
