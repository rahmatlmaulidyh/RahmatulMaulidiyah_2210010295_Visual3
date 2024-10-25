import PySimpleGUI as sg

sg.theme("LightPink")
sg.theme_text_color("#FF69B4")

window = sg.Window(title="Profile",
                   layout=[[sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="center", text_color="#FF69B4")],
                           [sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="left", text_color="#FF69B4")],
                           [sg.Text("TEKNOLOGI INFORMASI ", size=(25, 1), justification="right", text_color="#FF69B4")],
                           [sg.Text("TEKNOLOGI INFORMASI " + ' ' * 2, size=(25, 2), justification="center", text_color="#FF69B4")],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FF69B4")]],
                   size=(400, 250),
                   font=("Arial", 18))

window.read()
window.close()