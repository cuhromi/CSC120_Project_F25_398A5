import random


class Player:
    def __init__(self, name: str = "Tester"):
        # initialize attributes that used to be in the player dict
        self.name = name
        self.health = 100
        self.coin = 0
        self.x = 0
        self.y = 0

    def move(self, direction, map_size):
        # move updates x/y based on direction, bounded by map_size
        if direction == 'w' and self.x > 0:
            self.x -= 1
        elif direction == 's' and self.x < map_size - 1:
            self.x += 1
        elif direction == 'a' and self.y > 0:
            self.y -= 1
        elif direction == 'd' and self.y < map_size - 1:
            self.y += 1
        else:
            print("You cannot move that way!")


class GameMap:
    def __init__(self, size: int = 9):
        # default map size
        self.size = size

    def draw(self, player):
        print("=========================")
        for i in range(self.size):
            for j in range(self.size):
                if i == player.x and j == player.y:
                    print("C", end=" ")
                elif i == self.size - 1 and j == self.size - 1:
                    print("M", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("=========================")
        print(f"Health: {player.health}")
        print("-------------------------")
        print(f"Coin: {player.coin}")
        print("=========================")
        print("Your move (w/a/s/d/q):", end="")


class Game:
    def __init__(self):
        # some instance attributes
        self.game_name = "Escaping"
        self.name = "Tester"
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.player = Player()
        self.map = GameMap()
        # expose map_size for compatibility with tests
        self.map_size = self.map.size

    def check_event(self):
        event = random.choice(self.events)

        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10

    def play(self):
        # main game loop
        self.map.draw(self.player)
        direction = input("Your next move (w/a/s/d/q)")

        while direction != 'q':
            self.player.move(direction, self.map.size)

            if self.player.x == self.map.size - 1 and self.player.y == self.map.size - 1:
                print("Congratulations! You reach the gate for next level.")
                break

            self.check_event()

            self.map.draw(self.player)
            direction = input("Your next move (w/a/s/d/q)")


if __name__ == "__main__":
    Game().play()
