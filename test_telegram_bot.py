import pytest

from unittest.mock import AsyncMock

from RestaurantBookingStates import *
from TelegramBot import TelegramBot

bot = TelegramBot()


@pytest.mark.asyncio
async def test_datetime_handler():
    response = 'Неверная дата или время'
    mock1 = "99/99/99"
    message_mock1 = AsyncMock(text=mock1)
    await bot.handle_datetime(message=message_mock1, state=RestaurantBookingStates.askTime)
    message_mock1.answer.assert_called_with(response)


@pytest.mark.asyncio
async def test_person_handler():
    response = 'Укажите число'
    text_mock = "qwe"
    message_mock = AsyncMock(text=text_mock)
    await bot.handle_person(message=message_mock, state=RestaurantBookingStates.askTime)
    message_mock.answer.assert_called_with(response)


@pytest.mark.asyncio
async def test_negative_person_handler():
    response = 'Введите число больше нуля'
    text_mock = "-100"
    message_mock = AsyncMock(text=text_mock)
    await bot.handle_person(message=message_mock, state=RestaurantBookingStates.askTime)
    message_mock.answer.assert_called_with(response)
