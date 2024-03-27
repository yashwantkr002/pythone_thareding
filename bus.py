from threading import *
class Bus:
    def __init__(self ,available_seat=None):
        self.available_seat=available_seat
        self.Lock=Semaphore(1)

    def Booking(self,R_seat=None):
        self.Lock.acquire()
        print(f'available seat {self.available_seat}')
        if self.available_seat>= R_seat  and R_seat<=4:
            name=current_thread().name
            print(f'{R_seat} is book by {name}')
            self.available_seat-=R_seat
        elif self.available_seat!=0:
            name=current_thread().name
            print(f'Sorry only {self.available_seat} are Available and {name} not get any seat')
        else:
            name=current_thread().name
            print(f'Sorry all seat are booked and {name} not get any seat')
        self.Lock.release()

p=Bus(10)
p1=Thread(target=p.Booking,args=(3,),name='shareya')
p2=Thread(target=p.Booking,args=(3,),name='sony')
p3=Thread(target=p.Booking,args=(2,),name='suman')
p4=Thread(target=p.Booking,args=(4,),name='sarita')
p5=Thread(target=p.Booking,args=(3,),name='laxmi')
p6=Thread(target=p.Booking,args=(1,),name='mansi')
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()