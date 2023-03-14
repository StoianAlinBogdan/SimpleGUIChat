import PySimpleGUI as sg

menu_def = [["&File"], ["&Help"], ["&Exit"]]

AppFont = "Any 16"

layout_main = [
    [sg.Menu(menu_def, key="-MENU-", font=AppFont)],
    [sg.Multiline(size=(100, 30), key="-TEXT-", no_scrollbar=True, expand_x=True, expand_y=True, disabled=True), 
    sg.Listbox(values=[], key="-USERS-", size=(30, None), expand_y=True, expand_x=True)],
    [sg.InputText(size=(100, 3), key="-INPUT-", enable_events=True, expand_x=True, expand_y=True),
     sg.Button("Send", key="-SEND-"), sg.Button("Add Attachment", key="-ATTACH-")]
]

layout_login = [
    [sg.Text("Insert your Username:")],
    [sg.InputText(size=(50,1), key="-USERNAME-", enable_events=True, expand_x=True)],
    [sg.Button("Login", key="-LOGIN-")]
]