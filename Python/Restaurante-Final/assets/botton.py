# botao_personalizado.py

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QPoint, QSize

class BotaoPersonalizado(QPushButton):
    def __init__(self, texto, pos=(0, 0), font="Arial", tamanh_fonte=12, cor="#4CAF50", tamanho=(200, 40), parent=None):
        super().__init__(texto, parent)
        
        self.setFont(QFont(font, tamanh_fonte))
        self.setFixedSize(QSize(*tamanho))
        self.move(QPoint(*pos))

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {cor};
                color: white;
                border: none;
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: #45a049;
            }}
        """)
