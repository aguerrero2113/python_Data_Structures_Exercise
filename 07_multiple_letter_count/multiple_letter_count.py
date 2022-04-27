def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_freq = {}

    for n in phrase:

        keys = letter_freq.keys()

        if n in keys:

            letter_freq[n] += 1

        else:

            letter_freq[n] = 1

    return letter_freq
print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))