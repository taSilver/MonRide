from monride import db
from models.user import User
from models.destination import Destination
from models.available import Available
from models.events import CalendarEvent

db.drop_all()

db.create_all()
clayton = Destination(name='Clayton', address='Wellington Rd, Clayton', postcode=3800)
peninsula = Destination(name='Peninsula', address='Moorooduc Hwy, Frankston', postcode=3199)
caulfield = Destination(name='Caulfield', address='900 Dandenong Rd, Caulfield East', postcode=3145)

admin = User(username='admin', email='admin@example.com', driver=False, rating=5, first_name='admin', last_name='admin', course='arts/it', music='So Fresh 2007', interests='get away from the aux', avatar='admin')
guest = User(username='guest', email='guest@example.com', driver=False, rating=1, first_name='guest', last_name='guest', course='law', music='hip/hop jazz', interests='reading', avatar='guest')
user1 = User(username='user1', email='user1@example.com', driver=False, rating=2.6, first_name='user', last_name='1', course='sports science', music='chants', interests='getting bread', avatar='user1')
user2 = User(username='user2', email='user2@example.com', driver=True, rating=4.6, first_name='user', last_name='2', course='philosophy', music='black metal', interests='obeying the law', avatar='user2')
Doge = User(username='doge', email='Doge@example.com', driver=False, rating=4.6, first_name='Doge', last_name='Smith', course='Bachelor of Computer Science', music='So Fresh 2009', interests='saving lives', avatar='doge')

db.session.add(admin)
db.session.add(guest)
db.session.add(user1)
db.session.add(user2)
db.session.add(Doge)
db.session.commit()

