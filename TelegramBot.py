from abc import ABC
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from RestaurantBookingStates import *

TOKEN = "1839434383:AAHwtnLRfHruXJ91zg5tDNeiSDCKKkue0uk"


class TelegramBot(ABC):
    def __init__(self):
        self._bot = Bot(token=TOKEN)
        self._storage = MemoryStorage()
        self._dp = Dispatcher(self._bot, storage=self._storage)

        self._dp.register_message_handler(self.cmd_start, commands=["start"], state='*')
        self._dp.register_message_handler(self.cmd_cancel, commands=["cancel"], state='*')
        self._dp.register_message_handler(self.cmd_book, commands=["book"], state='*')
        self._dp.register_message_handler(self.handle_datetime, state=RestaurantBookingStates.askTime)
        self._dp.register_message_handler(self.handle_person, state=RestaurantBookingStates.askPeopleNumber)

    async def cmd_start(self, message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer("Введите /book что бы забронировать стол")

    async def cmd_book(self, message: types.Message):
        await message.reply("Здравствуйте! Пожалуйста, введите дату и время брони в формате: ДД/ММ/ГГ ЧЧ:ММ")
        await RestaurantBookingStates.askTime.set()

    async def cmd_cancel(self, message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer("Отменено. Что бы начать заново введите /book")

    async def handle_datetime(self, message: types.Message, state: FSMContext):
        try:
            time = datetime.strptime(message.text, '%d/%m/%y %H:%M')
            await state.update_data(chosenTime=time)
            await RestaurantBookingStates.next()
            await message.answer("Пожалуйста, укажите количество человек (в цифрах)")
        except ValueError:
            await message.answer("Неверная дата или время")

    async def handle_person(self, message: types.Message, state: FSMContext):
        try:
            assert int(message.text) > 0
            await state.update_data(personNumber=message.text)
            data = await state.get_data()
            await message.answer(f"Вы забронировали столик {data['chosenTime']} на {data['personNumber']} человек")
            await state.finish()
        except ValueError:
            await message.answer("Укажите число")
        except AssertionError:
            await message.answer("Введите число больше нуля")

    def start(self):
        executor.start_polling(self._dp, skip_updates=True)
