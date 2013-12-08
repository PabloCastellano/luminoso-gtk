#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ledfonts.py
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

sys.path.append('.')
sys.path.append('..')

from gtkledsgrid import GtkLedsGrid
from ledsfont import LedFont


class FontViewer:
    def __init__(self, filename=None):
        self.grid = GtkLedsGrid(16, 64)
        self.font = LedFont()
        self.ui = Gtk.Builder()
        self.ui.add_from_file('ui/fontviewer.glade')
        self.ui.connect_signals(self)

        self.ui.get_object('alignment2').add(self.grid)
        self.main_window = self.ui.get_object('mainwindow')
        self.combobox = self.ui.get_object('combobox')
        self.liststore = self.ui.get_object('liststore')
        self.sentenceentry = self.ui.get_object('sentenceentry')
        self.main_window.show_all()

        if filename:
            self.load_font(filename)
            #self.grid.load_file(filename)

    def load_font(self, filename):
        self.font.load2(filename)
        #self.combobox.clear()
        dict = sorted(self.font.dict.iteritems())
        for char, rep in dict:
            if self.isascii(char):
                # FIXME: filter not ascii chars
                self.liststore.append((char, rep))

    def on_combobox_changed(self, widget, data=None):
        it = self.combobox.get_active_iter()
        print self.liststore.get_value(it, 0)
        value = self.liststore.get_value(it, 1)
        print 'Repr:', value

        for ledbyte in value:
            ledbyte = ord(ledbyte)
            for b in range(7, -1, -1):
                val = ledbyte >> b & 1
                print val,
            print

        self.grid.clear(0, 16, 0, 8)
        self.grid.paint_bytes(value)

    def on_viewallbutton_clicked(self, widget, data=None):
        print 'View all'

    def on_openmenuitem_activate(self, widget, data=None):
        dialog = Gtk.FileChooserDialog('Abrir fuente', self.main_window,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_filename()
            print filename

        dialog.destroy()

    def gtk_main_quit(self, widget, data=None):
        Gtk.main_quit()

    def isascii2(self, s):
        return all(ord(c) < 128 for c in s)

    def isascii(self, c, printable=True):
        if 0x00 <= ord(c) <= 0x7f:
            if printable:
                if 0x20 <= ord(c) <= 0x7e:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main = FontViewer(sys.argv[1])
    else:
        main = FontViewer()

    Gtk.main()
