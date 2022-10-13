# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
#
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате.
# При этом, если человек регистрирует больше трёх человек на конференцию,
# то дополнительно получает 10% скидку на полную стоимость заказа.


price_all = 0
while True:
    try:
        ticket_number = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Для какого возраста билет №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-x человек')
else:
    print(f'Сумма к оплате {price_all} руб.')