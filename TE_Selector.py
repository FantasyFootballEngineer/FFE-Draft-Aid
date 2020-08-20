def TE_Selector(data,TEs):
    ## This function evaluates the average value of remaining Tight Ends and the value over replacement of the top remaining Tight End
    ## Value of replacement includes three variables - average projected score of top all players in that position in the top 100 players, the projected score of 
    ## the positional player right before the current top player, and the projected score of the positional player right after the current top player
    ## Take the average of those three values to get the Value of Replacement variable
    
    from statistics import mean 

    #Find highest ranked TE remaining on overall list, and determine their rank
    data_length = len(data)
    TEs_length = len(TEs)
    TE_Name = ''
    for i in range(data_length):  
        if data[i][1] == 'TE':
            x = i
            TE_Name = data[i][0]
            break

    for i in range(TEs_length):
        if data[x][0] == TEs[i][0]:
            Rank = i

    #Average the TEs from the top 100 list        
    Top_100_TEs = []
    for i in range(data_length):
        if data[i][1] == 'TE':
            Top_100_TEs.append(data[i][2])
    TE_average = sum(Top_100_TEs)/len(Top_100_TEs)

    #Calculate the replacement value
    if Rank == 0:
        TE_RankUp = TEs[0][2]
        TE_RankDown = TEs[1][2]
        TE_data = (TE_average,TE_RankDown,TE_RankUp)
        TE_Replacement_Value = mean(TE_data)
    else:
        for i in range(len(TEs)):
            if TE_Name == TEs[i][0]:
                TE_RankUp = TEs[i-1][2]
                TE_RankDown = TEs[i+1][2]
                TE_data = (TE_average,TE_RankDown,TE_RankUp)
                TE_Replacement_Value = mean(TE_data)

    # Calculate the value of replacement
    TE_Value_Over_Replacement = TEs[Rank][2] - TE_Replacement_Value

    return (TE_Name,TE_Value_Over_Replacement,TE_Replacement_Value)