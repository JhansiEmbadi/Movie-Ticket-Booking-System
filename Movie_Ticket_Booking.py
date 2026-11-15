cart_movies = []
cart_shows = []
cart_seats = []
cart_price = []
cart_bookings = []

movies = ['sita', 'Anand', 'Sakhi', 'kushi', 'Fidha']

shows = ['8AM-11AM', '12PM-3PM', '5PM-8PM', '9PM-12AM']

seats = ['a1', 'a2', 'a3', 'a4', 'a5',
         'a6', 'a7', 'a8', 'a9', 'a10']

price = [500, 500, 450, 450, 300,
         300, 250, 250, 150, 150]

ratings = ['*****', '****', '***', '****', '*****']

seat_prices = dict(zip(seats, price))

total_price = 0
name = ""
mobileno = ""

selected_movie = ""
selected_show = ""

pending_seats = []
pending_total = 0


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number!")


def display_movies():
    print(f'{"S.NO":<6}{"Movies":<15}{"Ratings":<12}')
    print("-" * 35)

    for i in range(len(movies)):
        print(f'{i+1:<6}{movies[i]:<15}{ratings[i]:<12}')


def display_shows():
    print(f'{"S.NO":<6}{"Available Shows":<20}')
    print("-" * 26)

    for i in range(len(shows)):
        print(f'{i+1:<6}{shows[i]:<20}')


def display_seats(movie, show):
    booked_seats = []

    for booking in cart_bookings:
        if booking["movie"] == movie and booking["show"] == show:
            booked_seats.append(booking["seat"])

    for seat in pending_seats:
        if seat not in booked_seats and movie == selected_movie and show == selected_show:
            booked_seats.append(seat)

    print("\nAvailable Seats:")

    for i in range(len(seats)):
        if seats[i] in booked_seats:
            status = "Booked"
        else:
            status = "Available"

        print(f'{seats[i]:<10}{status:<12}{seat_prices[seats[i]]}')


while True:

    print("\n========== MOVIE TICKET BOOKING SYSTEM ==========")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    chc = get_number("Enter your choice (1/2/3): ")

    # ================= ADMIN =================

    if chc == 1:

        while True:

            print("\n========== ADMIN MENU ==========")
            print("1. Add Movies")
            print("2. Add Shows")
            print("3. Manage Seats")
            print("4. Delete Shows/Movies")
            print("5. View Booking")
            print("6. Exit")

            choose = get_number("Enter your choice: ")

            if choose == 1:

                item = input("Enter a movie: ").strip()

                if item.lower() in [m.lower() for m in movies]:
                    print("Movie already exists!")
                elif item:
                    movies.append(item)
                    ratings.append(input("Enter movie rating: "))
                    print("Movie added successfully!")
                else:
                    print("Movie name cannot be empty!")

                display_movies()

            elif choose == 2:

                item = input("Enter showtime: ").strip()

                if item in shows:
                    print("Showtime already exists!")
                elif item:
                    shows.append(item)
                    print("Show added successfully!")
                else:
                    print("Showtime cannot be empty!")

                display_shows()

            elif choose == 3:

                if not movies or not shows:
                    print("No movies or shows available!")
                    continue

                display_movies()

                movie = input("Enter movie name: ").strip()

                if movie not in movies:
                    print("Movie not available!")
                    continue

                display_shows()

                show = input("Enter showtime: ").strip()

                if show not in shows:
                    print("Showtime not available!")
                    continue

                display_seats(movie, show)

            elif choose == 4:

                print("1. Delete Movies")
                print("2. Delete Shows")

                option = get_number("Select your choice: ")

                if option == 1:

                    item = input("Enter movie name: ").strip()

                    if item in movies:
                        index = movies.index(item)
                        movies.pop(index)
                        ratings.pop(index)
                        print("Movie deleted successfully!")
                    else:
                        print("Movie not available!")

                    display_movies()

                elif option == 2:

                    item = input("Enter showtime: ").strip()

                    if item in shows:
                        shows.remove(item)
                        print("Show deleted successfully!")
                    else:
                        print("Showtime not available!")

                    display_shows()

                else:
                    print("Invalid choice!")

            elif choose == 5:

                print("\n========== ALL BOOKINGS ==========")

                if not cart_bookings:
                    print("No bookings available!")
                else:
                    print(f'{"Name":<12}{"Movie":<12}{"Show":<15}{"Seat":<10}{"Price":<10}')
                    print("-" * 60)

                    for booking in cart_bookings:
                        print(
                            f'{booking["name"]:<12}'
                            f'{booking["movie"]:<12}'
                            f'{booking["show"]:<15}'
                            f'{booking["seat"]:<10}'
                            f'{booking["price"]:<10}'
                        )

            elif choose == 6:
                break

            else:
                print("Invalid choice!")

    # ================= USER =================

    elif chc == 2:

        selected_movie = ""
        selected_show = ""
        pending_seats = []
        pending_total = 0
        name = ""
        mobileno = ""

        while True:

            print("\n========== USER MENU ==========")
            print("1. View Movies")
            print("2. View Showtimes")
            print("3. Select Seats")
            print("4. Book Ticket")
            print("5. View Booking")
            print("6. Exit")

            choose = get_number("Enter your choice: ")

            if choose == 1:

                print("\nAvailable Movies")

                if not movies:
                    print("No movies available!")
                    continue

                display_movies()

                selected = input("Which movie do you want to watch? ").strip()

                movie_match = next(
                    (m for m in movies if m.lower() == selected.lower()),
                    None
                )

                if movie_match:
                    if selected_movie != movie_match:
                        pending_seats = []
                        pending_total = 0
                    selected_movie = movie_match
                    print("Selected Movie:", selected_movie)
                else:
                    print("Movie is not available!")

            elif choose == 2:

                print("\nAvailable Showtimes")

                if not shows:
                    print("No shows available!")
                    continue

                display_shows()

                selected1 = input("Select your showtime: ").strip()

                if selected1 in shows:
                    if selected_show != selected1:
                        pending_seats = []
                        pending_total = 0
                    selected_show = selected1
                    print("Selected Show:", selected_show)
                else:
                    print("Showtime not available!")

            elif choose == 3:

                if not selected_movie or not selected_show:
                    print("First select a movie and showtime!")
                    continue

                tickets = get_number("How many tickets do you want to book? ")

                booked_seats = [
                    b["seat"] for b in cart_bookings
                    if b["movie"] == selected_movie
                    and b["show"] == selected_show
                ]

                available_seats = [
                    s for s in seats
                    if s not in booked_seats
                    and s not in pending_seats
                ]

                if tickets <= 0:
                    print("Enter at least one ticket!")

                elif tickets > len(available_seats):
                    print("Only", len(available_seats), "seats available!")

                else:

                    cnt = 0

                    while cnt < tickets:

                        display_seats(selected_movie, selected_show)

                        selected2 = input("Select your seat: ").strip().lower()

                        if selected2 not in seats:
                            print("Seat not available!")

                        elif selected2 in booked_seats or selected2 in pending_seats:
                            print("Seat already selected or booked!")

                        else:
                            pending_seats.append(selected2)
                            pending_total += seat_prices[selected2]
                            cnt += 1

                            print("Selected seats:", pending_seats)
                            print("Tickets selected:", cnt)

                    print("Seats selected successfully!")

            elif choose == 4:

                if not pending_seats:
                    print("Please select seats first!")
                    continue

                print("Total Price:", pending_total)

                name = input("Please enter your name: ").strip()

                if not name:
                    print("Name cannot be empty!")
                    continue

                while True:

                    mobileno = input("Please enter your mobile number: ").strip()

                    if len(mobileno) == 10 and mobileno.isdigit() and mobileno[0] in "6789":
                        break
                    else:
                        print("Enter a valid 10-digit mobile number!")

                for seat in pending_seats:

                    booking = {
                        "name": name,
                        "mobile": mobileno,
                        "movie": selected_movie,
                        "show": selected_show,
                        "seat": seat,
                        "price": seat_prices[seat]
                    }

                    cart_bookings.append(booking)

                    cart_movies.append(selected_movie)
                    cart_shows.append(selected_show)
                    cart_seats.append(seat)
                    cart_price.append(seat_prices[seat])

                total_price = pending_total

                print("\nYour ticket is booked successfully!")
                print("Customer Name:", name)
                print("Total Tickets:", len(pending_seats))
                print("Total Amount:", total_price)

                pending_seats = []
                pending_total = 0

            elif choose == 5:

                print("\n========== SRI RAM THEATRE ==========")

                if not cart_bookings:
                    print("No bookings available!")
                    continue

                customer_bookings = [
                    b for b in cart_bookings
                    if b["mobile"] == mobileno and b["name"] == name
                ]

                if not customer_bookings:
                    print("No bookings found!")
                    continue

                print("User Name:", name)
                print("Mobile Number:", mobileno)

                print(f'\n{"Movie":<15}{"Show":<15}{"Seats":<15}{"Price":<10}')
                print("-" * 55)

                bookings = {}

                for booking in customer_bookings:

                    key = (booking["movie"], booking["show"])

                    if key not in bookings:
                        bookings[key] = {"seats": [], "price": 0}

                    bookings[key]["seats"].append(booking["seat"])
                    bookings[key]["price"] += booking["price"]

                total = 0

                for key, value in bookings.items():

                    movie = key[0]
                    show = key[1]
                    seat_list = ",".join(value["seats"])
                    amount = value["price"]

                    total += amount

                    print(
                        f'{movie:<15}{show:<15}'
                        f'{seat_list:<15}{amount:<10}'
                    )

                print("-" * 55)
                print("Total Tickets:", len(customer_bookings))
                print("Total Amount:", total)

            elif choose == 6:
                break

            else:
                print("Invalid choice!")

    elif chc == 3:
        print("Thank you for using Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice! Please select 1, 2 or 3.")
