import tkinter as tk
from tkinter import ttk, messagebox

def dd_to_dms(dd):
    try: 
        dd = float(dd)
        degrees = int(dd)
        minutes = int((dd - degrees) * 60)
        seconds = (dd - degrees - minutes / 60) * 3600
        return f"{degrees}° {minutes}' {seconds:.2f}\""
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Por favor, ingrese un número válido.")
        return ""
def dms_to_dd(degrees, minutes, seconds):
    try:
        degrees, minutes, seconds = int(degrees), int(minutes), float(seconds)
        return round(degrees + minutes / 60 + seconds / 3600, 6)
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Por favor, ingrese números válidos.")
        return None
    
def convert_dd_a_dms():
    dd_to_dms_input = entry_dd.get()
    result = dd_to_dms(dd_to_dms_input)
    if result:
        label_result.config(text=f"Resultado: {result}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Conversión")

# Entradas para grados, minutos y segundos
entry_grados = ttk.Entry(root, width=5)
entry_grados.grid(row=0, column=1)
entry_minutos = ttk.Entry(root, width=5)
entry_minutos.grid(row=0, column=2)
entry_segundos = ttk.Entry(root, width=5)
entry_segundos.grid(row=0, column=3) 

def convert_dms_a_dd():
    grade = entry_grados.get()
    minutes = entry_minutos.get()
    seconds = entry_segundos.get()
    result = dms_to_dd(grade, minutes, seconds)
    if result is not None:
        label_result.config(text=f"Resultado: {result}°")
# Etiquetas para grados, minutos y segundos
label_grados = ttk.Label(root, text="Grados:")
label_grados.grid(row=0, column=0)
label_minutos = ttk.Label(root, text="Minutos:")
label_minutos.grid(row=1, column=0)
label_segundos = ttk.Label(root, text="Segundos:")
label_segundos.grid(row=2, column=0)

def clean_entries():
    entry_grados.delete(0, tk.END)
    entry_minutos.delete(0, tk.END)
    entry_segundos.delete(0, tk.END)
    entry_dd.delete(0, tk.END)
    label_result.config(text="")
    result_dd_dms.set("")
    result_dms_dd.set("")
    
    
# Etiqueta para mostrar resultados
label_result = ttk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=4, pady=10)

# crear ventana de entrada para grados decimales 
ventana = tk.Tk()
ventana.title("Conversión de Coordenadas")
ventana.geometry("350x300")

#Dar estilo a la ventana
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#0CF1E2", foreground="white")

# Frame para grados decimales
frame_dd_dms = ttk.LabelFrame(ventana, text="Grados Decimales a DMS")
frame_dd_dms.pack(padx=10, pady=10, fill="x")

ttk.Label(frame_dd_dms, text="Grados Decimales:").pack(side="left", padx=5, pady=5)
entry_dd = ttk.Entry(frame_dd_dms, width=10)
entry_dd.pack(side="left", padx=5, pady=5)
ttk.Button(frame_dd_dms, text="Convertir", command=convert_dd_a_dms).pack(side="left", padx=5, pady=5)
result_dd_dms = tk.StringVar()
ttk.Label(frame_dd_dms, textvariable=result_dd_dms).pack(side="left", padx=5, pady=5)

# Frame para DMS a grados decimales
frame_dms_dd = ttk.LabelFrame(ventana, text="DMS a Grados Decimales") 
frame_dms_dd.pack(padx=10, pady=10, fill="x")
ttk.Label(frame_dms_dd, text="Grados:").pack(side="left", padx=5, pady=5)
entry_grades = ttk.Entry(frame_dms_dd, width=5)
entry_grades.pack(side="left", padx=5, pady=5)
ttk.Label(frame_dms_dd, text="Minutos:").pack(side="left", padx=5, pady=5)
entry_minutes = ttk.Entry(frame_dms_dd, width=5)
entry_minutes.pack(side="left", padx=5, pady=5)
ttk.Label(frame_dms_dd, text="Segundos:").pack(side="left", padx=5, pady=5)
entry_seconds = ttk.Entry(frame_dms_dd, width=5)    
entry_seconds.pack(side="left", padx=5, pady=5)
ttk.Button(frame_dms_dd, text="Convertir", command=convert_dms_a_dd).pack(side="left", padx=5, pady=5)
result_dms_dd = tk.StringVar()
ttk.Label(frame_dms_dd, textvariable=result_dms_dd).pack(side="left", padx=5, pady=5)

# Botón para limpiar entradas
ttk.Button(ventana, text="Limpiar", command=clean_entries).pack(pady=10)

# atajos  de teclado
ventana.bind("<Return>", lambda event: convert_dd_a_dms())
ventana.bind("<Escape>", lambda event: clean_entries()) 
ventana.mainloop()
# Iniciar la aplicación
root.mainloop()