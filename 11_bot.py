from dataclasses import dataclass
import time
import random
from typing import List


#    ♤♡♧♢
@dataclass
class Card:
    suit: str
    rank: str
def get_card(self):
    weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
def info(self, input):

    return f'{self.suit} + {self.rank}'

class Desk_Card:
    def __init__(self) -> None:
        _suits = ['♤', '♡', '♧', '♢']
        _ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(s,r) for s in _suits for r in _ranks]
        random.shuffle(self.cards)
    def get_cards(self):
        return self.cards.pop()
    
@dataclass
class Container:
    volume: int
    current_volume: int
    drop: int = 1
    def container_out(self):
        self.current_volume -= self.drop
        return self.drop
    def container_in(self, volume_in):
        self.current_volume += volume_in
        return self.drop
    def get_info(self):
        return f'{self.current_volume}'

def main():
    a = Desk_Card()
    print(a.get_cards())
if __name__ == '__main__':
    main()