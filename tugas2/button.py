import PySimpleGUI as sg

sg.theme("LightPink")
sg.theme_text_color("#FF69B4")

window = sg.Window("Contoh Button",
    layout=[[sg.Text("Contoh Button", text_color="#FF69B4")],
            [sg.Button("Button Simpan")],
            [sg.Button("Button Keluar")]],
    size=(400, 200),
    font=("Arial", 20))

kejadian, nilai = window.read()
print(kejadian, "=", nilai)

window.close()