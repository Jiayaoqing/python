def show_score(score):
    if score >= 90 and score <= 100:
     print("您的成绩是A!")
    elif score >= 80 and score < 90:
     print("您的成绩是B!")
    elif score >= 70 and score < 80:
     print("您的成绩是C!")
    elif score >= 60 and score < 70:
     print("您的成绩是D!")
    else:
     print("您需要努力了!")
stu_score = int(input("请输入成绩:\n"))
show_score(stu_score)
