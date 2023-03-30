import Connect_Project3
from random import randint



def First_Menu():
    Authorization_Or_Registration = input("Добро пожаловать в ресторан 'Лазанья и всё'\n1.Зарегистрироваться\n2.Авторизироваться\n")
    if Authorization_Or_Registration == "1":
        Registration()
    elif Authorization_Or_Registration == "2":
        Authorization()
    else:
        input("Ошибка, такой команды нет. Нажмите enter, чтобы продолжить")
        First_Menu()
    
def Registration():
    print("Добро пожаловать в окно регистрации")
    Admin_Or_Client = input("Выберите роль 1.Администратор 2.Клиент\n")
    Login = input("Введите логин: ")
    Password = input ("Введите пароль: ")
    try:
        if Admin_Or_Client == "1":
            Connect_Project3.DataBaseClass.BaseMethod("insert into [dbo].[User] values ('" + Login + "','" + Password + "'," + str(9000000) +"," + Admin_Or_Client + ")").commit()
        elif Admin_Or_Client == "2":
            Connect_Project3.DataBaseClass.BaseMethod("insert into [dbo].[User] values ('" + Login + "','" + Password + "'," + str((((sum ([i[0] for i in Connect_Project3.DataBaseClass.BaseMethod("select [Price] from [dbo].[Ingredients]")]))**2) * randint(20, 40))/100) +"," + Admin_Or_Client + ")").commit()
        else:
            input("Ошибка, такой команды нет. Нажмите enter, чтобы продолжить")
            Registration()
        print("Вы успешно зарегестрировались")
        First_Menu()
    except:
        input("Такой пользователь уже существует. Нажмите enter, чтобы продолжить")
        Registration()

    
def Authorization():
    print("Добро пожаловать в окно авторизации")
    Login = input("Введите логин: ")
    Password = input ("Введите пароль: ")
    WhatRole = [i[0] for i in Connect_Project3.DataBaseClass.BaseMethod("select [Role_Name] from [dbo].[User] inner join [dbo].[Role] on [Role_ID] = [ID_Role] where [Login] = '" + Login +"' and [Password] = '" + Password + "'")]
    global ID_User
    ID_User = [i[0] for i in Connect_Project3.DataBaseClass.BaseMethod("select [ID_User] from [dbo].[User] inner join [dbo].[Role] on [Role_ID] = [ID_Role] where [Login] = '" + Login +"' and [Password] = '" + Password + "'")]
    if WhatRole.__len__() > 0:
        if WhatRole[0] == "Администратор":
            AdminMenu()
        elif WhatRole[0] == "Клиент":
            global Balance
            Balance = [i[0] for i in Connect_Project3.DataBaseClass.BaseMethod("select [Balance] from [dbo].[User]")]
            if Balance[0] <= 2000000:
                Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[User] set [Balance] = {(((Balance[0]) **2) * randint(20, 40))/100} where [ID_User] = {ID_User[0]}").commit()
            ClientMenu()
    else:
        input("Такого аккаунта не существует. Нажмите enter, чтобы продолжить")
        First_Menu()

def AdminMenu():
    What_In_Menu = input("1.Составить акцию\n2.Пополнение ингредиентов\n3.Карты лояльности клиентов\n4.История покупок клиентов\n")
    if What_In_Menu == "1":
        StockCompilation()
    elif What_In_Menu == "2":
        IngredientsReplinishment()
    elif What_In_Menu == "3":
        LoyalityCartClientForAdmin()
    elif What_In_Menu == "4":
        StoryPurshases()
    else:
        input("Выбранной функции не существует. Нажмите enter для продолжения")
        AdminMenu()


def ClientMenu():
    What_In_Menu = input("1.Составить блюдо\n2.Карты лояльности\n")
    if What_In_Menu == "1":
        MakeADish()
    elif What_In_Menu == "2":
        LoyalityCard()
    else:
        input("Выбранной функции не существует. Нажмите enter для продолжения")
        ClientMenu()

def StockCompilation():
    print("Список ингредиентов:")

    IngredientsSQL = "select [ID_Ingredients], [Name_Ingredients], [Price], [Quantity] from [dbo].[Ingredients]"
    ID_Ingredients = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Name_Ingredients = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Price = [row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Quantity = [row[3] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]

    for row in range(ID_Ingredients.__len__()):
        print(f"(ID: {ID_Ingredients[row]}) (Название: {Name_Ingredients[row]}) (Цена: {Price[row]}) (Количество: {Quantity[row]})")

    Text_Stock = input ("Введите текст акции: ")
    Quantity_Stock = input("Введите количество ингредиентов в акции: ")
    ID_Ingredient = input("Введите ID ингредиента: ")
    try:
        Connect_Project3.DataBaseClass.BaseMethod(f"insert into [dbo].[Stock] values ('{Text_Stock}', {Quantity_Stock}, {ID_Ingredient})").commit()
        input("Успешное добавление акции. Нажмите Enter для продолжения")
        AdminMenu()
    except:
        input("Данного ID не существует. Нажмите enter для продолжения")
        StockCompilation()

    AdminMenu()


def IngredientsReplinishment():
    IngredientsSQL = "select [ID_Ingredients], [Name_Ingredients], [Price], [Quantity] from [dbo].[Ingredients]"
    ID_Ingredients = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Name_Ingredients = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Price = [row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Quantity = [row[3] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]

    for row in range(ID_Ingredients.__len__()):
        print(f"(ID: {ID_Ingredients[row]}) (Название: {Name_Ingredients[row]}) (Цена: {Price[row]}) (Количество: {Quantity[row]})")
    ID_Ingredient = input("Введите ID ингредиента: ")
    Count = input("Введите количество ингредиента: ")
    try:
        if Balance <= 0:
            Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[Ingredients] set [Quantity] = [Quantity] + {Count} where [ID_Ingredients] = {ID_Ingredient}").commit()
            Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[User] set [Balance] = [Balance]-(select [Price] from [dbo].[Ingredients] where [ID_Ingredients] = {ID_Ingredient})*{Count} where [ID_User] = {ID_User[0]}").commit()
            input("Ингредиенты успешно куплены. Нажмите enter для продолжения")
            AdminMenu()
        else:
            input("Ошибка, нехватает средств")
            AdminMenu()
    except:
        input("Данного ID не существует. Нажмите enter для продолжения")
        IngredientsReplinishment()

def LoyalityCartClientForAdmin():
    LoyalytiSQL = f"select [Login], [Telephone_Number], [Name_Loyality_Card] from [dbo].[Loyality_Card_User] inner join [dbo].[User] on [User_ID] = [ID_User] inner join [dbo].[Loyality_Card] on [ID_Loyality_Card] = [Loyality_Card_ID] where [Telephone_Number] is not null"
    Login = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(LoyalytiSQL)]
    Telephone_Number = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(LoyalytiSQL)]
    Name_Loyality_Card = [row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(LoyalytiSQL)]
    for row in range(Login.__len__()):
        print(f"(Логин: {Login[row]}) (Телефонный номер: {Telephone_Number[row]}) (Уровень карты лояльности: {Name_Loyality_Card[row]})")
    input("Нажмите любую кнопку, чтобы продолжить")
    AdminMenu()


def StoryPurshases():
    UserSQL = "select [ID_User], [Login] from [dbo].[User] where [Role_ID] = 2"
    ID_Users= [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(UserSQL)]
    Login = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(UserSQL)]

    for row in range(ID_Users.__len__()):
        print(f"\n(ID: {ID_Users[row]}) (Логин: {Login[row]}\n")

    ID_Userss = input("Введите ID пользователя: ")
    print("История покупок пользователя")

    CheckSQL = f"select [Check_Text] from [dbo].[Check] where [User_ID] = {ID_Userss}"
    Check_Text = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(CheckSQL)]

    if (Check_Text.__len__() > 0):
        for row in range(Check_Text.__len__()):
            print(f"Чек {row+1}: {Check_Text[row]})")
    else:
        print("История покупок пуста или пользователя не существует")
    

    input("Нажмите enter для продолжения")
    AdminMenu()


def MakeADish():
    global Ingredients_List
    Ingredients_List = []
    IngredientsSQL = "select top (5) [ID_Ingredients], [Name_Ingredients], [Price], [Quantity] from [dbo].[Ingredients]"
    ID_Ingredients = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Name_Ingredients = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Price = [row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]

    print("Обязательные ингредиенты")
    for row in range(ID_Ingredients.__len__()):
        Ingredients_List.append([ID_Ingredients[row], Name_Ingredients[row], Price[row]])
        print(f"(ID: {ID_Ingredients[row]}) (Название: {Name_Ingredients[row]}) (Цена: {Price[row]})")
    Dish()

def Dish():
    IngredientsSQL = "select [ID_Ingredients], [Name_Ingredients], [Price], [Quantity] from [dbo].[Ingredients]"
    ID_Ingredientss = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Name_Ingredientss = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]
    Prices = [row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(IngredientsSQL)]

    print("Добавляемые ингредиенты")

    for row in range(ID_Ingredientss.__len__()):
        print(f"(ID: {ID_Ingredientss[row]}) (Название: {Name_Ingredientss[row]}) (Цена: {Prices[row]})")
    ID_Ingredient = int(input("Введите ID ингредиента, которое хотите добавить, если ничего не хотите добавлять или хотите закончить введите -1: "))
    try:
        if ID_Ingredient == -1:
            Name_Ingredientsss = [row[1] for row in Ingredients_List]
            Pricesss = [row[2] for row in Ingredients_List]
            res = []
            for i in Ingredients_List:
                if i not in res:
                    res.append(i)
            ID_Ingredientss_res = [row[0] for row in res]
            Name_Ingredientsss_res = [row[1] for row in res]
            Pricesss_res = [row[2] for row in res]
            Chena = 0
            Name_Stock = []
            Price = []
            Stock_Quantity = []
            AllCheck = str()
            print("Ваш чек")
            for row in range(Name_Ingredientsss_res.__len__()):
                Chena += Pricesss[row] * Name_Ingredientsss.count(Name_Ingredientsss_res[row])
                AllCheck += f"Названия ингредиента: {Name_Ingredientsss_res[row]} {Name_Ingredientsss.count(Name_Ingredientsss_res[row])} шт. Цена: {Pricesss_res[row] * Name_Ingredientsss.count(Name_Ingredientsss_res[row])} руб\n"
                for row in range(ID_Ingredientss_res.__len__()):
                    StocksSQL = f"select [ID_Stock], [Name_Stock], [Stock_Quantity], [Ingredients_ID], [Price] from [dbo].[Stock] inner join [dbo].[Ingredients] on [Ingredients_ID] = [ID_Ingredients] where [Stock_Quantity] <= {Name_Ingredientsss.count(Name_Ingredientsss_res[row])} and [Ingredients_ID] = {ID_Ingredientss_res[row]}"
                    if Name_Stock.__len__() == 0:
                        Name_Stock.extend([row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                        Price.extend([row[4] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                        Stock_Quantity.extend([row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                    else:
                        Name = []
                        Name.extend([row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                        if (Name.__len__() > 0):
                            if Name[0] not in Name_Stock:
                                Name_Stock.extend([row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                                Price.extend([row[4] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                                Stock_Quantity.extend([row[2] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)])
                                Name.clear()
            if len(Name_Stock) > 0:
                for row in range(Name_Stock.__len__()):
                    AllCheck += f"Акция: {Name_Stock[row]}\n"
                    Chena -= Price[row] * Stock_Quantity[row] - Price[row]
                    AllCheck += f"Скидка: {Price[row] * Stock_Quantity[row] - Price[row]}\n"
            Rand1 = randint(1,6)
            Rand2 = randint(1,6)
            if (Rand1 == 5):
                AllCheck += "Клубника\n"
                if (Rand2 == 5):
                    AllCheck += "Скидка 30%\n"
                    Chena = ((Chena **2) * 30)/100

            LoyalitySQL = f"select [Loyality_Card_ID] from [Prac3].[dbo].[Loyality_Card_User] where [User_ID] = {ID_User[0]}"
            Loyality_Card_ID = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(LoyalitySQL)]

            if Loyality_Card_ID[0] == 1:
                Chena = Chena - (5/100*Chena)
                AllCheck += "Карта лояльности: Скидка 5%\n"
            elif Loyality_Card_ID[0] == 2:
                Chena = Chena - (10/100*Chena)
                AllCheck += "Карта лояльности: Скидка 10%\n"
            elif Loyality_Card_ID[0] == 3:
                Chena = Chena - (20/100*Chena)
                AllCheck += "Карта лояльности: Скидка 20%\n"

            AllCheck += f"Итого: {Chena}"
            print(AllCheck)
            input("Нажмите Enter для подтверждения покупки")
            Connect_Project3.DataBaseClass.BaseMethod(f"insert into [dbo].[Check] values ({ID_User[0]}, '{AllCheck}', {Chena})").commit()
            Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[User] set [Balance] = [Balance]-{Chena} where [ID_User] = {ID_User[0]}").commit()
            input("Успешная покупка, нажмите Enter для продолжения")
            ClientMenu()
        ID_Ingredient -= 1
        Ingredients_List.append([ID_Ingredientss[ID_Ingredient], Name_Ingredientss[ID_Ingredient], Prices[ID_Ingredient]])
        Dish()
    except:
        input("Ошибка, неверный ID или недостаточно средств")
        MakeADish()



def LoyalityCard():
    Number = input("Введите номер: ")
    try:
        Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[Loyality_Card_User] set [Telephone_Number] = '{Number}' where [User_ID] = {ID_User[0]}").commit()
        input("Успешно, нажмите Enter для продолжения")
        ClientMenu()
    except:
        input("Ошибка, нажмите Enter для продолжения")
        LoyalityCard()

def LoyalityCardAdd():
    StocksSQL = f"select [ID_Check], [User_ID] from [dbo].[Check]"
    User_ID = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(StocksSQL)]
    Sum = int()

    for row in range(User_ID.__len__()):
        BalanceSQL = f"select [ID_Check], [Check_Balance] from [dbo].[Check] where [User_ID] = {User_ID[row]}"
        Check_Balance = [row[1] for row in Connect_Project3.DataBaseClass.BaseMethod(BalanceSQL)]
        for row2 in range(Check_Balance.__len__()):
            Sum += Check_Balance[row2]

        LoyalitySQL = f"select [User_ID] from [Prac3].[dbo].[Loyality_Card_User] where [User_ID] = {User_ID[row]}"
        User_ID_Loyality = [row[0] for row in Connect_Project3.DataBaseClass.BaseMethod(LoyalitySQL)]

        if User_ID_Loyality.__len__() == 0:
            if Sum >= 5000:
                Connect_Project3.DataBaseClass.BaseMethod(f"insert into [dbo].[Loyality_Card_User] ([Loyality_Card_ID], [User_ID]) values (1, {User_ID[row]})").commit()
            elif Sum >= 15000:
                Connect_Project3.DataBaseClass.BaseMethod(f"insert into [dbo].[Loyality_Card_User] ([Loyality_Card_ID], [User_ID]) values (2, {User_ID[row]})").commit()
            elif Sum >= 25000:
                Connect_Project3.DataBaseClass.BaseMethod(f"insert into [dbo].[Loyality_Card_User] ([Loyality_Card_ID], [User_ID]) values (2, {User_ID[row]})").commit()
        else:
            if Sum >= 5000:
                Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[Loyality_Card_User] set [Loyality_Card_ID] = 1 where [User_ID] = {User_ID[row]}").commit()
            elif Sum >= 15000:
                Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[Loyality_Card_User] set [Loyality_Card_ID] = 2 where [User_ID] = {User_ID[row]}").commit()
            elif Sum >= 25000:
                Connect_Project3.DataBaseClass.BaseMethod(f"update [dbo].[Loyality_Card_User] set [Loyality_Card_ID] = 3 where [User_ID] = {User_ID[row]}").commit()

        Sum = 0

LoyalityCardAdd()
First_Menu()