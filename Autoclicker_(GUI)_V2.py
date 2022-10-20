import time 
import keyboard
from pynput.mouse import Button, Controller
import PySimpleGUI as sg
import random as rndom      #random is already a variable

error = False
seper = 60*"-"+"\n"
mouse = Controller()
sg.theme("Dark Grey 13")
helpText = (f"""
    ~~~~~~GG's Autoclicker help~~~~~~\n\nCps slider: Set your desired clicks per second
    {seper}Hotkey: The button on your keyboard to activate the autoclicker. \nYou can set it to every one-character-key (example: 'a', '1', '#' or '<'). \nThe spacebar can also be the hotkey.
    {seper}Mouse button: Select the mouse button that gets clicked.
    {seper}Infinite Cps mode: Clicks as fast as your Computer can. \nShould be around 600 clicks per second
    {seper}Random Cps mode: Varies the interval between clicks. \nMakes it harder for anticheat to detect the autoclicker.
    {seper}Info: To change settings without restarting the program, \njust press 'Start' again.\n\n\nWarning: The autoclicker can heavily affect Cpu performance.\n\nGet the source code on Github: https://github.com/GrosserGueffel\n©2022 Grosser_Gueffel aka GG
""")
    
#prevents the window from becoming unresponsive (also look in line 79)
def long_operation_logic():
    while True:     
        if keyboard.is_pressed(hotkey):
            print("Debug: Pressed hotkey")
            if buttonleft == True:
                mouse.click(Button.left, 1)
            else:
                mouse.click(Button.right, 1)
            if infinite == False and random == False:
                time.sleep(1/values.get("cps"))
                
            elif infinite == False and random == True:
                time.sleep(1/values.get("cps")+rndom.randint(int(-0.1),int(0.1)))
            elif infinite == True and random == False:      #is somehow faster
                pass                                        #      ''

#Gui window layout
layout = [
    [sg.Text("GG's Autoclicker V1", size=(25, 1),font=("Fixedsys",20),relief=sg.RELIEF_RIDGE)],
    [sg.Frame(layout=[
        [sg.Text("Cps"),sg.Text("",size=(13,1)),sg.Button("Help")],
        [sg.Slider(key="cps",range=(1,100),default_value=5,size=(20,15),orientation='horizontal',)],
        [sg.Text("Select hotkey")],
        [sg.InputText('v',key="hotkey",size=(5,1),text_color="yellow")],
        [sg.Text("Mouse button")],
        [sg.Radio("Left","buttonchoice",key="buttonleft",size=(5,1),default=True),sg.Radio("Right","buttonchoice",size=(5,1))],
        [sg.Text("Infinite Cps mode",size=(18,1)),sg.Checkbox("", key="infinite")],
        [sg.Text("Random Cps mode",size=(18,1)),sg.Checkbox("", key="random",size=(0,0))],
        ], title='Options',title_color='yellow',size=(400,250), relief=sg.RELIEF_SUNKEN)], [sg.Button("Start"), sg.Text("Click start to continue", size=(25,1), text_color="yellow",relief=sg.RELIEF_SUNKEN), sg.Button("Close",key="close")],
        [sg.Text("Click *start* again to update settings\n©2022 GG",size=(50,2))]       
]
#opens window
window = sg.Window('Autoclicker', layout, auto_size_text=False, auto_size_buttons=False, default_element_size=(20,1), text_justification='left',font="Fixedsys")

#gets events (pressed buttons)
while True:
    event, values = window.read()
    if event in ('Exit', 'Quit', None):
        print("Debug: exit")
        break
    elif event == "Start":
        print("Debug: start")
        print("Debug: values",values)
        hotkey = values.get("hotkey")
        infinite = values.get("infinite")
        random = values.get("random")
        buttonleft = values.get("buttonleft")
        print("Debug: Hotkey is",hotkey)
        try:
            keyboard.is_pressed(hotkey)
        except ValueError:
            error = True
        if len(values.get("hotkey")) > 1 or error == True:
            window.Element("hotkey").update(values["hotkey"][:-1])
            sg.popup_ok("Hotkey can only be 1 character long.\nProgram will close...",title="Error")
            window.close()
            exit()
        window.perform_long_operation(long_operation_logic,"") #also look in line 20

    elif event == "Help":
        print("Debug: Pressed 'Help'")
        sg.popup_scrolled(helpText,title="Help")

    elif event == "close":
        window.close()
        print("Debug: close")
        exit()

#https://github.com/GrosserGueffel
#finished 09.10.2022 GG