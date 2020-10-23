import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl

import plotly
import plotly.graph_objects as go


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(f'Plotly Demo')
        self.setMinimumSize(800, 600)
        self.setupUi()

        self.data = data = list(range(100))
        
        self.buttons['update'].clicked.connect(self.update_)
        
        #self.updatePlotly(data)

    def update_(self):
        self.updatePlotly(self.data)

    def updatePlotly(self, data):
        fig = go.Figure(data=go.Scatter(y=data))
        fig.write_html('first_figure.html', auto_open=False)
        path = QDir.current().filePath('first_figure.html') 
        url = QUrl.fromLocalFile(path)
        self.view.load(url)
        self.status.showMessage(path)

    def setupUi(self):
        self.view = view = QWebEngineView() 
        self.setCentralWidget(view)
        
        self.buttons = {}
        button =  QPushButton("Update", self)
        self.buttons['update'] = button

        self.status = self.statusBar()
        

if __name__ == "__main__":
    sys.argv.append("--disable-web-security")
    app = QApplication(sys.argv)

    mw =  MainWindow()
    mw.show()

    sys.exit(app.exec_())
