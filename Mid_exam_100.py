class Hall:
    def __init__(self, row, col, hallNo):
        self.__row = row
        self.__col = col
        self.__seats = {}
        self.__show_list = []
        self.__hallNo = hallNo
        self.__seat = [[0 for i in range(col)] for j in range(row)]

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [
            [0 for _ in range(self.__col)] for _ in range(self.__row)]

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.__seats:
            show_seats = self.__seats[show_id]
            for row, col in seats_to_book:
                if 0 <= row < self.__row and 0 <= col < self.__col:  
                    if show_seats[row][col] == 0:  
                        show_seats[row][col] = 1

                    else:
                        print("Seat Is Already Booked!")

                else:
                    print("Invalid Seat!")
        else:
            print("Show Not Found!")

    def view_show_list(self):
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, show_id):
        if show_id in [show[0] for show in self.__show_list]: 
            show_seats = self.__seats[show_id]
            for row in show_seats:
                print(" ".join(map(str, row)))

        else:
            print("Show Not Found!")

    def get_show_ids(self):  
        return [show[0] for show in self.__show_list]
class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def hall_done(self, hallNo):
        for hall in self.hall_list:
            if hall._Hall__hallNo == hallNo:
                return hall
        return None

hall1 = Hall(row=9, col=9, hallNo=1)
hall2 = Hall(row=8, col=9, hallNo=2)

hall1.entry_show(id='100', movie_name='Don 2', time='time :27/04/2024,2:00 PM')
hall1.entry_show(id='101', movie_name='Lagaan', time='time :27/04/2024,4:00 PM')

hall2.entry_show(id='102', movie_name='3 Idiots', time='time :27/04/2024,2:00 PM')
hall2.entry_show(id='103', movie_name='Rang De Basanti', time='time :27/04/2024,6:00 PM')

cinema = Star_Cinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

while True:
    print("Menu : ")
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKETS")
    print("4. EXITS")

    opt = input("Enter OPTION : ")

    if opt == '1':
        for hall in cinema.hall_list:
            print(f"Hall No : {hall._Hall__hallNo}")
            hall.view_show_list()
        print()

    elif opt == '2':
        show_id = input("Enter Show ID : ")
        hall = None
        for i in cinema.hall_list:
            if show_id in i.get_show_ids():
                hall = i
                break

        if hall:
            hall.view_available_seats(show_id)

        else:
            print("Show Not Found!")

    elif opt == '3':
        show_id = input("Enter Show ID : ")
        cnt = int(input("Enter The Number Of Seats To Booking : "))
        booking_seat = []

        for _ in range(cnt):
            seat_input = input(f"Enter Seat   {_ + 1} (Like (Row-col), R-C) : ")
            seat = tuple(map(int, seat_input.split('-')))
            booking_seat.append(seat)
        hall = None

        for i in cinema.hall_list:
            if show_id in i.get_show_ids():
                hall = i
                break

        if hall:
            hall.book_seats(show_id, booking_seat)
            print("Booking Successfully!")

        else:
            print("Show Not Found!")

    elif opt == '4':
        break

    else:
        print("Please Choose A Valid Option.")