from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def email_all():
	"""
	Print all the students in the database.
	"""
	Subscribtion = session.query(email).all()
	return subscribtion_object

def save_to_database(email):
	subscribtion_object= Subscribtion(email=email)
	session.add(subscribtion_object)
	session.commit()