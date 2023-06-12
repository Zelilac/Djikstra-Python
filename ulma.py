import tkinter as tk

def hitung_pbb():
    angka1 = int(entry1.get())
    angka2 = int(entry2.get())
    
    output_text.delete("1.0", tk.END)  # Menghapus teks sebelumnya (jika ada)
    output_text.insert(tk.END, "Proses Perbandingan a dan b:\n")
    
    while angka2 != 0:
        sisa = angka1 % angka2
        output_text.insert(tk.END, f"a: {angka1}, b: {angka2}\n")
        output_text.insert(tk.END, f"Sisa: {angka1} % {angka2} = {sisa}\n\n")
        angka1 = angka2
        angka2 = sisa
    
    result_label.config(text="PBB: " + str(angka1))

window = tk.Tk()
window.title("PBB Algoritma Euclidean")
window.geometry("300x400")  # Mengatur ukuran jendela

label1 = tk.Label(window, text="Angka 1:", font=("Consolas", 12))
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Angka 2:", font=("Consolas", 12))
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

calculate_button = tk.Button(window, text="Hitung PBB", command=hitung_pbb, bg="#4caf50", fg="white", font=("Consolas", 12))
calculate_button.pack()

result_label = tk.Label(window, text="PBB: ", font=("Consolas", 12))
result_label.pack()

output_text = tk.Text(window, height=8, width=30)
output_text.pack()

window.mainloop()
