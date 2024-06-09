import random

class Entertainment:
    def __init__(self, name, category, actors, duration, rating):
        self.name = name
        self.category = category
        self.actors = actors
        self.duration = duration
        self.rating = rating

    def display_info(self):
        return f"{self.name} ({self.category}): {self.actors} actors, {self.duration} minutes, rating: {self.rating}"

    def __str__(self):
        return self.display_info()
    def __repr__(self):
        return f"Entertainment('{self.name}', '{self.category}', {self.actors}, {self.duration}, {self.rating})"

    def __del__(self):
        print(f"The entertainment '{self.name}' has been removed.")

def create_entertainment_objects(num_objects=20):
    names = ["Movie", "Concert", "National-Geographic", "Game Show", "Stand-up Comedy", "Musical", "Dance Performance", "Magic Show", "Opera", "Reality Show", "Circus", "Talk Show", "Ducumentry", "Talent Show", "Sit-com", "Game Show", "Short Film", "Dark Comedy", "Sports Events", "Playing Chess"]
    categories = ["Comedy", "Drama", "Action", "Horror", "Documentary", "Musical", "Thriller", "Animation", "Dark Humor", "Sci-Fi", "Biography", "Documentry", "Mystery", "Thriller", "Family", "Sport", "War", "Crime","Historical"]
    actors = [random.randint(1, 10) for _ in range(20)]
    durations = [random.randint(60, 180) for _ in range(20)]
    ratings = [round(random.uniform(1, 10), 1) for _ in range(20)]

    entertainment_objects = []
    for name, category, actor, duration, rating in zip(names, categories, actors, durations, ratings):
        entertainment_objects.append(Entertainment(name=name, category=category, actors=actor, duration=duration, rating=rating))

    return entertainment_objects

def sort_by_actors(entertainment_objects):
    sorted_objects = sorted(entertainment_objects, key=lambda e: e.actors)
    return sorted_objects

# if __name__ == "__main__":
#     # Create 20 entertainment objects
#     entertainment_data = create_entertainment_objects()

#     # Sort by number of actors
#     sorted_entertainment = sort_by_actors(entertainment_data)

#     # Print sorted entertainment data
#     for entertainment in sorted_entertainment:
#         print(entertainment.display_info())
my_entertainment = Entertainment(name="My Movie", category="Drama", actors=5, duration=120, rating=8.5)
def __str__(self):
        return self.display_info()
print(my_entertainment)
