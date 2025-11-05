from PySide6 import QtCore

from PySide6TK import QtWrappers


class Worker(QtCore.QObject):
    work_done = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.work_done.connect(self.on_work_done)

    @QtWrappers.emit_signal('work_done')
    def do_work(self) -> None:
        print('Doing some work...')

    @staticmethod
    def on_work_done() -> None:
        print('Work is done!')


if __name__ == '__main__':
    app = QtCore.QCoreApplication([])

    worker = Worker()
    worker.work_done.connect(app.quit)
    QtCore.QTimer.singleShot(0, worker.do_work)

    app.exec()
