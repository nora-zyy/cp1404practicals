class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_info = ", ".join(self.musician)
        return f"{self.name} ({musician_info})"

    def add_musician(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")
