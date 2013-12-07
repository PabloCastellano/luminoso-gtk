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


# It creates a matrix using GtkEventBox + GtkFixed widgets
class GtkLedsGrid(Gtk.Grid):
    def __init__(self, rows, columns):
        Gtk.Grid.__init__(self)
        self.rows = rows
        self.columns = columns
        self.set_row_spacing(6)
        self.set_column_spacing(6)
        self.leds = LedsArray(rows, columns)
        self.init_leds()

    # Initialize the data structure and the led panel widget
    def init_leds(self):
        for x in range(self.columns):
            for y in range(self.rows):
                l = self._create_led()
                self.attach(l, x, y, 1, 1)
                self.leds.set_led(x, y, 0, l)

    # Load .iat files
    def load_file(self, filename):
        with open(filename, 'rb') as fp:
            self._bytes_to_leds(fp.read())

    def _bytes_to_leds(self, content):
        n = 0
        for ledbyte in content:
            ledbyte = ord(ledbyte)
            for b in range(7, -1, -1):
                value = ledbyte >> b & 1
                self.leds.set_value(n / self.rows, n % self.rows, value)
                n += 1

    def _create_led(self, color="gray"):
        f = Gtk.Fixed()
        f.set_size_request(6, 6)
        eb = Gtk.EventBox()
        eb.add(f)
        eb.modify_bg(Gtk.StateType.NORMAL, Gdk.Color.parse(color)[1])
        return eb


# Led represents one of the small lights. It associates the widget with its value (on, off)
class Led:
    def __init__(self, value, widget):
        if not value in (0, 1):
            raise KeyError(value)
        if not isinstance(widget, Gtk.Widget):
            raise KeyError(widget)
        self.value = value
        self.widget = widget
        self.color_on = "red"
        self.color_off = "gray"

    def set_value(self, value):
        if not value in (0, 1):
            raise KeyError
        self.value = value
        if value == 1:
            self.change_color(self.color_on)
        elif value == 0:
            self.change_color(self.color_off)

    def change_color(self, color):
        self.widget.modify_bg(Gtk.StateType.NORMAL, Gdk.Color.parse(color)[1])


# LedsArray represents the whole led panel
class LedsArray:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.leds = {}

        for x in range(columns):
            self.leds[x] = dict()

    def set_led(self, x, y, value, widget):
        if not (x >= 0 and x < self.columns):
            raise KeyError(x)
        elif not (y >= 0 and y < self.rows):
            raise KeyError(y)
        self.leds[x][y] = Led(value, widget)

    def set_value(self, x, y, value):
        if not (x >= 0 and x < self.columns):
            raise KeyError(x)
        elif not (y >= 0 and y < self.rows):
            raise KeyError(y)
        self.leds[x][y].set_value(value)

    def get_value(self, x, y):
        return self.leds[x][y].value
