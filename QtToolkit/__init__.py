from pathlib import Path
from typing import Optional
from typing import Union

from PySide6 import QtCore
from PySide6 import QtWidgets


QT_COMMON_TYPE = Union[QtWidgets.QWidget, QtWidgets.QLayout]
QT_WIDGET_TYPE = 'widget'
QT_LAYOUT_TYPE = 'layout'


def get_item_common_type(item: QtCore.QObject) -> Optional[str]:
    """Returns the string common type the item matches. E.g. 'widget',
     'layout', or None."""
    if isinstance(item, QtWidgets.QWidget):
        return QT_WIDGET_TYPE
    elif isinstance(item, QtWidgets.QLayout):
        return QT_LAYOUT_TYPE

    return None
