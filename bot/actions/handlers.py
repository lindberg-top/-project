from aiogram import Router, F, Bot
from aiogram.filters.command import Command
from aiogram.types import (ReplyKeyboardMarkup, 
                           Message, 
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton, 
                           callback_query)

router = Router()

could_send_tech_team = False
    
def start_reply_btns():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="profile", callback_data='profile')],
        [InlineKeyboardButton(text="subscribe", callback_data="subscribe")]]
    )
    return markup


    
@router.callback_query(lambda c: c.data == "profile")
async def profile_event(callback):
    await callback.message.answer('hello1')

@router.callback_query(lambda c: c.data == "subscribe")
async def subscribe_event(callback):
    await callback.message.answer('hello2')

@router.message(Command('start'))
async def begin(message: Message):
    await message.answer(f"id: {message.chat.id}", reply_markup=start_reply_btns())



@router.message(Command("support"))
async def support(message: Message):
    global could_send_tech_team
    could_send_tech_team = True
    await message.answer(f"Здраствуйте! Меня зовут Ирина, как я могу вам помочь 😃? \n staus {could_send_tech_team}")


chat_user_id = None

@router.message(F.text)
async def speech(message: Message, bot: Bot):
    if message.text == "/exit":
        await message.answer('спасибо за диалог, было приятно с вами пообщатся :) Всего доброго!')
        global could_send_tech_team
        could_send_tech_team = False
        await bot.send_message(chat_id=7449889285, text="пользователь закончил диалог")
        
    if could_send_tech_team:
        if not message.chat.id == 7449889285:
            await bot.send_message(chat_id=7449889285, text=f"сообщение: {message.text} \n id чата: {message.chat.id}")
            global chat_user_id
            chat_user_id = message.chat.id
        else:
            # print(message.text)
            await bot.send_message(chat_id=chat_user_id, text=message.text)
            
    else:
        await message.reply(f'извините но данная команда не разпознана :( \n status: {could_send_tech_team}')

# @router.message(Command("exit"))
# async def exit_chat(message: Message):
#     await message.answer('спасибо за диалог, было приятно с вами пообщатся :) Всего доброго!')
#     global could_send_tech_team
#     could_send_tech_team = False
    
    
    

# else:
# @router.message(F.text)
# async def error(message: Message):
#     global could_send_tech_team
#     await message.reply(f'извините но данная команда не разпознана :( \n status: {could_send_tech_team}')
            
            

            
            
            
            # @router.message(F.text)
            # async def tech_response(message_l: Message, bot: Bot):







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

