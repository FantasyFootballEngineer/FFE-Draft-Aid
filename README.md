# FFE-Draft-Aid

This drafting tool optimizes your lineup according to the players remaining on the draft board and the average value of replacement for each position.

This is a Work-in-Progress


Directions:

The logic of the optimization works based on season-long point projections for each draftable player. I wrote the code around GridironAI.com's projections, and would highly recommend using those (the most recent projections at the time of writing this are included in the GitHub). Note that at the time of writing this, the projections did not include rookies. If you use wish to use a different projections file, make sure to edit the CSV section of the code accordingly. Huge shoutout to the folk over at GridironAI for the projections.

In the first GUI, select the scoring format and the number of players that you wish to draft per position. Make sure to enter the number in number format, ie "5" and not "Five".

The drafting tool GUI is designed to be used side by side with your drafting window. Enter the names of the players drafted by other team owners as they come off the draft board in the text box, and when it is your turn to draft click the "Draft a Player" button to recieve the optimized pick for yourself.

Note that if you do not like the player that the algorithm picks for you, you can click the "No" button to see the next highest rated player at each position. If you have a specific player whom you want to draft, you can also enter them into the new text box on the Manual Drafter window.
