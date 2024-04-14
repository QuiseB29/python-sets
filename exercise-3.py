def add_stage_set(crowd, artist_name, stage_set):
    if artist_name not in stage_set:
        stage_set[artist_name] = set()
    stage_set[artist_name].add(crowd)

def display_set(stage_set):
    print("\nSet List:")
    for artist, crowds in stage_set.items():
        print(f"{artist}: {', '.join(crowds)}")

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
stage_set = {}

while True:
    print("\n1. Add stages to set")
    print("2. Display sets")
    print("3. Exit")
    choice = input("Enter a choice: ")

    if choice == "1":
        crowd = input("Enter the crowd: ")
        artist_name = input("Enter the artist name: ")
        add_stage_set(crowd, artist_name, stage_set)
    elif choice == "2":
        display_set(stage_set)
    elif choice == "3":
        print("Exiting")
        break
    else:
        print("Invalid input. Please try again.")
