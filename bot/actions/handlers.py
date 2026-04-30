from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import (ReplyKeyboardMarkup, 
                           Message, 
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton, 
                           callback_query)




router = Router()


    
def start_reply_btns():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="profile", callback_data='profile')],
        [InlineKeyboardButton(text="subscribe", callback_data="subscribe")]]
    )
    return markup


@router.callback_query(lambda c: c.data == "subscribe")
async def subscribe_event(callback):
    await callback.message.answer('hello1')
    
@router.callback_query(lambda c: c.data == "profile")
async def profile_event(callback):
    await callback.message.answer('hello2')


@router.message(Command('start'))
async def begin(message: Message):
    await message.answer("some text", reply_markup=start_reply_btns())





# class Form(StatesGroup):
#     name = State()
#     email = State()
#     phone_number = State()
#     password = State()

# @router.message(Command('start'))
# async def start_program(message: types.Message, state: FSMContext):
#     await message.answer("Добро пожаловать в -------! \n Мы рады тебя приветствовать и готовы предложить самые лучшие условия, но перед эти давай пройдем регистрацию\n напиши свое имя")
#     await state.set_state(Form.name)

# @router.message(Form.name, F.text)
# async def set_name(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer('отлично теперь напиши свою почту:')
#     await state.set_state(Form.email)
    

# @router.message(Form.email, F.text)
# async def set_email(message: types.Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     await message.answer('отлично теперь напиши свой номер телефона (начиная с индекса...):')
#     await state.set_state(Form.phone_number)
    
# @router.message(Form.phone_number, F.text)
# async def set_phone_number(message: types.Message, state: FSMContext):
#     await state.update_data(phone_number=message.text)
#     await message.answer('отлично теперь теперь придумай пароль:')
#     await state.set_state(Form.password)
    
# @router.message(Form.password, F.text)
# async def set_password(message: types.Message, state: FSMContext):
#     await state.update_data(password=message.text)
    
#     data = await state.get_data()
#     name = data["name"]
#     phone_number = data["phone_number"]
#     email = data["email"]
#     password = data["password"]
    
#     await message.answer(f'анкета заполнена! Все ли правильно указано?\n\n имя: {name}\n номер телефона: {phone_number}\n email: {email}\n пароль: {password}')
    
    

    # await state.set_state()
    
# @router.message(Command('cancel'))
# async def cancel_form(message: types.Message, state: FSMContext):
#     await state.clear()

