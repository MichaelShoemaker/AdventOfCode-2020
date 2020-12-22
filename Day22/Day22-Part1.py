import typing

def prep_data(file) -> tuple:
    data = open(file,'r').readlines()
    #Make two lists for the players
    player1 = []
    player2 = []
    #Create flag to indicate which players numbers are being read
    turn = True
    for i in data:
        if i[:8] == 'Player 1' and turn == True:
            pass
        elif i[:8] == 'Player 2':
            turn = False
        elif turn == True and len(i.strip())>0:
            player1.append(int(i.strip()))
        elif turn == False and len(i.strip())>0:
            player2.append(int(i.strip()))           
    return player1, player2


def play(p: tuple) -> list:
    p1 = p[0]
    p2 = p[1]
    while len(p1)>0 and len(p2)>0:
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
            p1.pop(0)
            p2.pop(0)
        elif p2[0]>p1[0]:
            p2.append(p2[0])
            p2.append(p1[0])
            p1.pop(0)
            p2.pop(0)
    if len(p1) > len(p2):
        return p1
    else:
        return p2

def total_cards(cards: list) -> int:
    total = 0
    mult = len(cards)
    for i in cards:
        total += i * mult
        mult -= 1
    return total

if __name__=='__main__':
    assert total_cards(play(prep_data('test.txt'))) == 306
    print(total_cards(play(prep_data('input.txt'))))
    
