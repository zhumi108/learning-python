from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))		
	phone = Column(String(110))

engine = create_engine('mysql+pymysql://root:password@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id=20, name='twenty', phone='110')
session.add(new_user)
session.commit()
session.close()




