counter = 0
score = 0
answer_1 = "My name ___ Vova"
answer_2 = "I ___ a coder"
answer_3 = "I live ___ Moscow"

user_name = input("Привет!\nПредлогаю проверить твои знания английского!\nРасскажи как тебя зовут!:  ")
print(f'Привет, {user_name}, начинаем тренировку!')

# question_1
question_1 = input(f"Вопрос первый! {answer_1}: ")
if question_1 == 'is':
    counter += 1
    score += 10
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: is')
# question_2
question_2 = input(f"Вопрос первый! {answer_2}: ")
if question_2 == 'am':
    counter += 1
    score += 10
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: am')
# question_3
question_3 = input(f"Вопрос первый! {answer_3}: ")
if question_3 == 'in':
    counter += 1
    score += 10
    print('Ответ верный!\nВы получаете 10 баллов!')

else:
    print('Неправильно.\nПравильный ответ: in')

quantity = (counter / 3) * 100

print(f'Вот и все {user_name}\nвы ответили на {counter} вопросов из 3 верно'
      f'\nВы заработали {score} балов \nэто {quantity:.2f}% правильных ответов.')