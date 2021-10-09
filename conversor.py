from conversor_modelo import *
from temperatura import Temperatura
from sys import argv
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Conversor(QWidget, Ui_Form):

    # ------------------------------------------------------------------

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.temperatura: Temperatura = Temperatura()
        
        self.conectar_botoes()
        self.preencher_combo()

    # ------------------------------------------------------------------

    def converter(self) -> None:
        if len(self.txt_entrada.text()) > 0:
            try:
                self.temperatura.temperatura_entrada = float(self.txt_entrada.text())
                self.detecta_tipo_temperatura()
                self.txt_saida.setText(str(
                    f"{self.temperatura.temperatura_saida}°"
                ))
            except ValueError:
                mensagem = QMessageBox()
                mensagem.setWindowTitle("Atenção")
                mensagem.setIcon(QMessageBox.Warning)
                mensagem.setText("A temperatura deve ser númerica")
                mensagem.exec_()

    # ------------------------------------------------------------------

    def reiniciar(self) -> None:
        if len(self.txt_entrada.text()) > 0:
            self.txt_entrada.clear()
        
        if len(self.txt_saida.text()) > 0:
            self.txt_saida.clear()

    # ------------------------------------------------------------------

    def detecta_tipo_temperatura(self) -> None:
        if self.cmb_entrada.currentText() == 'Celsius':
            if self.cmb_saida.currentText() == 'Fahrenheit':
                self.temperatura.celsius_para_fahrenheit()
            elif self.cmb_saida.currentText() == 'Kelvin':
                self.temperatura.celsius_para_kelvin()
            else:
                self.temperatura.celsius_para_celsius()
                
        elif self.cmb_entrada.currentText() == 'Fahrenheit':
            if self.cmb_saida.currentText() == 'Celsius':
                self.temperatura.fahrenheit_para_celsius()
            elif self.cmb_saida.currentText() == 'Kelvin':
                self.temperatura.fahrenheit_para_kelvin()
            else:
                self.temperatura.fahrenheit_para_fahrenheit()
                
        elif self.cmb_entrada.currentText() == 'Kelvin':
            if self.cmb_saida.currentText() == 'Celsius':
                self.temperatura.kelvin_para_celsius()
            elif self.cmb_saida.currentText() == 'Fahrenheit':
                self.temperatura.kelvin_para_fahrenheit()
            else:
                self.temperatura.kelvin_para_kelvin()

    # ------------------------------------------------------------------

    def preencher_combo(self) -> None:
        for temperatura in Temperatura.TEMPERATURAS:
            self.cmb_entrada.addItem(temperatura)
            self.cmb_saida.addItem(temperatura)

    # ------------------------------------------------------------------

    def conectar_botoes(self) -> None:
        self.btn_converter.clicked.connect(self.converter)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

    # ------------------------------------------------------------------


def main() -> None:
    aplicacao: QApplication = QApplication(argv)
    conversor: Conversor = Conversor()
    conversor.show()
    aplicacao.exec_()
# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()
