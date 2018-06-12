'''
	局部变量，就是在函数内部定义的变量。
	不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响。
	局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储。

	函数内部变量定义并且赋值，该变量为局部变量;
	在函数外部定义的变量，为全局变量；
	函数内部使用变量名，局部变量名和全局变量名同名，优先使用局部变量;
	在函数内部如果想要使用全局变量，使用global关键字声明;
	全局变量在函数内部未声明的情况下，只能使用，不可修改值.

'''
import random

# 玩家姓名
playerName = "John"
# 玩家金钱
playerMoney = 1000

# 显示玩家信息
def show_player():
    print("玩家姓名:%s 玩家余额:%d" % (playerName, playerMoney))

# 押注金额和赔率
def bet_on():

    money = 0
    rate = 1
    while True:
        money = int(input("请输入押注金额:"))
        # 如果押注金额大于账户余额，则重新输入
        if money > playerMoney:
            print("账户余额:%s，不足以本次押注，请重新输入!" % playerMoney)
        else:
            break

    # 计算合理赔率
    right_rate = playerMoney // money
    while True:
        print("请输入赔率(1-%d):" % right_rate, end="")
        rate = int(input())
        if int(rate) < 1 or int(rate) > right_rate:
            print("输入的赔率不正确，请重新输入!")
        else:
            break

    return rate, money


# 赌博
def gamble(rate, money):
    # 随机产生竞猜数字
    guessing_robot = random.randint(1, 6)
    # 输入竞猜数字
    guessing_number = int(input("先生,请输入竞猜数字(1-6):"))
    # 显示竞猜数字
    print("系统产生竞猜数字为:%d,您的竞猜数字为:%d" % (guessing_robot, guessing_number))
    # 比较竞猜数字
    global playerMoney
    if guessing_number == guessing_robot:
        print("恭喜您，本轮猜中!")
        playerMoney = playerMoney + money * (rate - 1)
    else:
        print("抱歉，本轮您未猜中!")
        playerMoney = playerMoney - money * rate


# 开始游戏
def start_game():

    # 当前局数
    game = 1
    while playerMoney > 0:
        print("第%d轮竞猜开始:" % game)
        # 显示玩家信息
        show_player()
        # 押注
        rate, money = bet_on()
        # 开始赌博
        gamble(rate, money)
        game += 1
        print("---------------------")
    show_player()
    print("游戏结束!")
start_game()
