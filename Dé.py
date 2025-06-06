import random


def roll_dice(faces, number_of_dice):
    
    results = [random.randint(1, faces) for _ in range(number_of_dice)]
    
    for i, result in enumerate(results, start=1):
        print(f"Dé {i} : {result}")
    print(f"\nRésultat total : {sum(results)}")

def main():
    print("Bienvenue dans le simulateur de lancer de dés !")
    
    faces = int(input("Nombre de faces par dé : "))
    number_of_dice = int(input("Nombre de dés à lancer : "))
    
    while True:
        roll_dice(faces, number_of_dice)
        
        if input("\nRelancer ? (o/n) : ").lower() != "o":
            if input("\nModifier les paramètres ? (o/n) : ").lower() == "o":
                faces = int(input("Nouveau nombre de faces par dé : "))
                number_of_dice = int(input("Nouveau nombre de dés à lancer : "))
            else:
                break    

    print("Merci d'avoir utilisé le simulateur !")

if __name__ == "__main__":
    main()