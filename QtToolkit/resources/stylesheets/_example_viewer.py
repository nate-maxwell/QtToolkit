"""
# Stylesheet Viewer

* Description:

    A UI theme and color viewer with example widgets.
"""


import sys
from pathlib import Path

from PySide6 import QtCore
from PySide6 import QtWidgets

import QtToolkit.gui
import QtToolkit.shapes
from QtToolkit.main_window import MainWindow
from QtToolkit.labeled_combobox import LabeledComboBox
from QtToolkit.searchable_list import SearchableList
from QtToolkit.groupbox import GroupBox


_styles = QtToolkit.gui.STYLE_PATH.glob('*')
_sheets = [i.stem for i in _styles]
_sheets.remove('__init__')
_sheets.remove('_example_viewer')


class ExampleWidget(QtWidgets.QWidget):
    """A widget filled with example items for theme and color testing."""
    def __init__(self) -> None:
        super().__init__()
        self._create_widgets()
        self._create_layout()

    def _create_widgets(self) -> None:
        self.layout_main = QtWidgets.QHBoxLayout()

        self.sl_items = SearchableList('Searchable List')

        self.sl_items.populate_column(_sheets)

        self.cmb_example = QtWidgets.QComboBox()
        self.cmb_example.addItems(['One', 'Two', 'Three'])

        self.le_example = QtWidgets.QLineEdit()
        self.le_example.setPlaceholderText("Line Edit")

        self.sbx_example = QtWidgets.QSpinBox()
        self.fsbx_example = QtWidgets.QDoubleSpinBox()
        self.cbx_example = QtWidgets.QCheckBox('Check Box')
        self.rdo_example = QtWidgets.QRadioButton('Radio Button')
        self.btn_example = QtWidgets.QPushButton('Push Button')
        self.btn_example.setFixedWidth(200)
        self.dial_example = QtWidgets.QDial()
        self.sldr_example = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sldr_example.setValue(50)
        self.grp_example = GroupBox('Group Box')

    def _create_layout(self) -> None:
        self.setLayout(self.layout_main)

        self.grp_example.add_widget(QtWidgets.QLabel('Combo Box'))
        self.grp_example.add_widget(self.cmb_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(self.le_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(QtWidgets.QLabel('Spin Box'))
        self.grp_example.add_widget(self.sbx_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(QtWidgets.QLabel('Double Spin Box'))
        self.grp_example.add_widget(self.fsbx_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(self.cbx_example)
        self.grp_example.add_widget(self.rdo_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(self.btn_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(QtWidgets.QLabel('Dial'))
        self.grp_example.add_widget(self.dial_example)
        self.grp_example.add_widget(QtToolkit.shapes.HorizontalLine())
        self.grp_example.add_widget(QtWidgets.QLabel('Slider'))
        self.grp_example.add_widget(self.sldr_example)
        self.grp_example.add_stretch()

        self.layout_main.addWidget(self.sl_items)
        self.layout_main.addWidget(self.grp_example)


class StyleViewer(MainWindow):
    def __init__(self) -> None:
        super().__init__('Style Library Viewer',
                         (0, 0), (0, 0))
        self._create_widgets()
        self._create_layout()
        self._create_connections()
        self._on_cmb_change()

    def _create_widgets(self) -> None:
        self.widget_main = QtWidgets.QWidget()
        self.layout_main = QtWidgets.QHBoxLayout()

        self.vlayout_left = QtWidgets.QVBoxLayout()
        self.cmb_stylesheet = LabeledComboBox('Stylesheet')
        self.cmb_stylesheet.add_items(_sheets)

        self.example_widget = ExampleWidget()

    def _create_layout(self) -> None:
        self.setCentralWidget(self.widget_main)
        self.widget_main.setLayout(self.layout_main)

        self.vlayout_left.addWidget(self.cmb_stylesheet)
        self.vlayout_left.addStretch()

        self.layout_main.addLayout(self.vlayout_left)
        self.layout_main.addWidget(QtToolkit.shapes.VerticalLine())
        self.layout_main.addWidget(self.example_widget)

    def _create_connections(self) -> None:
        self.cmb_stylesheet.cmb_box.currentTextChanged.connect(self._on_cmb_change)

    def _on_cmb_change(self) -> None:
        p = Path(QtToolkit.gui.STYLE_PATH, f'{self.cmb_stylesheet.current_text()}.qss')
        if not p.exists():
            return

        with open(p) as f:
            self.setStyleSheet(f.read())


def main():
    """Runs the standalone Batch Renamer."""
    app = QtWidgets.QApplication(sys.argv)
    window = StyleViewer()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
