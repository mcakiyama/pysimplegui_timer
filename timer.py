import PySimpleGUI as sg
from playsound import playsound
sg.theme('Python')   # Design theme Setting

# Components on Window
layout = [  [sg.Button('1s'), sg.Button('1min'), sg.Button('5min'), sg.Button('10min')],
            [sg.Text(size=(8, 1), font=('Helvetica', 20),justification='center', key='-jikan-'),
             sg.Text(size=(10, 1), font=('Helvetica', 14),justification='center', key='-Repeat-'),],
            [sg.Button('Start'), sg.Button('Stop'), sg.Button('Reset'), sg.Button('Repeat'), sg.Button('Close')],
            [sg.Text('© OtoLogic', size=(10, 1), font=('Helvetica', 9),justification='left')] ]

# Generate Window
window = sg.Window('Timer App', layout)

# Initialize variables
timer = 0
timer_disp = 0
saved_timer = 60
isRunning = False
rpt = False
rpt_text = 'Repeat:OFF'

# Event loop
while True:
    event, values = window.read(timeout=100,timeout_key='-timeout-')
    window['-jikan-'].update(timer_disp)
    window['-Repeat-'].update(rpt_text)
    

    if event == sg.WIN_CLOSED or event == 'Close':
        break

    # Add timer counts
    elif event == '1s' or event == '1min' or event == '5min' or event == '10min':
        if event == '1min':
            timer = timer + 600
        elif event == '5min':
            timer = timer + 600*5
        elif event == '10min':
            timer = timer + 600*10        
        elif event == '1s':
            timer = timer + 10
        
    # Button event
    elif event == 'Start':
        saved_timer = timer
        isRunning = True
    elif event == 'Stop':
        isRunning = False
    elif event == 'Reset':
        isRunning = False
        timer = 0 
        saved_timer = 0
    elif event == 'Repeat':
        rpt = not rpt
        if rpt:
            rpt_text = 'Repeat:ON'
        else:
            rpt_text = 'Repeat:OFF'


    # Event at timer stop
    elif timer<=0 and isRunning:
        if not rpt or saved_timer==0:
            isRunning = False
            timer = 0
        else:
            isRunning = True
            timer = saved_timer
        
        if not saved_timer==0:
            playsound("assets/Flexatone03-1(Mid).mp3")

    # Timer decriment
    elif event in '-timeout-' and isRunning:
        timer = timer - 1
    
    timer_disp = int(timer / 10)
        
window.close()
