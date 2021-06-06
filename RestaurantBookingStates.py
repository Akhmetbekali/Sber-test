from aiogram.dispatcher.filters.state import StatesGroup, State


class RestaurantBookingStates(StatesGroup):
    askTime = State()
    askPeopleNumber = State()
