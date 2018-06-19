def reverse(s):
    s = s[::-1]
    moves = ""
    for letter in s:
        if letter.isupper():
            moves += letter.lower()
        else:
            moves += letter.upper()
    return moves


def discount(r, gamma, normal):
    discount = np.zeros_like(r)
    G = 0.0
    for i in reversed(range(0, len(r))):
        G = G * gamma + r[i]
        discount[i] = G
    # Normalize
    if normal:
        mean = np.mean(discount)
        std = np.std(discount)
        discount = (discount - mean) / (std)
    return discount
