# -*- coding: utf-8 -*-
from .__init__ import *

class New_link(QDialog, link_Dialog):
    def __init__(self, parent=None):
        super(New_link, self).__init__(parent)
        self.setupUi(self)