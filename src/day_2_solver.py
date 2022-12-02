from typing import List

decoder = {
    'A': {'name': 'rock', 'defeated_by': 'paper', 'score': 1},
    'B': {'name': 'paper', 'defeated_by': 'scissors', 'score': 2},
    'C': {'name': 'scissors', 'defeated_by': 'rock', 'score': 3},
    'X': {'name': 'rock', 'defeated_by': 'paper', 'score': 1},
    'Y': {'name': 'paper', 'defeated_by': 'scissors', 'score': 2},
    'Z': {'name': 'scissors', 'defeated_by': 'rock', 'score': 3},
}

decoder_for_part_2 = {
    'A': {'name': 'rock', 'defeated_by': 'B', 'score': 1},
    'B': {'name': 'paper', 'defeated_by': 'C', 'score': 2},
    'C': {'name': 'scissors', 'defeated_by': 'A', 'score': 3},
}


def part_1(game_strategy: List[str]) -> int:
    winning_bonus = 6
    draw_bonus = 3
    score = 0
    for round in game_strategy:
        choices = round.split(' ')
        opponent_choice = decoder.get(choices[0])
        my_choice = decoder.get(choices[1])

        if opponent_choice.get('name') == my_choice.get('name'):
            round_score = my_choice.get('score') + draw_bonus
            score = score + round_score

        if my_choice.get('name') == opponent_choice.get('defeated_by'):
            round_score = my_choice.get('score') + winning_bonus
            score = score + round_score

        if my_choice.get('defeated_by') == opponent_choice.get('name'):
            round_score = my_choice.get('score')
            score = score + round_score

    return score


def part_2(game_strategy: List[str]) -> int:
    winning_bonus = 6
    draw_bonus = 3
    score = 0
    win = 'Z'
    draw = 'Y'
    lose = 'X'
    for round in game_strategy:
        choices = round.split(' ')
        opponent_choice = decoder_for_part_2.get(choices[0])
        my_action = choices[1]

        if my_action == draw:
            round_score = opponent_choice.get('score') + draw_bonus
            score = score + round_score

        if my_action == win:
            my_choice = decoder_for_part_2.get(opponent_choice.get('defeated_by'))
            round_score = my_choice.get('score') + winning_bonus
            score = score + round_score

        if my_action == lose:
            for key in decoder_for_part_2:
                if choices[0] == decoder_for_part_2.get(key).get('defeated_by'):
                    round_score = decoder_for_part_2.get(key).get('score')
                    score = score + round_score

    return score
