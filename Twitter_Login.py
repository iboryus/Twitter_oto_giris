import tkinter as tk
import time
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Giriş Yapma
def twitter_login(username, password):
    browser = webdriver.Chrome()
    browser.get("https://x.com/i/flow/login")
    time.sleep(5)
    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input"))
    )
    username_input.send_keys(username)
    time.sleep(5)
    ileri_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]"))
    )
    ileri_button.click()
    time.sleep(5)
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
    )
    password_input.send_keys(password)
    time.sleep(3)
    giris_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button"))
    )
    giris_button.click()

# Buton Fonksiyonu
def on_login_button_click():
    username = username_entry.get()
    password = password_entry.get()
    twitter_login(username, password)

# Arayüz
root = tk.Tk()
root.title("Twitter Giriş")
root.geometry("400x300")
root.configure(bg='#ffffff')
root.attributes('-alpha', 0.9)
style = ttk.Style()
style.configure('TFrame', background='#ffffff')
frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(root, text="Kullanıcı Adı").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Şifre").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Giriş Yap", command=on_login_button_click)
login_button.pack(pady=20)

root.mainloop()
