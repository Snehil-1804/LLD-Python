class Movie:
    def __init__(self,movie_name:str, total_seat:int, ticket_price:int)->None:
        self.movie_name=movie_name
        self.total_seat=total_seat
        self.ticket_price=ticket_price
        self.booked_seats=0

    def booked_tickets(self,number_of_tickets:int)->None:
        if number_of_tickets>self.total_seat-self.booked_seats:
            print (f"Sorry, Not enough seats are avilable.")
        else:
            self.booked_seats+=number_of_tickets
            print(f"Your tickets are booked.")
            print(f"Total Price: {self.ticket_price*number_of_tickets}\n")


    def show_status(self)->None:
        print(f"Movie name= {self.movie_name}")
        print(f"Seat available= {self.total_seat}")
        print(f"Total booked= {self.booked_seats}\n")

movie=Movie("Yo Yo",100,399)
movie.booked_tickets(50)
movie.show_status()

movie.booked_tickets(10)
movie.show_status()