from sqlalchemy.ext.declarative import declarative_base
from db.eng import POSTGRES_URL
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine(POSTGRES_URL, echo=False)


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    fio = Column(String)
    email = Column(String)

    account = relationship("Account", back_populates="client")

    def __repr__(self):
        return f"<{self.id},{self.fio},{self.email}>"


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tnumber = Column(String, unique=True)
    limit = Column(Integer)
    operator = Column(String)
    c_id = Column(Integer, ForeignKey(Client.id))

    client = relationship("Client", back_populates="account")
    talks = relationship("Talks", back_populates="account")

    def __repr__(self):
        return f"<{self.id},{self.tnumber},{self.limit},{self.operator},{self.c_id}>"


class Talks(Base):
    __tablename__ = 'talks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    begintime = Column(DateTime)
    endtime = Column(DateTime)
    tnumber = Column(String, ForeignKey(Account.tnumber))

    account = relationship("Account", back_populates="talks")

    def __repr__(self):
        return f"<{self.id},{self.tnumber},{self.begintime},{self.endtime}>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
