def RB_Selector(data,RBs):
    ## This function evaluates the average value of remaining Tight Ends and the value over replacement of the top remaining Tight End
    ## Value of replacement includes three variables - average projected score of top all players in that position in the top 100 players, the projected score of 
    ## the positional player right before the current top player, and the projected score of the positional player right after the current top player
    ## Take the average of those three values to get the Value of Replacement variable
    
    from statistics import mean 

    #Find highest ranked RB remaining on overall list, and determine their rank
    data_length = len(data)
    RBs_length = len(RBs)
    RB_Name = ''
    for i in range(data_length):  
        if data[i][1] == 'RB':
            x = i
            RB_Name = data[i][0]
            break

    for i in range(RBs_length):
        if data[x][0] == RBs[i][0]:
            Rank = i

    #Average the RBs from the top 100 list        
    Top_100_RBs = []
    for i in range(data_length):
        if data[i][1] == 'RB':
            Top_100_RBs.append(data[i][2])
    RB_average = sum(Top_100_RBs)/len(Top_100_RBs)

    #Calculate the replacement value
    if Rank == 0:
        RB_RankUp = RBs[0][2]
        RB_RankDown = RBs[1][2]
        RB_data = (RB_average,RB_RankDown,RB_RankUp)
        RB_Replacement_Value = mean(RB_data)
    else:
        for i in range(len(RBs)):
            if RB_Name == RBs[i][0]:
                RB_RankUp = RBs[i-1][2]
                RB_RankDown = RBs[i+1][2]
                RB_data = (RB_average,RB_RankDown,RB_RankUp)
                RB_Replacement_Value = mean(RB_data)

    # Calculate the value of replacement
    RB_Value_Over_Replacement = RBs[Rank][2] - RB_Replacement_Value

    return (RB_Name,RB_Value_Over_Replacement,RB_Replacement_Value)