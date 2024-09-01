def calculate_love_score(name1, name2):
    list = [['t', 'r', 'u', 'e'], ['l', 'o', 'v', 'e']]
    count1 = 0
    count2 = 0
    for c in name1:
        if c.lower() in list[0]:
            count1 += 1
        if c.lower() in list[1]:
            count2 += 1
    for x in name2:
        if x.lower() in list[0]:
            count1 += 1
        if x.lower() in list[1]:
            count2 += 1
        digit_string = str(name1)+ str(name2)
        combine = int(digit_string)
        print(combine)
calculate_love_score("Kanye West", "Kim Kardashian")


