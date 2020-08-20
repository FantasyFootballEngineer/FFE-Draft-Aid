## This is my Draft Optimization Tool for the 2020 Fantasy Football Draft
## Must be used with a CSV file of player season-long point projections

## Import Modules
import csv
from statistics import mean
from Player_Selector import *
import PySimpleGUI as sg

## Create Initial GUI to give owner Draft Options
sg.theme('DarkAmber')   # Add a touch of color
initial_layout = [  [sg.Text('Customize your draft settings:')],
                    [sg.Text(' ')],
                    [sg.Text('Scoring Format:             '), sg.Button('Standard',key='Standard',button_color=('black', 'gray'), size=(10,1)), sg.Button('PPR',key='PPR',button_color=('black', 'gray'),size=(10,1))],
                    [sg.Text(' ')],
                    [sg.Text('Number of QBs desired: '), sg.InputText(key='Number_of_QBs')],
                    [sg.Text('Number of RBs desired: '), sg.InputText(key='Number_of_RBs')], 
                    [sg.Text('Number of WRs desired:'), sg.InputText(key='Number_of_WRs')], 
                    [sg.Text('Number of TEs desired: '), sg.InputText(key='Number_of_TEs')],
                    [sg.Text(' ')],
                    [sg.Button('Ok',bind_return_key=True)] ]


initial_window = sg.Window('Fantasy Football Draft Aid 2020', initial_layout)
# Event Loop to process "events" and get the "values" of the inputs
scoring_format = 0

while True:
    initial_event, initial_values = initial_window.read()
    if initial_event == sg.WIN_CLOSED:
        exit()
    if initial_event == 'Standard':
        scoring_format = 'player_rankings_standard.csv'
        initial_window.FindElement('Standard').Update(button_color=('black', 'yellow'))
        initial_window.FindElement('PPR').Update(button_color=('black', 'gray'))
    if initial_event == 'PPR':
        scoring_format = 'player_rankings_PPR.csv'
        initial_window.FindElement('PPR').Update(button_color=('black', 'yellow'))
        initial_window.FindElement('Standard').Update(button_color=('black', 'gray'))
    if initial_event == 'Ok':
        Number_of_QBs = int(initial_values['Number_of_QBs'])
        Number_of_RBs = int(initial_values['Number_of_RBs'])
        Number_of_WRs = int(initial_values['Number_of_WRs'])
        Number_of_TEs = int(initial_values['Number_of_TEs'])
        break


initial_window.close()
## Open CSV file with {player, position, projected points}, and convert it to a list
with open(scoring_format, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

## Delete unneeded rows
## Syntax for del --> del list_name[sub_list_number][item_from_sublist_number]
## ie --> del data[0][2] will delete the third item from the first sub list
del data[0]
data_length = len(data)
for i in range(data_length):
    x = float(data[i][7])
    for j in range(23, 2, -1):
        del data[i][j]
    del data[i][1]
    data[i].append(x)
## Delete random spaces after certain player's names
for i in range(data_length):
    length = len(data[i][0]) - 1
    # print(i)
    # print(length)
    # print(data[i][0])
    if data[i][0][length] == ' ':
        data[i][0] = data[i][0][:-1]

## Number of players from each position left to draft, ie 2 QBs, 5 RBs, 5 WRs, 1 TE
## Order: QB,RB,WR,TE
Positions_Remaining = [Number_of_QBs,Number_of_RBs,Number_of_WRs,Number_of_TEs]

## Break the data list into positional lists
data_length = len(data)
# QBs
QBs = []
for i in range(data_length):
    if data[i][1] == 'QB':
        QBs.append(data[i])
# RBs
RBs = []
for i in range(data_length):
    if data[i][1] == 'RB':
        RBs.append(data[i])
# WRs
WRs = []
for i in range(data_length):
    if data[i][1] == 'WR':
        WRs.append(data[i])
# TEs
TEs = []
for i in range(data_length):
    if data[i][1] == 'TE':
        TEs.append(data[i])

# Initialize Team
spacing = 50
My_QBs = []
My_RBs = []
My_WRs = []
My_TEs = []
for i in range(Number_of_QBs):
    My_QBs.append(' '*spacing)
for i in range(Number_of_RBs):
    My_RBs.append(' '*spacing)
for i in range(Number_of_WRs):
    My_WRs.append(' '*spacing)
for i in range(Number_of_TEs):
    My_TEs.append(' '*spacing)

## Create the Draft Tool GUI
# All the stuff inside your window.
layout = [  [sg.Text(' ')],
            [sg.Text(' ')],
            [sg.Text('Enter the name of the last player drafted')],
            [sg.Text('Player Name'), sg.InputText(key='input_player')],
            [sg.Button('Ok',bind_return_key=True), sg.Button('Draft a Player'), sg.Button('Cancel')],
            [sg.Text(' ')],
            [sg.Text(' ')], 
            [sg.Text('Your Team:')],
            [sg.Text('-' * 100)],
            [sg.Text('RBs:')],
            [sg.Text('1. '), sg.Text(My_RBs[0],key='RB_1')],
            [sg.Text('2. '), sg.Text(My_RBs[1],key='RB_2')],
            [sg.Text('3. '), sg.Text(My_RBs[2],key='RB_3')],
            [sg.Text('4. '), sg.Text(My_RBs[3],key='RB_4')],
            [sg.Text('5. '), sg.Text(My_RBs[4],key='RB_5')],
            [sg.Text('WRs:')],
            [sg.Text('1. '), sg.Text(My_WRs[0],key='WR_1')],
            [sg.Text('2. '), sg.Text(My_WRs[1],key='WR_2')],
            [sg.Text('3. '), sg.Text(My_WRs[2],key='WR_3')],
            [sg.Text('4. '), sg.Text(My_WRs[3],key='WR_4')],
            [sg.Text('5. '), sg.Text(My_WRs[4],key='WR_5')],
            [sg.Text('QBs:')],
            [sg.Text('1. '), sg.Text(My_QBs[0],key='QB_1')],
            [sg.Text('2. '), sg.Text(My_QBs[1],key='QB_2')],
            [sg.Text('TEs:')],
            [sg.Text('1. '), sg.Text(My_TEs[0],key='TE_1')] ]

# Create the Window
window = sg.Window('Fantasy Football Draft Aid 2020', layout, size=(400,1080))
window2_active = False
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':
        player_name = values['input_player']
        checker = 0
        for i in range(len(data)):
            if player_name == data[i][0]:
                del data[i]
                window['input_player'].update('')
                checker = 1
                break
        if checker == 0:
            sg.popup('Error: Not Valid Player')
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Draft a Player':
        Player_Name,Player_Position = Player_selector(data, QBs, RBs, WRs, TEs, Positions_Remaining)    
        decision = sg.PopupYesNo('You should draft:',Player_Name, Player_Position)

        if decision == 'Yes':
            #Delete Drafted Player from board
            for i in range(len(data)):
                if Player_Name == data[i][0]:
                    del data[i]
                    break

            #Update the remaining positions list with new player, and add player to "My Team List"
            if Player_Position == 'QB':
                Positions_Remaining[0] = Positions_Remaining[0] - 1
                for i in range(len(My_QBs)):
                    if My_QBs[i] == ' '*spacing:
                        My_QBs[i] = Player_Name
                        window['QB_1'].update(My_QBs[0])
                        window['QB_2'].update(My_QBs[1])
                        break
            if Player_Position == 'RB':
                Positions_Remaining[1] = Positions_Remaining[1] - 1
                for i in range(len(My_RBs)):
                    if My_RBs[i] == ' '*spacing:
                        My_RBs[i] = Player_Name
                        window['RB_1'].update(My_RBs[0])
                        window['RB_2'].update(My_RBs[1])
                        window['RB_3'].update(My_RBs[2])
                        window['RB_4'].update(My_RBs[3])
                        window['RB_5'].update(My_RBs[4])
                        break
            if Player_Position == 'WR':
                Positions_Remaining[2] = Positions_Remaining[2] - 1
                for i in range(len(My_WRs)):
                    if My_WRs[i] == ' '*spacing:
                        My_WRs[i] = Player_Name
                        window['WR_1'].update(My_WRs[0])
                        window['WR_2'].update(My_WRs[1])
                        window['WR_3'].update(My_WRs[2])
                        window['WR_4'].update(My_WRs[3])
                        window['WR_5'].update(My_WRs[4])
                        break
            if Player_Position == 'TE':
                Positions_Remaining[3] = Positions_Remaining[3] - 1
                My_TEs[0] = Player_Name
                window['TE_1'].update(My_TEs[0])
        
        if decision == 'No':

            ## Define next best at each position
            #QB:
            if Positions_Remaining[0] != 0:
                for i in range(len(data)): 
                    if data[i][1] == 'QB':
                        Next_QB = data[i][0]
                        break
            if Positions_Remaining[0] == 0:
                Next_QB = 'QB is full'
            #RB:
            if Positions_Remaining[1] != 0:
                for i in range(len(data)):
                    if data[i][1] == 'RB':
                        Next_RB = data[i][0]
                        break
            if Positions_Remaining[1] == 0:
                Next_RB = 'RB is full'
            #WR:
            if Positions_Remaining[2] != 0:
                for i in range(len(data)):
                    if data[i][1] == 'WR':
                        Next_WR = data[i][0]
                        break
            if Positions_Remaining[2] == 0:
                Next_WR = 'WR is full'
            #TE:
            if Positions_Remaining[3] != 0:
                for i in range(len(data)):
                    if data[i][1] == 'TE':
                        Next_TE = data[i][0]
                        break
            if Positions_Remaining[3] == 0:
                Next_TE = 'TE is full'

            window2_active = True
            layout2 = [ [sg.Text('Who do you want to draft?')],
                        [sg.Button(Next_QB), sg.Button(Next_RB), sg.Button(Next_WR), sg.Button(Next_TE)],
                        [sg.Text(' ')],
                        [sg.Text('Manual Input: Player Name'), sg.InputText(key='input_player2')],
                        [sg.Button('Ok',bind_return_key=True)] ]
            # layout2 = [[sg.Button('Remove QB'),sg.Button('Remove RB'),sg.Button('Remove WR'),sg.Button('Remove TE')]]
            window2 = sg.Window('Manual Drafter', layout2)
            while True:
                event2, values2 = window2.Read()
                if event2 == 'Ok':
                    Player_Name2 = values2['input_player2']
                    #Delete Drafted Player from board
                    for i in range(len(data)):
                        if Player_Name2 == data[i][0]:
                            Player_Position2 = data[i][1]
                            if Player_Position2 == 'QB':
                                var = 0
                            if Player_Position2 == 'RB':
                                var = 1
                            if Player_Position2 == 'WR':
                                var = 2
                            if Player_Position2 == 'TE':
                                var = 3
                            if Positions_Remaining[var] == 0:
                                sg.Popup('You have already selected the maximum number of ' + Player_Position2 + 's, select another position')
                            if Positions_Remaining[var] != 0:
                                del data[i]
                                break

                    #Update the remaining positions list with new player
                    if Player_Position2 == 'QB':
                        Positions_Remaining[0] = Positions_Remaining[0] - 1
                        for i in range(len(My_QBs)):
                            if My_QBs[i] == ' '*spacing:
                                My_QBs[i] = Player_Name2
                                window['QB_1'].update(My_QBs[0])
                                window['QB_2'].update(My_QBs[1])
                                break
                    if Player_Position2 == 'RB':
                        Positions_Remaining[1] = Positions_Remaining[1] - 1
                        for i in range(len(My_RBs)):
                            if My_RBs[i] == ' '*spacing:
                                My_RBs[i] = Player_Name2
                                window['RB_1'].update(My_RBs[0])
                                window['RB_2'].update(My_RBs[1])
                                window['RB_3'].update(My_RBs[2])
                                window['RB_4'].update(My_RBs[3])
                                window['RB_5'].update(My_RBs[4])
                                break
                    if Player_Position2 == 'WR':
                        Positions_Remaining[2] = Positions_Remaining[2] - 1
                        for i in range(len(My_WRs)):
                            if My_WRs[i] == ' '*spacing:
                                My_WRs[i] = Player_Name2
                                window['WR_1'].update(My_WRs[0])
                                window['WR_2'].update(My_WRs[1])
                                window['WR_3'].update(My_WRs[2])
                                window['WR_4'].update(My_WRs[3])
                                window['WR_5'].update(My_WRs[4])
                                break
                    if Player_Position2 == 'TE':
                        Positions_Remaining[3] = Positions_Remaining[3] - 1
                        My_TEs[0] = Player_Name2
                        window['TE_1'].update(My_TEs[0])
                    window2.Close()
                    window2_active = False
                    break

                if event2 == Next_QB:
                    if Next_QB == 'QB is full':
                        sg.Popup('You have already selected the maximum number of QBs, select another position')
                    if Next_QB != 'QB is full':
                        Player_Name2 = Next_QB
                        #Delete Drafted Player from board
                        for i in range(len(data)):
                            if Player_Name2 == data[i][0]:
                                del data[i]
                                break

                        #Update the remaining positions list with new player
                        Positions_Remaining[0] = Positions_Remaining[0] - 1
                        for i in range(len(My_QBs)):
                            if My_QBs[i] == ' '*spacing:
                                My_QBs[i] = Player_Name2
                                window['QB_1'].update(My_QBs[0])
                                window['QB_2'].update(My_QBs[1])
                                break
                        window2.Close()
                        window2_active = False
                        break      

                if event2 == Next_RB:
                    if Next_RB == 'RB is full':
                        sg.Popup('You have already selected the maximum number of RBs, select another position')
                    if Next_RB != 'RB is full':
                        Player_Name2 = Next_RB
                        #Delete Drafted Player from board
                        for i in range(len(data)):
                            if Player_Name2 == data[i][0]:
                                del data[i]
                                break

                        #Update the remaining positions list with new player
                        Positions_Remaining[1] = Positions_Remaining[1] - 1
                        for i in range(len(My_RBs)):
                            if My_RBs[i] == ' '*spacing:
                                My_RBs[i] = Player_Name2
                                window['RB_1'].update(My_RBs[0])
                                window['RB_2'].update(My_RBs[1])
                                window['RB_3'].update(My_RBs[2])
                                window['RB_4'].update(My_RBs[3])
                                window['RB_5'].update(My_RBs[4])
                                break                
                        window2.Close()
                        window2_active = False
                        break
                
                if event2 == Next_WR:
                    if Next_WR == 'WR is full':
                        sg.Popup('You have already selected the maximum number of WRs, select another position')
                    if Next_WR != 'WR is full':
                        Player_Name2 = Next_WR
                        #Delete Drafted Player from board
                        for i in range(len(data)):
                            if Player_Name2 == data[i][0]:
                                del data[i]
                                break

                        #Update the remaining positions list with new player
                        Positions_Remaining[2] = Positions_Remaining[2] - 1  
                        for i in range(len(My_WRs)):
                            if My_WRs[i] == ' '*spacing:
                                My_WRs[i] = Player_Name2
                                window['WR_1'].update(My_WRs[0])
                                window['WR_2'].update(My_WRs[1])
                                window['WR_3'].update(My_WRs[2])
                                window['WR_4'].update(My_WRs[3])
                                window['WR_5'].update(My_WRs[4])
                                break              
                        window2.Close()
                        window2_active = False
                        break

                if event2 == Next_TE:
                    if Next_TE == 'TE is full':
                        sg.Popup('You have already selected the maximum number of TEs, select another position')
                    if Next_TE != 'TE is full':
                        Player_Name2 = Next_TE
                        #Delete Drafted Player from board
                        for i in range(len(data)):
                            if Player_Name2 == data[i][0]:
                                del data[i]
                                break

                        #Update the remaining positions list with new player
                        Positions_Remaining[3] = Positions_Remaining[3] - 1
                        My_TEs[0] = Player_Name2
                        window['TE_1'].update(My_TEs[0])                
                        window2.Close()
                        window2_active = False
                        break                                        
window.close()