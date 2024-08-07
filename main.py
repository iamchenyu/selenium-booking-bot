from booking.booking import Booking

# context manager
with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.close_signin_popup()
    bot.search_place_togo("New York")