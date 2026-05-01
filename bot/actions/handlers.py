from aiogram import Router, F, Bot
from aiogram.filters.command import Command
from aiogram.types import (ReplyKeyboardMarkup, 
                           Message, 
                           InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton, 
                           CallbackQuery)

router = Router()

could_send_tech_team = False







def start_reply_btns():
    markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Профиль", callback_data='profile'), KeyboardButton(text="Купить подписку", callback_data="subscribe")]]
    )
    return markup

@router.callback_query(lambda c: c.data == "profile")
async def profile_event(callback):
    await callback.message.answer('hello1')

@router.callback_query(lambda c: c.data == "subscribe")
async def subscribe_event(callback):
    await callback.message.answer("выбирите продолжительность подписки")

@router.message(Command('start'))
async def begin(message: Message):
    await message.answer('добро пожаловать в -------, нажмите на *Профиль если хотите увидеть дополнительную информацию*, нажмите на *Купить подписку* если хотите приобрести подписку', reply_markup=start_reply_btns())
    
    
    
    



def subscribes_buttons():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1 месяц", callback_data="one_month"),InlineKeyboardButton(text="3 месяца", callback_data="three_month")],
            [InlineKeyboardButton(text="6 месяцев", callback_data="six_month"), InlineKeyboardButton(text="12 месяцев", callback_data="twelve_month")]
        ]
    )
    return markup

def yes_or_not():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="wants_to_buy"), InlineKeyboardButton(text="Нет", callback_data="doesnt_want_to_buy")]]
    )
    return markup

@router.callback_query(lambda c: c.data =="wants_to_buy")
async def buying_subscribe(callback: CallbackQuery):
    # await message.answer('подальший код при согласии...')
    await callback.message.answer('выбирите подписку', reply_markup=subscribes_buttons())
    
@router.callback_query(lambda c: c.data =="one_month")
async def buying_subscribe(callback: CallbackQuery):
    # await message.answer('подальший код при согласии...')
    await callback.message.answer('подписка на 1 месяц успешно обретена!')
    
@router.callback_query(lambda c: c.data =="three_month")
async def buying_subscribe(callback: CallbackQuery):
    # await message.answer('подальший код при согласии...')
    await callback.message.answer('подписка на 3 месяца успешно обретена!')
    
@router.callback_query(lambda c: c.data =="six_month")
async def buying_subscribe(callback: CallbackQuery):
    # await message.answer('подальший код при согласии...')
    await callback.message.answer('подписка на 6 месяцев успешно обретена!')
    
@router.callback_query(lambda c: c.data =="twelve_month")
async def buying_subscribe(callback: CallbackQuery):
    # await message.answer('подальший код при согласии...')
    await callback.message.answer('подписка на 12 месяцев успешно обретена!')

@router.message(F.text == "Купить подписку")
async def buy_subscribe(message: Message):
    await message.answer("у вас нет в наличии активных подписок, желаете приобрести?", reply_markup=yes_or_not())


@router.message(F.text == "Профиль")
async def buy_subscribe(message: Message):
    await message.answer("ваш профиль: ")



    
@router.callback_query(lambda c: c.data =="doesnt_want_to_buy")
async def buying_subscribe(message: Message):
    await message.answer('подальший код при отказе...')
    




@router.message(Command("support"))
async def support(message: Message):
    global could_send_tech_team
    could_send_tech_team = True
    await message.answer(f"Здраствуйте! Меня зовут Ирина, как я могу вам помочь 😃?")

chat_user_id = None

def stop_chat():
    global could_send_tech_team
    could_send_tech_team = False

@router.message(F.text)
async def speech(message: Message, bot: Bot):        
    if could_send_tech_team:
        if message.text == "/exit":
            await message.answer('спасибо за диалог, было приятно с вами пообщатся :) Всего доброго!')
            stop_chat()
            await bot.send_message(chat_id=7449889285, text="пользователь закончил диалог")
        if not message.chat.id == 7449889285:
            await bot.send_message(chat_id=7449889285, text=f"сообщение: {message.text} \n id чата: {message.chat.id}")
            global chat_user_id
            chat_user_id = message.chat.id
        else:
            await bot.send_message(chat_id=chat_user_id, text=message.text)
            
    else:
        await message.reply(f'извините но данная команда не разпознана :(')
