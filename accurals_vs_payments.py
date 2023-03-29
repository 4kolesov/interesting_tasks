import os
import sqlite3

database = 'database.db'


def check_db(filename):
    """Проверим, есть ли файл с БД."""
    return os.path.exists(filename)

if check_db(database):
    connection = sqlite3.connect(database)

cursor = connection.cursor()

connection.execute(
    '''CREATE TABLE accrual
             (id INTEGER PRIMARY KEY,
              date DATETIME,
              month TEXT)'''
)

connection.execute(
    '''CREATE TABLE payment
             (id INTEGER PRIMARY KEY,
              date DATETIME,
              month TEXT)'''
)

connection.commit()

connection.execute('INSERT INTO accrual (date, month) VALUES (?, ?)', ('2022-01-01', 'Январь'))
connection.execute('INSERT INTO accrual (date, month) VALUES (?, ?)', ('2022-02-03', 'Февраль'))
connection.execute('INSERT INTO accrual (date, month) VALUES (?, ?)', ('2022-04-05', 'Апрель'))
connection.execute('INSERT INTO payment (date, month) VALUES (?, ?)', ('2022-01-01', 'Январь'))
connection.execute('INSERT INTO payment (date, month) VALUES (?, ?)', ('2022-02-03', 'Февраль'))
connection.execute('INSERT INTO payment (date, month) VALUES (?, ?)', ('2022-05-06', 'Май'))

connection.commit()
connection.close()


def find_matching_accrual_payments():
    """Поиск и вывод соответствия платежей и долгов."""
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    payments = cursor.execute('SELECT * FROM payment').fetchall()
    accruals = cursor.execute('SELECT * FROM accrual').fetchall()

    matching_accruals = []
    unpaid_payments = []

    for payment in payments:
        paid_accrual = False
        for accrual in accruals:
            if payment[2] == accrual[2] and not paid_accrual:
                matching_accruals.append((payment, accrual))
                accruals.remove(accrual)
                paid_accrual = True
            if accrual[1] < payment[1] and not paid_accrual:
                matching_accruals.append((payment, accrual))
                accruals.remove(accrual)
                paid_accrual = True

        if not paid_accrual:
            unpaid_payments.append(payment)

    print('Оплаченные платежи / долги:')
    for pay, acc in matching_accruals:
        print(f'Платеж: {pay[1]} {pay[2]}, долг: {acc[1]} {acc[2]}')
    print('Платежи без долга:')
    for pay in unpaid_payments:
        print(*pay)

    connection.close()


if __name__ == '__main__':
    find_matching_accrual_payments()
