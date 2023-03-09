import PySimpleGUI as sg
from layouts import layout_main

_VARS = {
    'window': False,
    "data_to_send": [],
    "data_to_display": []
    }

def main_loop():
    _VARS["window"] = sg.Window("MainWindow", layout_main, finalize=True, resizable=True)
    _VARS["window"]["-INPUT-"].bind("<Return>", "_Enter")
    while True:
        event, values = _VARS['window'].read(timeout=500)
        print(event)
        print(values)
        print(_VARS)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "-SEND-" or event == "-INPUT-_Enter":
            data = values['-INPUT-']
            _VARS["data_to_send"].append(data)
            _VARS["window"].find_element("-INPUT-").update("")
        if _VARS["data_to_display"]:
            _VARS["window"]["-TEXT-"].update(_VARS["window"]["-TEXT-"].get() + "\n" + str(_VARS["data_to_display"].pop()))


if __name__ == "__main__":
    main_loop()
