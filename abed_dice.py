import pandas as pd
import numpy as np


def dice (attacking_units, defending_units, net_of_loss):

    while True:
        if net_of_loss < attacking_units and defending_units > 0:
            a_die_1 = np.random.randint(1,6)
            a_die_2 = np.random.randint(1,6)
            a_die_3 = np.random.randint(1,6)
            d_die_1 = np.random.randint(1,6)
            d_die_2 = np.random.randint(1,6)

            if attacking_units >= 4:
                a_num_dice = [a_die_1,  a_die_2, a_die_3]
            elif attacking_units == 3:
                a_num_dice = [a_die_1,  a_die_2]
            elif defending_units == 2:
                a_num_dice = [a_die_1]

            if defending_units >= 2:
                d_num_dice = [d_die_1, d_die_2]
            elif defending_units == 1:
                d_num_dice = [d_die_1]
            attack_roll = sorted(a_num_dice, reverse= True)
            defend_roll = sorted(d_num_dice, reverse = True)

            if attack_roll[0] <= defend_roll[0]:
                attacking_units -= 1
                print (f'Attacker highest roll: {attack_roll[0]}\nDefender highest roll: {defend_roll[0]}\nAttacker loses 1 soldier {attacking_units}\n')
            else:
                defending_units -= 1
                print (f'Attacker highest roll: {attack_roll[0]}\nDefender highest roll: {defend_roll[0]}\nDefender loses 1 soldier {defending_units}\n')
            if attacking_units > 1 and defending_units > 1:
                if attack_roll[1] <= defend_roll[1]:
                    attacking_units -= 1
                    print (f'Attacker second highest roll: {attack_roll[1]}\nDefender second highest roll: {defend_roll[1]}\nAttacker loses 1 soldier {attacking_units}\n')
                else:
                    defending_units -= 1
                    print (f'Attacker second highest roll: {attack_roll[1]}\nDefender second highest roll: {defend_roll[1]}\nDefender loses 1 soldier {defending_units}\n') 
                continue
            else:
                continue
        else:
            if net_of_loss == attacking_units:
                print(f'{25 * "-"}\nDefender Wins!')
                print (f'Attacker remaining units: {attacking_units}')
                print (f'Defender remaining units: {defending_units}')
            elif defending_units == 0:
                print(f'{25 * "-"}\nAttacker Wins!')
                print (f'Attacker remaining units: {attacking_units}')
                print (f'Defender remaining units: {defending_units}')
            break

def main():
    intro = 'Welcome to Risk Dice Roll Program!'
    print(intro)
    print(f'{len(intro) * "-"}\n')
    while True:
        try:
            attacking_units_amt = int(input('Enter the number of attackers: '))
            break
        except:
            print('Please input a valid integer!')
            continue
    while True:
        try:
            attacking_loss_limit = int(input(
                'How many units is the attacker willing to lose?: '))
            net_of_loss = attacking_units_amt - attacking_loss_limit
            if net_of_loss < 1:
                print('You cant lose more than you have! Try again.')
                continue
            else:
                break
            break
        except:
            print('Please input a valid integer!')
            continue
    while True:
            try:
                defending_units_amt = int(input('Enter the number of defenders: '))
                break
            except:
                print('Please input a valid integer!')
                continue

    dice(attacking_units_amt, defending_units_amt, net_of_loss)

if __name__ == '__main__':
    main()