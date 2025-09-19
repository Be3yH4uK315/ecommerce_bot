from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

catalog_button = KeyboardButton(text="Каталог 🛍️")
cart_button = KeyboardButton(text="Корзина 🛒")
profile_button = KeyboardButton(text="Профиль 👤")

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[catalog_button, cart_button, profile_button]],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню"
)