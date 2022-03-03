from modeldb import engine, Account, Talks, Client
from sqlalchemy.orm import sessionmaker
from random import randint
import datetime
Session = sessionmaker(bind=engine)


def create_client_and_account(c_id:int ,fio :str):
    with Session() as session:
        try:
            client = Client(id=c_id, fio=fio, email=(fio+"@gmail.com"))
            session.add(client)
            session.flush()
            account = Account(tnumber=f'+375({randint(29,44)}){randint(1000000,9999999)}', limit=randint(150,500), operator=f'{randint(1,10)}', c_id=c_id)
            session.add(account)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def create_talk(tnum: str, btim: datetime, etim: datetime):
    with Session() as session:
        try:
            talk = Talks(tnumber=tnum, begintime=btim, endtime=etim)
            session.add(talk)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


