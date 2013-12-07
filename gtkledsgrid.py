#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# gtkledsgrid.py
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
from gi.repository import Gdk


class GtkLedsGrid(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(6)
        self.set_column_spacing(6)

        # Create a matrix using GtkEventBox + GtkFixed widgets
        for x in range(64):
            for y in range(16):
                l = self.create_led()
                self.attach(l, x, y, 1, 1)

    def create_led(self, color="gray"):
        f = Gtk.Fixed()
        f.set_size_request(6, 6)
        eb = Gtk.EventBox()
        eb.add(f)
        eb.modify_bg(Gtk.StateType.NORMAL, Gdk.Color.parse(color)[1])
        return eb
