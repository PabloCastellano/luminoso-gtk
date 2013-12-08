#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# luminoso-gtk.py
# Copyright (C) 2013 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gi.repository import Gtk

import sys
from gtkledsgrid import GtkLedsGrid


class LuminosoGtk:
    def __init__(self, filename=None):
        self.grid = GtkLedsGrid(16, 64)
        self.ui = Gtk.Builder()
        self.ui.add_from_file('ui/mainwindow.glade')
        self.ui.connect_signals(self)

        self.ui.get_object('alignment6').add(self.grid)
        self.main_window = self.ui.get_object('mainwindow')
        self.main_window.show_all()

        if filename:
            self.grid.load_file(filename)

    def on_chooseimagebutton_activate(self, widget, data=None):
        dialog = Gtk.FileChooserDialog('Abrir imagen', self.main_window,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_filename()
            print filename

        dialog.destroy()

    def on_quitmenuitem_activate(self, widget, data=None):
        raise NotImplementedError

    def on_saveasanimationmenuite_activate(self, widget, data=None):
        raise NotImplementedError

    def on_saveanimationmenuitem_activate(self, widget, data=None):
        raise NotImplementedError

    def on_newanimationmenuitem_activate(self, widget, data=None):
        raise NotImplementedError

    def on_viewimagemenuitem_activate(self, widget, data=None):
        dialog = ViewImageDialog()
        if dialog.run() == Gtk.ResponseType.ACCEPT:
            print 'ran!'

    def on_newimagemenuitem_activate(self, widget, data=None):
        dialog = NewImageDialog()
        if dialog.run() == Gtk.ResponseType.ACCEPT:
            print 'ran!'

    def on_openanimationmenuitem_activate(self, widget, data=None):
        dialog = Gtk.FileChooserDialog('Abrir animación', self.main_window,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_filename()
            print filename

        dialog.destroy()

    def gtk_main_quit(self, widget, data=None):
        Gtk.main_quit()


class ViewImageDialog:
    def __init__(self):
        self.ui = Gtk.Builder()
        self.ui.add_from_file('ui/viewimage.glade')
        self.ui.connect_signals(self)
        self.dialog = self.ui.get_object('dialog')
        self.grid = GtkLedsGrid(16, 64)
        self.ui.get_object('alignment2').add(self.grid)
        self.dialog.show_all()

    def run(self):
        return self.dialog.run()

    def destroy(self):
        self.dialog.destroy()

    def on_chooseimagebutton_clicked(self, widget, data=None):
        dialog = Gtk.FileChooserDialog('Abrir imagen', self.dialog,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_filename()
            print filename

        dialog.destroy()


class NewImageDialog:
    def __init__(self):
        self.ui = Gtk.Builder()
        self.ui.add_from_file('ui/newimage.glade')
        self.ui.connect_signals(self)
        self.dialog = self.ui.get_object('dialog')
        self.grid = GtkLedsGrid(16, 64)
        self.ui.get_object('alignment2').add(self.grid)
        self.dialog.show_all()

    def run(self):
        return self.dialog.run()

    def destroy(self):
        self.dialog.destroy()

    def on_openimagebutton_clicked(self, widget, data=None):
        dialog = Gtk.FileChooserDialog('Abrir imagen', self.dialog,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_filename()
            print filename

        dialog.destroy()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main = LuminosoGtk(sys.argv[1])
    else:
        main = LuminosoGtk()
    Gtk.main()
