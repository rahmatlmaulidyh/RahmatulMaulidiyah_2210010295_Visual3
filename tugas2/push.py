import PySimpleGUI as sg

sg.theme("LightPink")
sg.theme_text_color("#FF69B4")

susunan = [
    [sg.Push(), 
     sg.Text("UNISKA MAAB", font=("Arial", 24), text_color="#FF69B4"), 
     sg.Push()],
    [sg.Push(),
     sg.Text("BANJARMASIN", font=("Arial", 18), text_color="#FF69B4"), 
     sg.Push()]
]

window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   size=(430, 200),
                   font=("Arial", 18))

window.read()
window.close()