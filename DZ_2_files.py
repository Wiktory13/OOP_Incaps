with open('recepts.txt', encoding='utf-8') as file:
    data = file.read().split("\n\n")
    cook_book = {}
    for i in data:
        name = i.split("\n")[0]
        ing = i.split('\n')[2:]
        # print(name)
        # print(ing)
        print(cook_book)
        for j in ing:
            ing_1 = j.split('|')
            ing_dict = {'ingredient_name':ing_1[0], 'quantity':ing_1[1], 'meansure':ing_1[2]}
            # print(ing_dict)
            if name in cook_book:
                cook_book[name].append(ing_dict)
            else:
                cook_book[name] = [ing_dict]

    print(cook_book)
    
    file.close()