def rock_paper_scissor(num1, num2, bit1, bit2, player_one, player_two):
    if not (0 <= bit1 < len(num1) and 0 <= bit2 < len(num2)):
        print("Error: Secret bit position out of range")
        return

    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3

    if player_one[p1] == player_two[p2]:
        print("Draw")
    elif player_one[p1] == "Rock" and player_two[p2] == "Scissor":
        print("player one wins")
    elif player_one[p1] == "Rock" and player_two[p2] == "Paper":
        print("player two wins")
    elif player_one[p1] == "Paper" and player_two[p2] == "Scissor":
        print("player two wins")
    elif player_one[p1] == "Paper" and player_two[p2] == "Rock":
        print("player one wins")
    elif player_one[p1] == "Scissor" and player_two[p2] == "Rock":
        print("player two wins")
    elif player_one[p1] == "Scissor" and player_two[p2] == "Paper":
        print("player one wins")

player_one = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
player_two = {0: 'Paper', 1: 'Rock', 2: 'Scissor'}

while True:
    num1 = input("PLAYER ONE, ENTER YOUR CHOICE: ")
    num2 = input("PLAYER TWO, ENTER YOUR CHOICE: ")
    bit1 = int(input("PLAYER ONE, ENTER THE SECRET BIT POSITION: "))
    bit2 = int(input("PLAYER TWO, ENTER THE SECRET BIT POSITION: "))
    rock_paper_scissor(num1, num2, bit1, bit2, player_one, player_two)
    ch = input("Do you want to continue? (y/n): ")
    if ch == 'n':
        break