import random
import sys

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

def announce_winner(player_one_cards, player_two_cards):
    try:
        score_player_one = len(player_one_cards)
        score_player_two = len(player_two_cards)
        if score_player_one == 52:
            print("Game over: The winner is Player One")
        elif score_player_two == 52:
            print("Game over: The winner is Player Two")
        else:
            if score_player_one < score_player_two:
                print("Game ended. The winner is Player Two")
            elif score_player_one > score_player_two:
                print("Game ended. The winner is Player One")
            else:
                print("Game ended. It's a draw")
    except KeyboardInterrupt:
        print("\nExiting the game...")
        sys.exit()

class DistributeCards:
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

class GameBattle:
    def __init__(self, player_one_cards, player_two_cards):
        self.player_one_cards = player_one_cards
        self.player_two_cards = player_two_cards

    def draw_compare_cards(self):
        try:
            if len(self.player_one_cards) == 0 or len(self.player_two_cards) == 0:
                announce_winner(self.player_one_cards, self.player_two_cards)
                return

            player_one_pick = [self.player_one_cards.pop(0)]
            player_two_pick = [self.player_two_cards.pop(0)]
            card_value_player1 = int(player_one_pick[0].split(": ")[1])
            card_value_player2 = int(player_two_pick[0].split(": ")[1])
            print("Player One draws", player_one_pick, "valued at:", card_value_player1, "points\n")
            print("Player Two draws", player_two_pick, "valued at:", card_value_player2, "points\n")

            if card_value_player1 < card_value_player2:
                self.player_two_cards.extend(player_one_pick)
            elif card_value_player1 > card_value_player2:
                self.player_one_cards.extend(player_two_pick)
            else:
                print("Start a War")
                self.war_game()

            print("Player One's new deck is:", self.player_one_cards)
            print("Player Two's new deck is:", self.player_two_cards)

            input("Press Enter to continue the game")
            self.draw_compare_cards()

        except KeyboardInterrupt:
            print("\nExiting the game...")
            announce_winner(self.player_one_cards, self.player_two_cards)
            sys.exit()

    def war_game(self):
        if len(self.player_one_cards) < 3 or len(self.player_two_cards) < 3:
            announce_winner(self.player_one_cards, self.player_two_cards)
            return

        player_one_pick = self.player_one_cards[0:3]
        player_two_pick = self.player_two_cards[0:3]
        print("Player One draw:", player_one_pick, "\n\n")
        print("Player Two draw:", player_two_pick, "\n\n")

        card_value_player1 = int(player_one_pick[-1].split(": ")[1])
        card_value_player2 = int(player_two_pick[-1].split(": ")[1])
        if card_value_player1 < card_value_player2:
            self.player_two_cards.extend(player_one_pick)
        elif card_value_player1 > card_value_player2:
            self.player_one_cards.extend(player_two_pick)
        else:
            print("Start a Battle")
            self.war_game()

        input("Press Enter to continue the game")
        self.draw_compare_cards()

print("Let's start a War Game!!! Remember you can always exit the game by pressing Ctrl+C.\n")

# Create an instance of DistributeCards and distribute the cards
distributor = DistributeCards(cards)
player_one_cards, player_two_cards = distributor.distribute()

# Create an instance of GameBattle and compare the cards
battle = GameBattle(player_one_cards, player_two_cards)
battle.draw_compare_cards()
