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


from gi.repository import Gdk, Gtk

from gtkledsgrid import GtkLedsGrid


class LuminosoGtk:
    def __init__(self):
        self.grid = GtkLedsGrid()
        self.ui = Gtk.Builder()
        self.ui.add_from_file('ui/mainwindow.glade')
        self.ui.connect_signals(self)

        e1 = self.ui.get_object('eventbox1')
        e1.modify_bg(Gtk.StateType.NORMAL, Gdk.Color.parse("black")[1])
        a7 = self.ui.get_object('alignment7')
        a7.add(self.grid)
        self.main_window = self.ui.get_object('mainwindow')
        self.main_window.show_all()

    def gtk_main_quit(self, widget, data=None):
        Gtk.main_quit()


if __name__ == "__main__":
    main = LuminosoGtk()
    Gtk.main()
