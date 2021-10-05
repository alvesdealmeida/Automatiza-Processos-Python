import pyautogui
import time
import pyperclip

import pandas as pd

tabela = pd.read_excel(r"C:\Users\salvesa\Downloads\Venda-Dez.xlsx")
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

#Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

#Enviar o email com o resultado
pyautogui.click(x=134, y=197)
pyautogui.write("contato.sebastiaoalves+diretoria@gmail.com")
pyautogui.press("tab") #seleciona o email
pyautogui.press("tab")  # pula campo de assunto
pyperclip.copy("Relatorio de Vendas")
pyautogui.hotkey("ctrl", "v") #assunto do email
pyautogui.press("tab") #pular para o corpo do email

texto = f"""
Prezado, Bom dia!
O faturamento de ontem foi de:R${faturamento:,.2f}
A quantidade de produtos foi de:{quantidade:,}

Abs
Sebastiao"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")


