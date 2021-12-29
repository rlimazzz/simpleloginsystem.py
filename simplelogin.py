import PySimpleGUI as sg
sg.theme('Topanga') #the colorscheme of pysimplegui, you can see more themes in the cookbook

def principalapp():
    layout = [[sg.Text('Enter your user and password :'), sg.Text(size = (25, 1),key = '-OUTPUT-')],
             [sg.Text('user:'), sg.Input(key= '-NAME-')],
             [sg.Text('password:'), sg.Input(key='-IN-')],
             [sg.Button('Check'), sg.Button('Exit'), sg.Button('Show Message')]]

    window = sg.Window('Simple Login System', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Check':
            if(values['-IN-'] == 'ryserk' and values['-NAME-'] == '123'): #here you can define your user and password inside the quotation marks
                window['-OUTPUT-'].update("Connection accepted")
            else:
                window['-OUTPUT-'].update("Connection not accepted")
        if event == 'Show Message':
            sg.popup('Hello {}'.format(values['-NAME-'])) #this line will show a popup with a message for the user

    window.close()


principalapp()

