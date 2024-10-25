import PySimpleGUI as sg

sg.theme("LightPink")
sg.theme_text_color("#FF69B4")

window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA", font=("Arial", 24), text_color="#FF69B4")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Arial", 18, "italic", "bold", "underline"), text_color="#FF69B4")],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FF69B4")]],
                   size=(430, 200),
                   font=("Arial", 18))

window.read()
window.close()