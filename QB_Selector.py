def QB_Selector(data,QBs):
    ## This function evaluates the average value of remaining Tight Ends and the value over replacement of the top remaining Tight End
    ## Value of replacement includes three variables - average projected score of top all players in that position in the top 100 players, the projected score of 
    ## the positional player right before the current top player, and the projected score of the positional player right after the current top player
    ## Take the average of those three values to get the Value of Replacement variable
    
    from statistics import mean 

    #Find highest ranked QB remaining on overall list, and determine their rank
    data_length = len(data)
    QBs_length = len(QBs)
    QB_Name = ''
    for i in range(data_length):  
        if data[i][1] == 'QB':
            x = i
            QB_Name = data[i][0]
            break

    for i in range(QBs_length):
        if data[x][0] == QBs[i][0]:
            Rank = i

    #Average the QBs from the top 100 list        
    Top_100_QBs = []
    for i in range(data_length):
        if data[i][1] == 'QB':
            Top_100_QBs.append(data[i][2])
    QB_average = sum(Top_100_QBs)/len(Top_100_QBs)

    #Calculate the replacement value
    if Rank == 0:
        QB_RankUp = QBs[0][2]
        QB_RankDown = QBs[1][2]
        QB_data = (QB_average,QB_RankDown,QB_RankUp)
        QB_Replacement_Value = mean(QB_data)
    else:
        for i in range(len(QBs)):
            if QB_Name == QBs[i][0]:
                QB_RankUp = QBs[i-1][2]
                QB_RankDown = QBs[i+1][2]
                QB_data = (QB_average,QB_RankDown,QB_RankUp)
                QB_Replacement_Value = mean(QB_data)

    # Calculate the value of replacement
    QB_Value_Over_Replacement = QBs[Rank][2] - QB_Replacement_Value

    return (QB_Name,QB_Value_Over_Replacement,QB_Replacement_Value)