def WR_Selector(data,WRs):
    ## This function evaluates the average value of remaining Tight Ends and the value over replacement of the top remaining Tight End
    ## Value of replacement includes three variables - average projected score of top all players in that position in the top 100 players, the projected score of 
    ## the positional player right before the current top player, and the projected score of the positional player right after the current top player
    ## Take the average of those three values to get the Value of Replacement variable
    
    from statistics import mean 

    #Find highest ranked WR remaining on overall list, and determine their rank
    data_length = len(data)
    WRs_length = len(WRs)
    WR_Name = ''
    for i in range(data_length):  
        if data[i][1] == 'WR':
            x = i
            WR_Name = data[i][0]
            break

    for i in range(WRs_length):
        if data[x][0] == WRs[i][0]:
            Rank = i

    #Average the QBs from the top 100 list        
    Top_100_WRs = []
    for i in range(data_length):
        if data[i][1] == 'WR':
            Top_100_WRs.append(data[i][2])
    WR_average = sum(Top_100_WRs)/len(Top_100_WRs)

    #Calculate the replacement value
    if Rank == 0:
        WR_RankUp = WRs[0][2]
        WR_RankDown = WRs[1][2]
        WR_data = (WR_average,WR_RankDown,WR_RankUp)
        WR_Replacement_Value = mean(WR_data)
    else:
        for i in range(len(WRs)):
            if WR_Name == WRs[i][0]:
                WR_RankUp = WRs[i-1][2]
                WR_RankDown = WRs[i+1][2]
                WR_data = (WR_average,WR_RankDown,WR_RankUp)
                WR_Replacement_Value = mean(WR_data)

    # Calculate the value of replacement
    WR_Value_Over_Replacement = WRs[Rank][2] - WR_Replacement_Value

    return (WR_Name,WR_Value_Over_Replacement,WR_Replacement_Value)