import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from helper_function.compile_qrc import compile_qrc

compile_qrc()
from icons_setup.compiledIcons import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Music Similarity Analysis')
        self.setWindowIcon(QIcon('icons_setup/icons/logo.png'))

        self.play_icon = QIcon(':/icons_setup/icons/play.png')
        self.pause_icon = QIcon(':/icons_setup/icons/pause.png')

        # Find the tableFrame
        self.tableFrame = self.findChild(QFrame, 'tableFrame')
        if not self.tableFrame:
            print("Error: tableFrame not found in the UI file.")
            return
        
        self.setup_table()

    def setup_table(self):

        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Rank", "Song Name", "Matching %", "Controls"])

        self.table.verticalHeader().setVisible(False)


        # Style table
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #142A4A;
                color: #ffffff;
                border: none;
                gridline-color: #39bef7;
                font-size: 16px;
                border-radius: 10px;
            }
            QTableWidget::item {
                padding: 12px; /* Increased padding */
                border: none;
                margin: 4px; /* Adds spacing around each cell */
                border-radius: 6px;
            }
            QTableWidget::item:selected {
                background-color: #1e3a5f;
            }
            QHeaderView::section {
                background-color: #0f1729;
                color: #39bef7;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #39bef7;
                font-weight: bold;
                font-size: 15px;
                text-transform: uppercase;
            }
            QHeaderView::section:first {
                border-top-left-radius: 10px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 10px;
            }
            QPushButton {
                background-color: #39bef7;
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 8px 15px;
                min-width: 80px;
                font-weight: bold;
                text-transform: uppercase;
            }
            QPushButton:hover {
                background-color: #2196f3;
            }
            QScrollBar:vertical {
            background: #0f1729;
            width: 12px;
            border: none;
            margin: 2px 0 2px 0;
            border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #39bef7;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
                background: #142A4A;
                height: 12px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                background: #142A4A;
                height: 12px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: #0f1729;
                border-radius: 6px;
            }
        """)

        # Configure columns
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Fixed)
        header.setSectionResizeMode(3, QHeaderView.Fixed)

        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 180)

        # Populate with dummy data
        dummy_data = [
            (1, "Bohemian Rhapsody - Queen", "98.5%"),
            (2, "Hotel California - Eagles", "95.2%"),
            (3, "Stairway to Heaven - Led Zeppelin", "92.8%"),
            (4, "Sweet Child O' Mine - Guns N' Roses", "90.1%")
        ]

        for row, (rank, song, match) in enumerate(dummy_data):
            # Set row height
            self.table.setRowHeight(row, 80) 

            # Rank
            rank_item = QTableWidgetItem(str(rank))
            rank_item.setTextAlignment(Qt.AlignCenter)
            rank_item.setFlags(rank_item.flags() & ~Qt.ItemIsEditable)  
            self.table.setItem(row, 0, rank_item)

            # Song name
            song_item = QTableWidgetItem(song)
            song_item.setFlags(song_item.flags() & ~Qt.ItemIsEditable)  
            self.table.setItem(row, 1, song_item)

            # Match percentage
            match_item = QTableWidgetItem(match)
            match_item.setTextAlignment(Qt.AlignCenter)
            match_item.setFlags(match_item.flags() & ~Qt.ItemIsEditable)  
            self.table.setItem(row, 2, match_item)

            play_btn = QPushButton()
            play_btn.setIcon(QIcon(":/icons_setup/icons/play.png"))
            play_btn.setIconSize(QtCore.QSize(15, 15))

            # Create container frame
            container = QFrame()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(play_btn, alignment=Qt.AlignCenter)

            self.table.setCellWidget(row, 3, container)

        self.tableFrame.layout().addWidget(self.table)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())