import random

print(''' ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█ █ ▄ █ █       █   █   █       █       █  █▄█  █       █
█ ██ ██ █    ▄▄▄█   █   █       █   ▄   █       █    ▄▄▄█
█       █   █▄▄▄█   █   █     ▄▄█  █ █  █       █   █▄▄▄ 
█       █    ▄▄▄█   █▄▄▄█    █  █  █▄█  █       █    ▄▄▄█
█   ▄   █   █▄▄▄█       █    █▄▄█       █ ██▄██ █   █▄▄▄ 
█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█
''')

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list_of_rps = [rock, paper, scissors]

# print(f"{rock}\n {paper} \n {scissors}\n")

choose_user = int(
    input("what is your choose 0=Rock , 1=paper , 2= scissors\n"))
print(list_of_rps[choose_user])
print("you choose")

comp_choose = random.randint(0, 2)
print(list_of_rps[comp_choose])
print("computer choose choose")

if choose_user >= 3 or choose_user < 0:
    print("worte coorect number ")
elif choose_user == 2 and comp_choose == 0:
    print("you loose")

elif choose_user == comp_choose:
    print(" it's Draw")

elif choose_user > comp_choose:
    print("you win  ")

elif choose_user < comp_choose:
    print("you lose  ")

elif choose_user == 0 and comp_choose == 2:
    print("you win")
