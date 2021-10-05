import pyautogui
import time
import pyperclip
pyautogui.PAUSE = 1
#abrir navegador

pyautogui.press("winleft")
pyautogui.write("chome")
pyautogui.press("enter")
#pyautogui.alert("Vai comecar, aperte ok e nao mexa em nada")
pyautogui.hotkey('ctrl', 't')

#abrir drive
#ensinar o write
link = "https://drive.google.com/drive/u/0/folders/1qjIgoyl6x_kGBSKW98yks0C-6uHtAtFf"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=624, y=806)
time.sleep(2)
pyautogui.click(x=416, y=461)
time.sleep(2)
pyautogui.click(x=1389, y=196)
time.sleep(2)
pyautogui.click(x=1258, y=594)
time.sleep(2)
pyautogui.click(x=635, y=432)

#import pandas as pd

#tabela = pd.read_excel(r"C:\Users\salvesa\Downloads\Venda-Dez.xlsx")
#display(tabela)
#faturamento = tabela["Valor Final"].sum()
#quantidade = tabela["Quantidade"].sum()

#Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

time.sleep(5)
pyautogui.position()
#Enviar o email com o resultado
pyautogui.click(x=94, y=215)
pyautogui.write("contato.sebastiaoalves+diretoria@gmail.com")
pyautogui.press("tab") #seleciona o email
pyautogui.press("tab")  # pula campo de assunto
pyperclip.copy("Relatorio de Vendas")
pyautogui.hotkey("ctrl", "v") #assunto do email
pyautogui.press("tab") #pular para o corpo do email

texto = """
Prezado, Bom dia!
O faturamento de ontem foi de:R${faturamento:,.2f}
A quantidade de produtos foi de:{quantidade:,}

Abs
Sebastiao"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")


