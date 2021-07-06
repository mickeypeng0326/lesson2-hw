Math=input('數學成績?')
English=input('英文成績?')
Math=int(Math)
English=int(English)
if Math>=90 and English>=90:
    print('有獎品!!')
elif Math<60 and English<60:
    print('下次處罰!')
elif Math<60 or English<60:
    print('再加油!')
elif 90>Math>60 or 90>English>60:
    print('很棒!!')

