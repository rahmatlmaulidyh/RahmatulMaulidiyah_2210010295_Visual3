import PySimpleGUI as sg

sg.theme("LightPink")
sg.theme_text_color("#FF69B4")

susunan = [
    [sg.Text("UNISKA MAAB", font=("Arial", 24), text_color="#FF69B4")],
    [sg.Text("BANJARMASIN", font=("Arial", 18), text_color="#FF69B4")]
]

window = sg.Window(
    title="New Icon",
    layout=susunan,
    element_justification="center",
    icon="favicon.ico",
    resizable=True,
    size=(430, 200),
    font=("Arial", 18)
)

window.read()
window.close()