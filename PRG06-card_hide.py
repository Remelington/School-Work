def card_hide (card_num):
    return 12*"X" + card_num[12:]

print (card_hide("1234123456785678"))