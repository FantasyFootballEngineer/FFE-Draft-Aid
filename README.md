# FFE-Draft-Aid

This drafting tool optimizes your lineup according to the players remaining on the draft board and the average value of replacement for each position.

This is a Work-in-Progress


Directions:

First, make sure the CSV file with your projections are in the same folder as the code and named "player_rankings.csv". Note that the logic of the optimization works based on season-long point projections for each draftable player. I wrote the code around GridironAI.com's projections, and would highly recommend using those, but as they are proprietary I did not include them in this GitHub. If you use a different projections file, make sure to edit the CSV sections accordingly.

The drafting tool GUI is designed to be used side by side with your drafting window. Enter the names of the players drafted by other team owners as they come off the draft board in the text box, and when it is your turn to draft click the "Draft a Player" button to recieve the optimized pick for yourself.

Note that if you do not like the player that the algorithm picks for you, you can click the "No" button to see the next highest rated player at each position. If you have a specific player whom you want to draft, you can also enter them into the new text box on the Manual Drafter window.
