# def test():
#     sf = "6C 7C 8C 9C TC".split()  # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
#     fh = "TD TC TH 7C 7D".split()  # Full House
#     # repeat sf 100 times
#     print([[sf]+99*[fk]])


# test()


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r, s in cards]
    # for every char in ranks ,turn from 'T' to 10, 'J' to 11, 'Q' to 12, 'K' to 13, 'A' to 14

    for i in range(len(ranks)):
        if ranks[i] == 'T':
            ranks[i] = 10
        elif ranks[i] == 'J':
            ranks[i] = 11
        elif ranks[i] == 'Q':
            ranks[i] = 12
        elif ranks[i] == 'K':
            ranks[i] = 13
        elif ranks[i] == 'A':
            ranks[i] = 14
        else:
            ranks[i] = int(ranks[i])
    ranks.sort(reverse=True)
    return ranks

# print(card_ranks(['AC', '3D', '4S', 'KH'])) #should output [14, 13, 4, 3]


# def poker(hands):
#     "Return the best hand: poker([hand,...]) => hand"
#     return max(hands, key=hand_rank)

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    print(hand)
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

# def test():
#     "Test cases for the functions in poker program"
#     sf = "6C 7C 8C 9C TC".split() # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
#     fh = "TD TC TH 7C 7D".split() # Full House
#     assert poker([sf, fk, fh]) == sf
#     assert poker([fk, fh]) == fk
#     assert poker([fh, fh]) == fh
#     assert poker([sf]) == sf
#     assert poker([sf] + 99*[fh]) == sf
#     assert hand_rank(sf) == (8, 10)
#     assert hand_rank(fk) == (7, 9, 7)
#     assert hand_rank(fh) == (6, 10, 7)
#     return 'tests pass'


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.

    s = set(ranks)

    # T J Q K A

    if len(s) == 5:
        # if s has 14
        # A 2 3 4 5
        if 14 in s and min(s) == 2:
            s.remove(14)
            s.add(1)
            #  这里比较大小的时候可能出问题， 需要修改ranks数值 14->1
            #  test(&["2H 3C 4D 5D 6H", "4S AH 3S 2D 5H"], &["2H 3C 4D 5D 6H"])
            ranks[0] = 1
        return max(s)-min(s) == 4
    else:
        return False

    # for i in range(len(ranks)-1):
    #     if ranks[i] - ranks[i+1] != 1:
    #         return False

    # return True


def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    suit = [s for r, s in hand]
    for i in range(len(suit)-1):
        if suit[i] != suit[i+1]:
            return False

    return True

# def test():
#     "Test cases for the functions in poker program."
#     sf = "6C 7C 8C 9C TC".split()
#     fk = "9D 9H 9S 9C 7D".split()
#     fh = "TD TC TH 7C 7D".split()
#     assert straight([9, 8, 7, 6, 5]) == True
#     assert straight([9, 8, 8, 6, 5]) == False
#     assert flush(sf) == True
#     assert flush(fk) == False
#     return 'tests pass'

# print(test())


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    # n=2 ranks=[7,7,5,1,3] return 7
    # count every number's frequency
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


# def test():
#     "Test cases for the functions in poker program."
#     sf = "6C 7C 8C 9C TC".split() # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
#     fh = "TD TC TH 7C 7D".split() # Full House
#     tp = "5S 5D 9H 9C 6S".split() # Two pairs
#     fkranks = card_ranks(fk)
#     tpranks = card_ranks(tp)
#     assert kind(4, fkranks) == 9
#     assert kind(3, fkranks) == None
#     assert kind(2, fkranks) == None
#     assert kind(1, fkranks) == 7
#     return 'tests pass'

# def card_ranks(hand):
#     "Return a list of the ranks, sorted with higher first."
#     ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
#     ranks.sort(reverse = True)
#     return ranks

# print(test())

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    # [7,7,5,5,3] should return (7,5)

    cnt = {}
    for r in ranks:
        if r in cnt:
            cnt[r] += 1
        else:
            cnt[r] = 1

    tows = []  # 出现2次的牌
    for (k, v) in cnt.items():
        if v == 2:
            tows.append(k)

    if len(tows) != 2:
        return None
    else:
        return (max(tows), min(tows))


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


# def test():
#     "Test cases for the functions in poker program."
#     sf = "6C 7C 8C 9C TC".split()  # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
#     fh = "TD TC TH 7C 7D".split()  # Full House
#     tp = "TD 9H TH 7C 3S".split()  # Two Pair
#     fkranks = card_ranks(fk)
#     tpranks = card_ranks(tp)
#     assert kind(4, fkranks) == 9
#     assert kind(3, fkranks) == None
#     assert kind(2, fkranks) == None
#     assert kind(1, fkranks) == 7
#     return 'tests pass'


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks


# def test():
#     "Test cases for the functions in poker program."
#     sf = "6C 7C 8C 9C TC".split()  # Straight Flush
#     fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
#     fh = "TD TC TH 7C 7D".split()  # Full House
#     al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
#     assert straight(card_ranks(al)) == True
#     return 'tests pass'

def test():
    "Test cases for the functions in poker program."
    sf1 = "6C 7C 8C 9C TC".split()  # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    return 'tests pass'


print(test())

# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

# import random # this will be a useful library for shuffling

# # This builds a deck of 52 cards. If you are unfamiliar
# # with this notation, check out Andy's supplemental video
# # on list comprehensions (you can find the link in the
# # Instructor Comments box below).

# mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

# def deal(numhands, n=5, deck=mydeck):
#     # Your code here.
#     random.shuffle(deck)
#     ans =[]
#     for i in range(numhands):
#         ans.append([])
#         for j in range(n*i,n*(i+1)):
#             ans[i].append(deck[j])
#     return ans

# print(deal(3,2))
