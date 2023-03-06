import PySimpleGUI as sg
from layouts import layout_main

_VARS = {
    'window': False
    }

def main_loop():
    _VARS["window"] = sg.Window("MainWindow", layout_main, finalize=True, resizable=True)
    while True:
        event, values = _VARS['window'].read(timeout=500)
        print(event)
        print(values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "File":
            print("kys")
        

if __name__ == "__main__":
    main_loop()
