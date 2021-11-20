print("SELAMAT DATANG DI ZyraXenOS 0.1 EMULATOR!")

import time
print("starting emulator...")
time.sleep(5)
print("\n")
print("\n")
print("╭━━━━┳╮╱╱╭┳━━━┳━━━┳━╮╭━┳━━━┳━╮╱╭╮╭━━━┳━━━╮")
print("╰━━╮━┃╰╮╭╯┃╭━╮┃╭━╮┣╮╰╯╭┫╭━━┫┃╰╮┃┃┃╭━╮┃╭━╮┃")
print("╱╱╭╯╭┻╮╰╯╭┫╰━╯┃┃╱┃┃╰╮╭╯┃╰━━┫╭╮╰╯┃┃┃╱┃┃╰━━╮")
print("╱╭╯╭╯╱╰╮╭╯┃╭╮╭┫╰━╯┃╭╯╰╮┃╭━━┫┃╰╮┃┃┃┃╱┃┣━━╮┃")
print("╭╯━╰━╮╱┃┃╱┃┃┃╰┫╭━╮┣╯╭╮╰┫╰━━┫┃╱┃┃┃┃╰━╯┃╰━╯┃")
print("╰━━━━╯╱╰╯╱╰╯╰━┻╯╱╰┻━╯╰━┻━━━┻╯╱╰━╯╰━━━┻━━━╯")
time.sleep(3)
print("\n")
print("\n")
print("ZyraXenOS is already started!")
print("\n")
print("█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█")
print("█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█")
#main menu

choice = input("""
A.Youtube
B.Discord
C.WhatsApp
D.Close Program

Masukkan pilihan anda: """)

if choice == "A" or choice == "a":
    print("sedang mengalihkan anda ke Youtube...")
    import webbrowser
    webbrowser.open("https://youtube.com/")
    
if choice == "B" or choice == "b":
    print("Sedang mengalihkan anda ke Discord...")
    import webbrowser
    webbrowser.open("https://discord.gg/") 
if choice == "C" or choice == "c":
    print("Sedang mengalihkan anda ke WhatsApp...")
    import webbrowser
    webbrowser.open("https://chat.whatsapp.com/") or ("https://whatsapp.com/")
    
if choice == "D" or choice == "d":
    print("closing program...")
    time.sleep(1)
    print("shutting down...")
    time.sleep(3)
    print("\n")
    print("program closed sucsessfully!")