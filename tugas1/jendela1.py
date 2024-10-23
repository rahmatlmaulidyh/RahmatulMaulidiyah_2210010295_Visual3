import PySimpleGUI as sg
sg.theme("DarkPurple3")
sg.theme_text_color("#bda961")
window = sg.Window(title="Profile",
    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
            font=("Arial",25,"italic","bold","underline"))],
            [sg.Text("NPM        : 2210010391 ")],
            [sg.Text("Nama       : Rahmatul Maulidiyah ")],
            [sg.Text("Kelas      : 5B NonRegular Banjarmasin ")],
            ],
    size=(510,200),
    font=("Times", 18))

window()
window.close()
