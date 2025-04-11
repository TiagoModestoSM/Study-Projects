from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget   
from assets.botton import BotaoPersonalizado

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Usando Botão Personalizado")
        self.setFixedSize(1280, 720)
        
        botao1 = BotaoPersonalizado(
            "Cadastrar",
            pos=(150, 520),
            font="Segoe UI",
            tamanh_fonte=13,
            cor="#FF5722",
            tamanho=(200, 45),
            parent=self
        )
        
        botao2 = BotaoPersonalizado(
            "Sair",
            pos=(400, 520),
            font="Segoe UI",
            tamanh_fonte=13,
            cor="#FF5722",
            tamanho=(200, 45),
            parent=self
        )
        self.centralizar_na_tela()

    def centralizar_na_tela(self):
        qr = self.frameGeometry()  # Pega o retângulo da janela
        cp = QDesktopWidget().availableGeometry().center()  # Centro da tela disponível
        qr.moveCenter(cp)  # Move o centro da janela pro centro da tela
        self.move(qr.topLeft())  # Move a janela para esse ponto
        
if __name__ == "__main__":
    app = QApplication([])
    janela = JanelaPrincipal()
    janela.show()
    app.exec_()
