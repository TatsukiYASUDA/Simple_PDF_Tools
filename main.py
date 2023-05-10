import ctypes
import os
import subprocess

import PySimpleGUI as sg

from pdf_process import pdf_merge, pdf_rotate, pdf_split

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass


def open_folder(path: str) -> None:
    path = path.replace("/", os.sep)
    subprocess.Popen(["explorer", path], shell=True)


sg.theme("BlueMono")
font = ("Yu Gothic UI", 10)

# fmt:off
tab1_layout = [
    [sg.T("フォルダ内のPDFファイルは名前順に結合されます", font=font)],
    [sg.T("Folder :", s=(5, 1)), sg.In(s=(30, 1)), sg.FolderBrowse("選択", k="FolderPath")],
    [sg.T("【ファイルの上書きに注意】 ", font=font)],
    [sg.T("保存名: (フォルダ名).pdf", font=font)],
]

tab2_layout = [
    [sg.T("ファイルを一つ選択し、分割します", font=font)],
    [sg.T("File :", s=(4, 1)), sg.In(s=(30, 1)), sg.FileBrowse("選択", k="FilePath_split", file_types=[("PDF files", "*.pdf")], s=(4, 1))],
    [sg.T("【ファイルの上書きに注意】", font=font)],
    [sg.T("保存名: (ファイル名)_001, 002,... .pdf", font=font)],
]

tab3_layout = [
    [sg.T("ファイルを一つ選択し、回転します", font=font)],
    [sg.T("File :", s=(4, 1)), sg.In(s=(30, 1)), sg.FileBrowse("選択", k="FilePath_rotate", file_types=[("PDF files", "*.pdf")], s=(4, 1))],
    [sg.T("Angle (clockwise):"), sg.Combo([90, 180, 270, 360], 90, k="angle", s=(8, 1))],
    [sg.T("【ファイルの上書きに注意】 保存名: (ファイル名)_roll.pdf", font=font)],
]

layout = [
    [sg.TabGroup([[
        sg.Tab("結合", tab1_layout, element_justification="center", k="merge"),
        sg.Tab("分割", tab2_layout, element_justification="center", k="split"),
        sg.Tab("回転", tab3_layout, element_justification="center", k="rotate"),
    ]], k="tab_group", font=font)],
    [sg.Column([[sg.Button("実行", k="execution", s=(18, 1))]], justification="r")],
]
# fmt:on

window = sg.Window("PDF Tools", layout, location=(10, 10), keep_on_top=True)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "execution":
        is_done = False
        if values["tab_group"] == "merge":
            folder_path = values["FolderPath"]
            if pdf_merge(folder_path):
                is_done = True
                open_folder(os.path.dirname(folder_path))

        elif values["tab_group"] == "split":
            pdf_path = values["FilePath_split"]
            if pdf_split(pdf_path):
                is_done = True
                open_folder(os.path.dirname(pdf_path))

        elif values["tab_group"] == "rotate":
            pdf_path = values["FilePath_rotate"]
            angle = int(values["angle"])
            if pdf_rotate(pdf_path, angle):
                is_done = True
                open_folder(os.path.dirname(pdf_path))

        if not is_done:
            sg.popup("Error")

window.close()
