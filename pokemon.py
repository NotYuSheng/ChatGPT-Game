import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QMessageBox # Written by user


class Pokemon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Game")

        # Create the labels for the player's and the enemy's Pokemons
        self.player_pokemon = QLabel("Player's Pokemon:")
        self.player_pokemon_name = QLabel("Naruto")
        self.player_pokemon_health = QLabel("Health: 100")
        self.player_pokemon_animation = QLabel()
        self.player_pokemon_animation.setMovie(QMovie("naruto.gif"))

        self.enemy_pokemon = QLabel("Enemy's Pokemon:")
        self.enemy_pokemon_name = QLabel("Goku")
        self.enemy_pokemon_health = QLabel("Health: 100")
        self.enemy_pokemon_animation = QLabel()
        self.enemy_pokemon_animation.setMovie(QMovie("goku.gif"))

        # Create the attack and heal buttons
        self.attack_button = QPushButton("Attack")
        self.heal_button = QPushButton("Heal")

        # Create the grid layout
        grid = QGridLayout()

        # Add the labels and the buttons to the grid
        grid.addWidget(self.player_pokemon, 0, 0)
        grid.addWidget(self.player_pokemon_name, 0, 1)
        grid.addWidget(self.player_pokemon_health, 0, 2)
        grid.addWidget(self.player_pokemon_animation, 0, 3)
        grid.addWidget(self.enemy_pokemon, 1, 0)
        grid.addWidget(self.enemy_pokemon_name, 1, 1)
        grid.addWidget(self.enemy_pokemon_health, 1, 2)
        grid.addWidget(self.attack_button, 2, 0)
        grid.addWidget(self.heal_button, 2, 1)

        # Start the animation for the player's and the enemy's Pokemons
        self.player_pokemon_animation.movie().start()
        self.enemy_pokemon_animation.movie().start()

        # Set the grid layout as the layout of the widget
        self.setLayout(grid)

        # Connect the attack and heal buttons to the attack and heal functions
        self.attack_button.clicked.connect(self.attack)
        self.heal_button.clicked.connect(self.heal)

        # Initialize the health of the player's and the enemy's Pokemons
        self.player_health = 100
        self.enemy_health = 100

    def start_ai(self):
        # Use a timer to call the AI function every 1 second
        self.ai_timer = QTimer()
        self.ai_timer.timeout.connect(self.ai)
        self.ai_timer.start(1000)

    def ai(self):
        # If the enemy's health is less than or equal to 30, try to heal
        if self.enemy_health <= 30:
            self.heal()
        else:
            # Otherwise, attack the player's Pokemon
            self.enemy_attack()

    def enemy_attack(self):
        # Decrease the player's health by 10
        self.player_health -= 10

        # Set the new health of the player's Pokemon on the label
        self.player_pokemon_health.setText("Health: " + str(self.player_health))

        # If the player's Pokemon's health is less than or equal to 0, show a message box and stop the AI
        if self.player_health <= 0:
            QMessageBox.information(self, "Pokemon Game", "You lost the battle!")
            self.ai_timer.stop()

    def attack(self):
        # Decrease the enemy's health by 10
        self.enemy_health -= 10

        # Set the new health of the enemy's Pokemon on the label
        self.enemy_pokemon_health.setText("Health: " + str(self.enemy_health))

        # If the enemy's Pokemon's health is less than or equal to 0, show a message box
        if self.enemy_health <= 0:
            QMessageBox.information(self, "Pokemon Game", "You won the battle!")

    def heal(self):
        # Increase the player's health by 10
        self.player_health += 10

        # Set the new health of the player's Pokemon on the label
        self.player_pokemon_health.setText("Health: " + str(self.player_health))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Pokemon()
    game.start_ai() # Written by user
    game.show() # Corrected by user
    app.exec() # Written by user
