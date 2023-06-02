# Game summary: 
the game starts with a distribution of the 52 cards and splitting them in two. 
each player ends with 26 cards selected randomly. 
players pick a card from the top of their stack each. 
players cards are compared to determine if there is a battle or war based on the value of the card itself. 





# wargame
 children card game 
1. From a dictionary of dictionnaries create a list named game_cards with all the 52 cards names of the war game 
2. Create two empty lists to store cards of each player for playerOneCards and playerTwoCards (3 lists in total).
3. create a main function that has all the other sub functions and will ensure the game is played. 

3. create a function (distribute-cards) that will first shuffle the items in cards list THEN split them equally in two to Assign 26 cards to each player.
 
4. create a  function (battle-game) to prompt players for their first card one by one THEN compare it based on values
set two conditions: 1 in case cards are diffrent the card with the lowest value is appended to the list of the opnent player ELIF cards are equal a war starts by calling a function named war-game. 

5. Create a function war-game that pulls the first two cards from each of the players decks THEN returns two list with two card values where one card value is hidden and the other is shown THEN compare based on values again to determine if the war game function is to be prompted again or break and go for the battle. 

5. create an exception block so when user presses ctrl d or writes done the game is ended and player with highest count in their list/deck is announced winner






