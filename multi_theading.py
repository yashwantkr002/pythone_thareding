from  threading import current_thread, Thread
class Train:
    def __init__(self,ablible_seat):
        self.ablible_seat=ablible_seat


    def Booking(self,need_seat):
        print('Ablible seat',self.ablible_seat)
        if need_seat<=self.ablible_seat:
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.ablible_seat-=need_seat
        else:
            print(f'Sorry {self.ablible_seat} seat are left')

p=Train(2)
p1=Thread(target=p.Booking,args=(3,),name="yshwant")
p2= Thread(target=p.Booking,args=(1,),name="tinku")
p1.start()
p2.start()