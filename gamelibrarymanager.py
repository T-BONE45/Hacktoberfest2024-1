class Game:
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform

class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, title, genre, platform):
        new_game = Game(title, genre, platform)
        self.games.append(new_game)
        print(f"Added {title} to the library.")

    def remove_game(self, title):
        for game in self.games:
            if game.title.lower() == title.lower():
                self.games.remove(game)
                print(f"Removed {title} from the library.")
                return
        print(f"{title} not found in the library.")

    def list_games(self):
        if not self.games:
            print("No games in the library.")
        else:
            print("Games in the library:")
            for i, game in enumerate(self.games, start=1):
                print(f"{i}. {game.title} ({game.genre}, {game.platform})")

def main():
    library = GameLibrary()

    while True:
        print("\nGame Library Management")
        print("1. Add game")
        print("2. Remove game")
        print("3. List games")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter game title: ")
            genre = input("Enter game genre: ")
            platform = input("Enter game platform: ")
            library.add_game(title, genre, platform)
        elif choice == "2":
            title = input("Enter game title to remove: ")
            library.remove_game(title)
        elif choice == "3":
            library.list_games()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
