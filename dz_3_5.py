from random import choice


def get_jokes(n, repeat):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if repeat:
        i = 0
        while i < n:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
        return jokes
    else:
        i = 0
        while i < n:
            word_1 = choice(nouns)
            word_2 = choice(adverbs)
            word_3 = choice(adjectives)
            jokes.append(f'{word_1} {word_2} {word_3}')
            nouns.remove(word_1)
            adverbs.remove(word_2)
            adjectives.remove(word_3)
            i += 1
        return jokes

print(get_jokes(n=5, repeat=True))

print(get_jokes(n=5, repeat=False))