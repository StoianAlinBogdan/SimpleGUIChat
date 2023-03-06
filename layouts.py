import PySimpleGUI as sg

menu_def = [["&File"], ["&Help"], ["&Exit"]]

AppFont = "Any 16"

layout_main = [
    [sg.Menu(menu_def, key="-MENU-", font=AppFont)],
    [sg.Multiline(size=(100, 30), key="-TEXT-", no_scrollbar=True, expand_x=True, expand_y=True), 
    sg.Listbox(values=["First", "Second", "Third"], key="-LISTBOX-", size=(30, None), expand_y=True, expand_x=True)],
    [sg.Multiline(size=(100, 3), key="-INPUT-", no_scrollbar=True, expand_x=True, expand_y=True),
     sg.Button("Send", key="-SEND-"), sg.Button("Add Attachment", key="-ATTACH-")]
]