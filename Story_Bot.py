import random


def horror_story():
    place = random.choice(["a blackened mansion on a hill", "a fog-filled forest outside town", "an abandoned hospital with a flickering elevator"])
    protagonist = random.choice(["a nervous teenage girl", "a quiet librarian", "a lost traveler with a broken compass"])
    ally = random.choice(["her younger brother", "the janitor who never left his desk", "a skeptical priest who smelled of smoke"])
    clue = random.choice(["a trail of wet footprints leading upstairs", "a hidden room behind the wall clock", "a scratched message that said, 'do not let it out'"])
    twist = random.choice(["the house had been hiding a family no one remembered", "the whispering voice was not a ghost, but the building itself", "the person they trusted most had been dead for ten years"])
    ending = random.choice(["they escaped before dawn, but the house still watched from the window every night", "they burned the mansion to ash and finally heard the silence they had been chasing", "they learned the haunting was only the first warning, and some doors should never be opened again"])

    return (
        f"On the edge of town, {protagonist} arrived at {place} with {ally} beside them. "
        f"The doors creaked open before they touched them, and a cold wind slid through the halls like a whisper. "
        f"At first, the silence seemed normal, but soon they noticed {clue}. "
        f"Every step deeper into the building made the air heavier, and the walls began to answer in the voices of people who had been missing for years. "
        f"When they finally reached the cellar, they discovered the truth: {twist}. "
        f"The thing inside the walls was not trying to kill them at random; it wanted a witness. "
        f"In the final confrontation, {protagonist} had to choose between running forever or exposing the nightmare to the world. "
        f"By dawn, they had escaped, but the memory of the house stayed with them, and {ending}."
    )


def comedy_story():
    place = random.choice(["a crowded amusement park", "a noisy supermarket where the carts could fly", "a tiny village talent contest in the middle of summer"])
    protagonist = random.choice(["a clumsy magician", "a pizza delivery robot", "a nervous clown with a very expensive mustache"])
    rival = random.choice(["the mayor's overconfident son", "a singer who thought every room was their stage", "a suspiciously talented goat in a tuxedo"])
    disaster = random.choice(["accidentally turned the mayor into a chicken", "lost the map to the free dessert booth", "started a dance battle with the town band"])
    setback = random.choice(["the crowd booed at first, then roared with laughter", "the mayor's helicopter landed in the fountain", "the prize cake exploded in a shower of confetti"])
    ending = random.choice(["they won the festival by laughing at themselves", "they got free pizza for life, which somehow felt like a blessing and a curse", "they realized the best joke was the one they told first and the whole town laughed with them"])

    return (
        f"It started as an ordinary day in {place}, which was already a terrible place to be calm. "
        f"{protagonist} had one simple job: stay out of trouble and make it to the finish line. "
        f"But then {rival} challenged them to a public showdown, and before anyone could stop it, {protagonist} {disaster}. "
        f"The crowd gasped, the mayor shouted, and the whole town seemed to freeze for one terrible second. "
        f"Then came the worst part: {setback}. "
        f"Instead of panicking, {protagonist} leaned into the chaos, made a joke at their own expense, and somehow the audience turned from skeptics into fans. "
        f"By the end, the entire square was laughing, the competition was forgotten, and {ending}. "
        f"The problem was solved, the dignity was mostly restored, and the town would never again look at a surprise birthday parade the same way."
    )


def drama_story():
    place = random.choice(["a rainy train station at midnight", "a small seaside town in the middle of a storm", "a school hallway on the last day before graduation"])
    protagonist = random.choice(["a young musician with a ruined hand", "a tired nurse keeping a family secret", "a student who had spent years pretending they were fine"])
    problem = random.choice(["had to say goodbye to someone they loved before they ever said the truth", "carried a secret that could ruin their family if it came out", "made a choice that could destroy the future they had worked for"])
    conflict = random.choice(["the train was delayed, the sky was falling apart, and every minute made the goodbye harder", "the town's gossip moved faster than truth, and every rumor made the secret heavier", "their friends were moving on, and no one noticed how close they were to breaking"])
    realization = random.choice(["they had been afraid of the truth because it was the only thing that made them honest", "love did not disappear just because distance tried to erase it", "forgiveness was not a reward; it was a way to keep living"])
    ending = random.choice(["they chose peace over pride and left the station with a lighter heart", "they finally told the truth and found that love had been waiting for them all along", "they realized every ending was part of a new beginning, even if it had to be painful first"])

    return (
        f"At {place}, {protagonist} {problem}. "
        f"There was no dramatic speech, no perfect moment, no clear solution, only {conflict}. "
        f"The whole world seemed to narrow to one choice: keep hiding, or say what was actually true. "
        f"As they stood there with shaking hands and a heart full of old mistakes, the truth finally surfaced with unbearable clarity. "
        f"{realization}. "
        f"By the end, the storm had passed and the future was no longer something they were running from. "
        f"It was something they could finally face. {ending}."
    )


while True:
    print("\nHello, I'm your story Bot. Call me Dave.")
    print("What kind of story do you want me to make?")
    print("1 - Horror")
    print("2 - Comedy")
    print("3 - Drama")
    print("Q - Quit")

    dave = input("Please choose a genre: ").strip().lower()

    if dave == "q":
        print("Goodbye! Come back for another story soon.")
        break

    if dave == "1":
        print("You chose Horror. Here is your story:")
        print(horror_story())

    elif dave == "2":
        print("You chose Comedy. Here is your story:")
        print(comedy_story())

    elif dave == "3":
        print("You chose Drama. Here is your story:")
        print(drama_story())

    else:
        print("Invalid choice. Please try again.")
