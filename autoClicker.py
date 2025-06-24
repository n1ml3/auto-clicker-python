import tkinter as tk
import threading
import time
import keyboard
from pynput.mouse import Controller, Button

mouse = Controller()
running = threading.Event()
hotkey = 'f6'

def auto_click(interval):
    while running.is_set():
        mouse.click(Button.left)
        # Đảm bảo sleep không nhỏ hơn 5ms để tránh CPU 100%
        time.sleep(max(0.005, interval))

def toggle_clicking():
    if running.is_set():
        running.clear()
    else:
        try:
            interval = float(entry_interval.get())
        except ValueError:
            interval = 0.1
        running.set()
        threading.Thread(target=auto_click, args=(interval,), daemon=True).start()

def set_hotkey():
    global hotkey
    new_key = entry_hotkey.get().strip().lower()
    if new_key:
        try:
            keyboard.remove_hotkey(hotkey)
        except:
            pass
        hotkey = new_key
        keyboard.add_hotkey(hotkey, toggle_clicking)
        label_status.config(text=f"Đã gán hotkey: {hotkey.upper()}")

# GUI
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("280x200")
root.resizable(False, False)

tk.Label(root, text="Thời gian giữa các click (giây):").pack()
entry_interval = tk.Entry(root, width=10)
entry_interval.insert(0, "0.1")
entry_interval.pack()

tk.Label(root, text="Phím tắt để bắt đầu/dừng:").pack()
entry_hotkey = tk.Entry(root, width=10)
entry_hotkey.insert(0, "f6")
entry_hotkey.pack()

tk.Button(root, text="Gán phím tắt", command=set_hotkey).pack(pady=4)
label_status = tk.Label(root, text="Mặc định: F6 để bật/tắt", fg="green")
label_status.pack()

def clean_exit():
    running.clear()
    try:
        keyboard.remove_hotkey(hotkey)
    except:
        pass
    root.destroy()

tk.Button(root, text="Thoát", command=clean_exit).pack(pady=5)

# Khởi tạo mặc định
keyboard.add_hotkey(hotkey, toggle_clicking)
root.protocol("WM_DELETE_WINDOW", clean_exit)
root.mainloop()
