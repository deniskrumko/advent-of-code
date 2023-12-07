from collections import (
    Counter,
    defaultdict,
)
from functools import partial
from pathlib import Path
from typing import Generator

INPUT_FILE = Path(__file__).parent / 'input.txt'
DEFAULT_DECK = 'AKQJT98765432'
DECK_WITH_JOKER = 'AKQT98765432J'
JOKER = 'J'


def n_of_a_kind(n: int, cards: str) -> bool:
    """Check if cards has N of similar card."""
    return n in Counter(cards).values()


def full_house(cards: str) -> bool:
    """Check if cards has 2 similar and 3 similar cards."""
    return set(Counter(cards).values()) == {2, 3}


def n_pairs(n: int, cards: str) -> bool:
    """Check if cards has exactly N pairs."""
    return Counter(Counter(cards).values()).get(2, 0) == n


def high_card(cards: str) -> bool:
    """High card rule applies to every cards."""
    return True


HANDS = [
    partial(n_of_a_kind, n=5),  # 0 - five of a kind
    partial(n_of_a_kind, n=4),  # 1 - four of a kind
    full_house,                 # 2 - full house
    partial(n_of_a_kind, n=3),  # 3 - three of a kind
    partial(n_pairs, n=2),      # 4 - two pairs
    partial(n_pairs, n=1),      # 5 - one pair
    high_card,                  # 6 - high card
]


def get_hand(cards: str) -> int:
    """Determine hand of cards."""
    for i, h in enumerate(HANDS):
        if h(cards=cards):
            return i


def get_card_power(card: str, joker: bool = False) -> int:
    """Get integer power of card in deck."""
    deck = DECK_WITH_JOKER if joker else DEFAULT_DECK
    return len(deck) - deck.index(card)


def cards_to_powers(cards: str, joker: bool = False) -> tuple[int, ...]:
    """Covert card values to their integer powers."""
    return tuple(get_card_power(c, joker=joker) for c in cards)


def joker_pretend(cards: str) -> str:
    """Convert original cards with Jokers to strongest hand without Jokers."""
    if JOKER not in cards:
        return cards

    if set(cards) == {JOKER}:  # Single corner case
        return 'AAAAA'

    not_jokers = [c for c in DECK_WITH_JOKER[:-1] if c in cards]
    best_cards, best_hand = cards, get_hand(cards)

    for card in not_jokers:
        new_cards = cards.replace(JOKER, card, 1)
        if JOKER in new_cards:
            new_cards = joker_pretend(new_cards)

        if (new_hand := get_hand(new_cards)) < best_hand:
            best_cards = new_cards
            best_hand = new_hand

    return best_cards


def get_cards_ranks(cards_with_bets: list[tuple], joker: bool) -> Generator[str, int, int]:
    """Get iterator over cards, bets and their ranks."""
    # Find groups of cards with same hand
    hands_map = defaultdict(list)
    for original_cards, bet in cards_with_bets:
        pretended_cards = joker_pretend(original_cards) if joker else original_cards
        hand_type = get_hand(pretended_cards)
        hands_map[hand_type].append((original_cards, bet))

    # Sort each hand group using card powers
    rank = 1
    for i in range(len(HANDS) - 1, -1, -1):
        if hands := hands_map[i]:
            for cards, bet in sorted(hands, key=lambda x: cards_to_powers(x[0], joker)):
                yield cards, int(bet), rank
                rank += 1


def parse_data(data: str) -> list[list[int]]:
    """Parse puzzle data."""
    return [line.split() for line in data.splitlines()]


def function_1(data: str, joker=False) -> bool:
    """Get result for puzzle (part 1)."""
    return sum(bet * rank for _, bet, rank in get_cards_ranks(parse_data(data), joker=joker))


def function_2(data: str) -> bool:
    """Get result for puzzle (part 2)."""
    return function_1(data, joker=True)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {function_1(input_data)}')
        print(f'Your result (2): {function_2(input_data)}')
