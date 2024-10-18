import PySimpleGUI as sg
sg.theme("Darkpurple4")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("NPM   : 2210010667")],
                            [sg.Text("NAMA  : Muhammad Albar")],
                            [sg.Text("KELAS : 5M REGULAR BANJARMASIN")],
                            [sg.Text("MATKUL    : Pemrograman Visual 3")]
                            
                            ], size=(400,200))
window()
window.close()