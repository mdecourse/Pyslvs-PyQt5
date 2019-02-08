# -*- coding: utf-8 -*-

"""The option dialog to specify target points."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import TYPE_CHECKING, Iterator
from core.QtModules import (
    Slot,
    Qt,
    QDialog,
    QListWidget,
)
from .Ui_targets import Ui_Dialog

if TYPE_CHECKING:
    from core.synthesis.collections import ConfigureWidget


def list_texts(widget: QListWidget) -> Iterator[str]:
    """Generator to get the text from list widget."""
    for row in range(widget.count()):
        yield widget.item(row).text()


class TargetsDialog(QDialog, Ui_Dialog):

    """Option dialog.

    Only edit the settings after closed.
    """

    def __init__(self, parent: 'ConfigureWidget'):
        """Filter and show the target option (just like movable points)."""
        super(TargetsDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        current_item = parent.grounded_list.currentItem()

        if current_item:

            def combo_texts(widget) -> Iterator[str]:
                """Generator to get the text from combobox widget."""
                for index in range(widget.count()):
                    yield widget.itemText(index)

            for text in combo_texts(parent.joint_name):
                num = int(text.replace('P', ''))
                if (num not in parent.configure_canvas.same) and (text not in (
                    current_item.text()
                    .replace('(', '')
                    .replace(')', '')
                    .split(", ")
                )):
                    self.other_list.addItem(text)

        target_list = [text for text in list_texts(parent.target_list)]
        for row, text in enumerate(list_texts(self.other_list)):
            if text in target_list:
                self.targets_list.addItem(self.other_list.takeItem(row))

    @Slot(name='on_targets_add_clicked')
    def __add(self):
        """Add a new target joint."""
        row = self.other_list.currentRow()
        if not row > -1:
            return
        self.targets_list.addItem(self.other_list.takeItem(row))

    @Slot(name='on_other_add_clicked')
    def __remove(self):
        """Remove a target joint."""
        row = self.targets_list.currentRow()
        if not row > -1:
            return
        self.other_list.addItem(self.targets_list.takeItem(row))
