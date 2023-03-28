import tkinter as tk
from funciones import get_hostname, get_ip_address, scan_port, find_password_in_dict, decimal_to_binary

class App:
    def __init__(self, master):
        self.master = master
        master.title("Basic Tools PenTests Python")

        self.label_ip = tk.Label(master, text="Insert IP:")
        self.label_ip.grid(row=0, column=0)

        self.entry_ip = tk.Entry(master)
        self.entry_ip.grid(row=0, column=1)

        self.label_scan = tk.Label(master, text="Scan Objev:")
        self.label_scan.grid(row=1, column=0)

        self.result_scan = tk.Text(master, height=10, width=50)
        self.result_scan.grid(row=1, column=1)

        self.scan_button = tk.Button(master, text="Scan", command=self.scan_ip)
        self.scan_button.grid(row=0, column=2)

        self.label_hostname = tk.Label(master, text="DesktopName: ")
        self.label_hostname.grid(row=2, column=0)

        self.result_hostname = tk.Label(master, text=get_hostname())
        self.result_hostname.grid(row=2, column=1)

        self.label_ipaddr = tk.Label(master, text="IP:")
        self.label_ipaddr.grid(row=3, column=0)

        self.result_ipaddr = tk.Label(master, text=get_ip_address())
        self.result_ipaddr.grid(row=3, column=1)

        self.label_passhash = tk.Label(master, text="Hashed Password: ")
        self.label_passhash.grid(row=4, column=0)

        self.entry_passhash = tk.Entry(master)
        self.entry_passhash.grid(row=4, column=1)

        self.label_passdict = tk.Label(master, text="Dir")
        self.label_passdict.grid(row=5, column=0)

        self.entry_passdict = tk.Entry(master)
        self.entry_passdict.grid(row=5, column=1)

        self.hash_button = tk.Button(master, text="Find Password", command=self.find_password)
        self.hash_button.grid(row=4, column=2)

        self.label_decimal = tk.Label(master, text="Insert Number: ")
        self.label_decimal.grid(row=6, column=0)

        self.entry_decimal = tk.Entry(master)
        self.entry_decimal.grid(row=6, column=1)

        self.binary_button = tk.Button(master, text="Convert to Binary", command=self.decimal_to_binary)
        self.binary_button.grid(row=6, column=2)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=7, column=2)

        self.label_footer = tk.Label(master, text="Creado por [TATO COFFEE CoDeXs]")
        self.label_footer.grid(row=8, column=1, sticky="S")

    def scan_ip(self):
        ip = self.entry_ip.get()
        self.result_scan.delete(1.0, tk.END)
        self.result_scan.insert(tk.END, scan_port(ip))

    def find_password(self):
        hash_val = self.entry_passhash.get()
        dict_val = self.entry_passdict.get()
        self.result_scan.delete(1.0, tk.END)
        self.result_scan.insert(tk.END, find_password_in_dict(hash_val, dict_val))

    def decimal_to_binary(self):
        decimal_val = int(self.entry_decimal.get())
        self.result_scan.delete(1.0, tk.END)
        self.result_scan.insert(tk.END, decimal_to_binary(decimal_val))


root = tk.Tk()
app = App(root)
root.mainloop()
