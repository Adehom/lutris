# -*- coding:Utf-8 -*-
###############################################################################
## Lutris
##
## Copyright (C) 2009 Mathieu Comandon strycore@gmail.com
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
###############################################################################
import gobject
import urllib

class Downloader(gobject.GObject):
    """Downloader class that doesn't block the program"""
    __gsignals__ = {
            'report-progress': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
                (gobject.TYPE_INT,))
            }

    def __init__(self, url, dest):
        """Set up the downloader."""
        gobject.GObject.__init__(self)
        self.url = url
        self.dest = dest

    def start(self):
        """Start the download."""
        urllib.urlretrieve(self.url, self.dest, self._report_progress)

    def _report_progress(self, piece, received_bytes, total_size):
        """Emit a signal for each piece downloaded."""
        progress = ((piece * received_bytes) * 100) / total_size
        self.emit('report-progress', progress)
