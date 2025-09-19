from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import queries
from app.keyboards.reply import main_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession):
    await queries.add_user(
        session,
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        username=message.from_user.username
    )

    await message.answer(
        f"Здравствуйте, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в наш магазин!",
        reply_markup=main_keyboard
    )


@router.message(F.text == "Каталог 🛍️")
async def catalog_handler(message: Message):
    await message.answer("Открываю каталог...")
    # Здесь мы будем вызывать функцию для отображения категорий


@router.message(F.text == "Корзина 🛒")
async def cart_handler(message: Message):
    await message.answer("Открываю вашу корзину...")
    # Здесь мы будем вызывать функцию для отображения содержимого корзины