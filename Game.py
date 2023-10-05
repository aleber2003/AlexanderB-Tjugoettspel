import random

class Game:
    def __init__(self):
        # Initialize the game with player and computer hands, and a shuffled deck
        self.player_hand = []
        self.computer_hand = []
        self.deck = Deck()
        self.deck.shuffle()

    def deal_initial_cards(self):
        # Deal two cards to both the player and the computer at the beginning
        self.player_hand.append(self.deck.deal_card())
        self.computer_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.computer_hand.append(self.deck.deal_card())

    def calculate_hand_value(self, hand):
        # Calculate the value of a hand, considering Aces as either 1 or 14 based on user choice
        value = 0
        num_aces = 0

        for card in hand:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                num_aces += 1
                value += Card.ACE_VALUE

        # Adjust for Aces if the value exceeds 21
        while value > 21 and num_aces:
            value -= 13  # Subtracting 13 will convert 14 to 1
            num_aces -= 1
        return value

    def player_turn(self):
        # Allow the player to draw cards until they choose to stop or bust
        while True:
            print(f"\nComputer's card: {str(self.computer_hand[0])}")
            print(f"Your hand: {[str(card) for card in self.player_hand]}")
            print(f"Your hand value: {self.calculate_hand_value(self.player_hand)}")

            choice = input("Do you want to draw another card? (yes/no): ").lower()

            if choice == 'yes':
                drawn_card = self.deck.deal_card()
                self.player_hand.append(drawn_card)

                if drawn_card.rank == 'Ace':
                    ace_choice = input("Do you want to count Ace as 1 or 14? (1/14): ")
                    Card.ACE_VALUE = int(ace_choice)

                print(f"You drew: {str(drawn_card)}")
            elif choice == 'no':
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

            if self.calculate_hand_value(self.player_hand) > 21:
                print("You busted! Computer wins.")
                return False

        return True

    def computer_turn(self):
        # Let the computer draw cards until its hand value is at least 17
        while self.calculate_hand_value(self.computer_hand) < 17:
            self.computer_hand.append(self.deck.deal_card())
            print(f"Computer drew: {str(self.computer_hand[-1])}")

        return True

    def determine_winner(self):
        # Compare hand values and determine the winner
        player_value = self.calculate_hand_value(self.player_hand)
        computer_value = self.calculate_hand_value(self.computer_hand)

        print(f"\nYour final hand: {[str(card) for card in self.player_hand]}")
        print(f"Your final hand value: {player_value}")
        print(f"\nComputer's final hand: {[str(card) for card in self.computer_hand]}")
        print(f"Computer's final hand value: {computer_value}")

        if player_value > 21:
            print("You busted! Computer wins.")
        elif computer_value > 21 or player_value > computer_value:
            print("Congratulations! You win.")
        elif player_value < computer_value:
            print("Computer wins.")
        else:
            print("It's a tie!")

    def play_game(self):
        while True:
            print("Welcome to 21!")
            self.deal_initial_cards()

            player_turn_result = self.player_turn()

            if player_turn_result:
                computer_turn_result = self.computer_turn()

                if computer_turn_result:
                    self.determine_winner()

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == 'no':
                print("Thanks for playing! Goodbye.")
                break
            else:
                self.computer_hand.clear()
                self.player_hand.clear()


# Define a class to represent a playing card
class Card:
    ACE_VALUE = 14  # Default value for Ace

    def __init__(self, suit, rank):
        # Initialize card with suit and rank
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # Return a string representation of the card
        return f"{self.rank} of {self.suit}"

# Define a class to represent a deck of cards
class Deck:
    def __init__(self):
        # Create a deck with all possible combinations of suits and ranks
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        # Deal a card from the deck
        return self.cards.pop()

# Define a class to represent the 21 game

# Main program
if __name__ == "__main__":
    # Create a game instance and start playing
    game = Game()
    game.play_game()
