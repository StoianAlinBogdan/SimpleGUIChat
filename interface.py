import PySimpleGUI as sg
from layouts import layout_main, layout_login

_VARS = {
    'window': False,
    "data_to_send": [],
    "data_to_display": [],
    "usernames": [],
    "user": None
    }

def make_login_window():
    return sg.Window("Login Window", layout_login, finalize=True)

def main_loop():
    _VARS["window"] = sg.Window("MainWindow", layout_main, finalize=True, resizable=True)
    _VARS["window"]["-INPUT-"].bind("<Return>", "_Enter")
    _VARS["window"].disable()
    _VARS["login_window"] = make_login_window()
    while True:
        event, values = _VARS['window'].read(timeout=500)
        if _VARS["login_window"]:
            event2, values2 = _VARS["login_window"].read(timeout=500)
        print(event)
        print(values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "-SEND-" or event == "-INPUT-_Enter":
            data = values['-INPUT-']
            _VARS["data_to_send"].append(data)
            _VARS["window"].find_element("-INPUT-").update("")
        if _VARS["data_to_display"]:
            _VARS["window"]["-TEXT-"].update(_VARS["window"]["-TEXT-"].get() + "\n" + str(_VARS["data_to_display"].pop()))
        if event2 == "-LOGIN-":
            username = _VARS['login_window']["-USERNAME-"].get()
            _VARS["user"] = username
            _VARS["login_window"].close()
            _VARS["window"].enable()


if __name__ == "__main__":
    main_loop()
