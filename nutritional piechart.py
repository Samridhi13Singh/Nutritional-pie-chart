import matplotlib.pyplot as plt
food ={
    'Apple':{'protein':15,'fats':12,'carbohydrates':3.43},
    'Banana':{'protein':43,'fats':13,'carbohydrates':20},
    'Milk':{'protein':54,'fats':22,"carbohydrates":23},
    'Chocolate':{'protein':0,'fats':65,'carbohydrates':34}
}

# print(food["Apple"])

def nutrition_plot(food_name):
    if food_name not in food:
        print('INVALID SYNTAX TRY AGAIN')
    else:

        data =food[food_name]
        Protein=data['protein']
        Fats =data['fats']
        Carbohydrates=data['carbohydrates']

        print(Protein,Fats,Carbohydrates)
        value=[Protein,Fats,Carbohydrates]
        label=data.keys()
        plt.figure(figsize=(6,7))
        plt.pie(value,labels=label,autopct='%1.0f%%',startangle=140,wedgeprops={'edgecolor':'black'})
        plt.title(f'The Nutritional value are :{food_name}')
        plt.legend(label)
        plt.show()



fl=input("enter food item:-")
nutrition_plot(fl)


