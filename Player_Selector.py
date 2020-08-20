def Player_selector(data, QBs, RBs, WRs, TEs, Positions_Remaining):
    ## This function will determine the best player to draft
    ## Method: Select the top player, and fill the remaining draft spots with value of replacement for the respective position
    ## Compare which top positional player will give you the highest points


    ## Import the functions
    from QB_Selector import QB_Selector
    from RB_Selector import RB_Selector
    from WR_Selector import WR_Selector
    from TE_Selector import TE_Selector


    ## Call the functions 
    QB_Name, QB_Value_Over_Replacement, QB_Replacement_Value = QB_Selector(data,QBs)
    RB_Name, RB_Value_Over_Replacement, RB_Replacement_Value = RB_Selector(data,RBs)
    WR_Name, WR_Value_Over_Replacement, WR_Replacement_Value = WR_Selector(data,WRs)
    TE_Name, TE_Value_Over_Replacement, TE_Replacement_Value = TE_Selector(data,TEs)

    ## Calculate positional values
    # Case 1: QB Select
    if Positions_Remaining[0] == 0:
        QB_Select_Value = 0
    if Positions_Remaining[0] == 1:     
        QB_Select_QBs = QB_Value_Over_Replacement
        QB_Select_RBs = RB_Replacement_Value * Positions_Remaining[1]
        QB_Select_WRs = WR_Replacement_Value * Positions_Remaining[2]
        QB_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        QB_Select_Value = QB_Select_QBs + QB_Select_RBs + QB_Select_WRs + QB_Select_TEs
    if Positions_Remaining[0] == 2:
        QB_Select_QBs = QB_Value_Over_Replacement + QB_Replacement_Value
        QB_Select_RBs = RB_Replacement_Value * Positions_Remaining[1]
        QB_Select_WRs = WR_Replacement_Value * Positions_Remaining[2]
        QB_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        QB_Select_Value = QB_Select_QBs + QB_Select_RBs + QB_Select_WRs + QB_Select_TEs


    # Case 2: RB Select
    if Positions_Remaining[1] == 0:
        RB_Select_Value = 0
    if Positions_Remaining[1] == 1:
        RB_Select_QBs = QB_Replacement_Value * Positions_Remaining[0]
        RB_Select_RBs = RB_Value_Over_Replacement
        RB_Select_WRs = WR_Replacement_Value * Positions_Remaining[2]
        RB_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        RB_Select_Value = RB_Select_QBs + RB_Select_RBs + RB_Select_WRs + RB_Select_TEs
    if 2 <= Positions_Remaining[1] <= 5:
        RB_Select_QBs = QB_Replacement_Value * Positions_Remaining[0]
        RB_Select_RBs = RB_Value_Over_Replacement + (RB_Replacement_Value * Positions_Remaining[1])
        RB_Select_WRs = WR_Replacement_Value * Positions_Remaining[2]
        RB_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        RB_Select_Value = RB_Select_QBs + RB_Select_RBs + RB_Select_WRs + RB_Select_TEs

    # Case 3: WR Select
    if Positions_Remaining[2] == 0:
        WR_Select_Value = 0
    if Positions_Remaining[2] == 1:
        WR_Select_QBs = QB_Replacement_Value * Positions_Remaining[0]
        WR_Select_RBs = RB_Replacement_Value * Positions_Remaining[1]
        WR_Select_WRs = WR_Value_Over_Replacement
        WR_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        WR_Select_Value = WR_Select_QBs + WR_Select_RBs + WR_Select_WRs + WR_Select_TEs
    if 2 <= Positions_Remaining[2] <= 5:
        WR_Select_QBs = QB_Replacement_Value * Positions_Remaining[0]
        WR_Select_RBs = RB_Replacement_Value * Positions_Remaining[1]
        WR_Select_WRs = WR_Value_Over_Replacement + (WR_Replacement_Value * Positions_Remaining[2])
        WR_Select_TEs = TE_Replacement_Value * Positions_Remaining[3]
        WR_Select_Value = WR_Select_QBs + WR_Select_RBs + WR_Select_WRs + WR_Select_TEs

    # Case 4: TE Select
    if Positions_Remaining[3] == 0:
        TE_Select_Value = 0
    if Positions_Remaining[3] == 1:     
        TE_Select_QBs = QB_Replacement_Value * Positions_Remaining[0]
        TE_Select_RBs = RB_Replacement_Value * Positions_Remaining[1]
        TE_Select_WRs = WR_Replacement_Value * Positions_Remaining[2]
        TE_Select_TEs = TE_Value_Over_Replacement
        TE_Select_Value = TE_Select_QBs + TE_Select_RBs + TE_Select_WRs + TE_Select_TEs

    ## Determine which is the highest value, and output who to draft
    Positional_values = [QB_Select_Value,RB_Select_Value,WR_Select_Value,TE_Select_Value]
    Max_value = max(Positional_values)

    # Case 1: QB Select:
    if Max_value == Positional_values[0]:
        Player_Name = QB_Name
        Player_Position = 'QB'
    # Case 2: RB Select:
    if Max_value == Positional_values[1]:
        Player_Name = RB_Name
        Player_Position = 'RB'
    # Case 3: WR Select:
    if Max_value == Positional_values[2]:
        Player_Name = WR_Name
        Player_Position = 'WR'
    # Case 4: TE Select:
    if Max_value == Positional_values[3]:
        Player_Name = TE_Name
        Player_Position = 'TE'

    return(Player_Name,Player_Position)