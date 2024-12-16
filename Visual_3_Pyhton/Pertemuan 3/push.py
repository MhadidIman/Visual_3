import PySimpleGUI as sg
susunan=[[sg.Push(),
         sg.Text("UNISKA MAB",font=("helvatica",24)),
         sg.Push()],
        [sg.Push(),
         sg.Text("BANJARMASIN",font=("courier",18)),
         sg.Push()]
        ]
window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   size=(400,200))

window()
window.close()