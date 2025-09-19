from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from .models import User, Category, Product, CartItem


async def add_user(session: AsyncSession, user_id: int, first_name: str, username: str = None):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        new_user = User(user_id=user_id, first_name=first_name, username=username)
        session.add(new_user)
        await session.commit()
        return new_user
    return user


async def get_categories(session: AsyncSession):
    query = select(Category)
    result = await session.execute(query)
    return result.scalars().all()

async def get_products_by_category(session: AsyncSession, category_id: int):
    query = select(Product).where(Product.category_id == category_id)
    result = await session.execute(query)
    return result.scalars().all()

async def get_product_by_id(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def add_to_cart(session: AsyncSession, user_id: int, product_id: int):
    query = select(CartItem).where(CartItem.user_id == user_id, CartItem.product_id == product_id)
    result = await session.execute(query)
    cart_item = result.scalar_one_or_none()

    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=1)
        session.add(cart_item)

    await session.commit()
    return cart_item

async def get_cart_items(session: AsyncSession, user_id: int):
    query = (
        select(CartItem, Product)
        .join(Product, CartItem.product_id == Product.id)
        .where(CartItem.user_id == user_id)
    )
    result = await session.execute(query)
    return result.all()

async def clear_cart(session: AsyncSession, user_id: int):
    query = delete(CartItem).where(CartItem.user_id == user_id)
    await session.execute(query)