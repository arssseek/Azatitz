from crud import create_client_and_account, create_talk
from sqlalchemy.sql.expression import func
from modeldb import engine, Account, Talks, Client
from sqlalchemy.orm import sessionmaker
import datetime
from random import choice, randint

F = ("Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas",
    "Jackson", "White", "Harris", "Martin", "Thompson", "Wood", "Lewis", "Scott", "Cooper", "King", "Green", "Walker",
    "Edwards", "Turner", "Mrgan", "Baker", "Hill", "Phillips")
IO = ("M", "J", "A", "H", "B", "C", "K", "R", "W", "N", "P", "S", "G","Y","O","I","D","T")
for i in range(30):
    create_client_and_account(i, f"{choice(F)}.{choice(IO)}.{choice(IO)}")

Session = sessionmaker(bind=engine)

session = Session()

for i in range(1000):
    n = randint(0, 29)
    row = session.query(Account).order_by(func.random()).first()
    create_talk(row.tnumber, datetime.datetime(2022, 3, 2, 10, i % 59, randint(0, 59)),
                datetime.datetime(2022, 3, 2, 10, randint(i % 60, 59), randint(0, 59)))

inp_oper = input()
oper = session.query(Account).filter(Account.operator == inp_oper).all()
for i in range(len(oper)):
    j_oper = session.query(Talks).filter(Talks.tnumber == oper[i].tnumber).all()
    sumtime = 0
    for j in range(len(j_oper)):
        sumtime += j_oper[j].endtime.minute * 60 + j_oper[j].endtime.second - j_oper[j].begintime.minute * 60 + j_oper[
            j].begintime.second
    if (oper[i].limit * 60 < sumtime):
        print(session.query(Client).filter(Client.id == oper[i].c_id).all())
