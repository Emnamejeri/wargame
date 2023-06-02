import random

cards = {
    "Hearts": {
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2
    },
    "Diamonds": {
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2
    },
    "Clubs": {
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2
    },
    "Spades": {
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2
    }
}

# To shuffle cards and assign them randomly to each player
class DistributeCards:
    print("Let's start a War Game!!! remember you can always exit the game by clicking ctrl D or cmd D \n\n")
    def __init__(self, cards):
        self.cards = cards
        self.game_cards = []
        self.player_one_cards = []
        self.player_two_cards = []
    def distribute(self):
        for suit, ranks in self.cards.items():
            for rank, value in ranks.items():
                self.game_cards.append(f"{suit}, {rank}: {value}")
        
        random.shuffle(self.game_cards)
        
        self.player_one_cards = self.game_cards[:26]
        self.player_two_cards = self.game_cards[26:]
        
        return self.player_one_cards, self.player_two_cards

# To take a card from players and compare them
class GameBattle:
    def __init__(self, player_one_cards, player_two_cards):
        self.player_one_cards = player_one_cards
        self.player_two_cards = player_two_cards

    def draw_compare_cards(self):
        player_one_pick = [self.player_one_cards[0]]
        player_two_pick = [self.player_two_cards[0]]
        card_value_player1 = int(self.player_one_cards[0].split(": ")[1])
        card_value_player2 = int(self.player_two_cards[0].split(": ")[1])
        print("player one draws ", player_one_pick, "valued at: ", card_value_player1, "points\n\n")
        print("player two draws ", player_two_pick, "valued at: ", card_value_player2, "points\n\n")
        
        if card_value_player1 < card_value_player2:
            self.player_two_cards.append(player_one_pick.pop(0))
        elif card_value_player1 > card_value_player2:
            self.player_one_cards.append(player_two_pick.pop(0))
        else:
            print("Start a War")
            self.war_game()
        print("First player new deck is: ", self.player_one_cards, "\n\n")
        print("Second player new deck is: ", self.player_two_cards, "\n\n")
    
    def war_game(self):
        player_one_pick = [self.player_one_cards[1:3]]
        player_two_pick = [self.player_two_cards[1:3]]
        print("First player draw: ", player_one_pick, "\n\n")
        print("Second player draw: ", player_two_pick, "\n\n")
        card_value_player1 = self.player_one_cards[1:3].split(": ")[1]
        card_value_player2 = self.player_two_cards[1:3].split(": ")[1]
        if card_value_player1 < card_value_player2:
            self.player_two_cards.append(player_one_pick.pop(0))
        elif card_value_player1 > card_value_player2:
            self.player_one_cards.append(player_two_pick.pop(0))
        else:
            print("start a battle")
            self.war_game()


def announce_winner(player_one_cards, player_two_cards):
    try: 
        score_player_one = len(player_one_cards)
        score_player_two = len(player_two_cards)
        if score_player_one == 52:
            print("Game over: winner is Player one")
        elif score_player_two == 52:
            print("Game over: winner is Player two")
    except EOFError:
        if score_player_one < score_player_two:
            print("Game Ended and the winner is player Two")
        elif score_player_one > score_player_two: 
            print("Game Ended and the winner is player one")
        else: 
            print("Game Ended and it's a draw")
    announce_winner(player_one_cards, player_two_cards)

# Create an instance of DistributeCards and distribute the cards
distributor = DistributeCards(cards)
player_one_cards, player_two_cards = distributor.distribute()

# Create an instance of GameBattle and compare the cards
battle = GameBattle(player_one_cards, player_two_cards)
battle.draw_compare_cards()

