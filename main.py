from PySimpleGUI import PySimpleGUI as sg


__versao__ = "Versão 1.0.0"
sg.theme("LightGray1")

layout = [[sg.Push(), sg.T("Hello World"), sg.Push()]]

janela = sg.Window("Desempenho", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break

janela.close()
