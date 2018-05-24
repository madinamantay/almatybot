import telebot 
from telebot import types 
import const 

bot = telebot.TeleBot(const.API_TOKEN) 

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) 
btn_address = types.KeyboardButton('Топ — 10 романтических мест в Алматы') 
btn_payment = types.KeyboardButton('Пять мест вблизи Алматы, которые должен посетить каждый') 
btn_delivery = types.KeyboardButton('Места для бега в Алматы')   
btn_place = types.KeyboardButton('Антикафе')  
btn_delivery3 = types.KeyboardButton('Музеи')  
btn_delivery4 = types.KeyboardButton('Природа и парки') 
btn_delivery5 = types.KeyboardButton('Квесты')
btn_delivery6 = types.KeyboardButton('Караоке')
btn_delivery7 = types.KeyboardButton('Кинотеатры')
btn_delivery8 = types.KeyboardButton('Аквапарки')
markup_menu.add(btn_address, btn_delivery, btn_payment, btn_place, btn_delivery3, btn_delivery4, btn_delivery5, btn_delivery6, btn_delivery7, btn_delivery8)

@bot.message_handler(commands=['start', 'help']) 
def send_welcome(message): 
    bot.reply_to(message, "Привет мой друг! Хочешь посетить все лучшие места в Алматы, то тогда ты пришел по адресу))Almacitybot был разработан специально для наших любимых гостей ))\U0001f525 Удачи в путешествие!!! 😊 ", reply_markup=markup_menu)  
    bot.send_photo(message.chat.id, open('photos/alma.jpg', 'rb'))

@bot.message_handler(func=lambda message: True) 
def echo_all(message):   
    if message.text == "Топ — 10 романтических мест в Алматы":
        bot.reply_to(message, "1.Парк Первого Президента \n2.Звездная поляна \n3.Высокогорный каток Медеу \n4.Ботанический Сад \n5.Аллея Любви \n6.Большое Алматинское озеро \n7.Международный комплекс лыжных трамплинов \n8.Мост любви \n9.Скамья примирений \n10.«Романтический дворик» около Столичного", reply_markup=markup_menu)  
        bot.send_photo(message.chat.id, open('photos/Roman.jpg', 'rb'))
    elif message.text == "Пять мест вблизи Алматы, которые должен посетить каждый":
        bot.reply_to(message, "1.ЧАРЫНСКИЙ КАНЬОН \n2.БОЛЬШОЕ АЛМАТИНСКОЕ ОЗЕРО \n3.ГОРЯЧИЕ ИСТОЧНИКИ В ЧУНДЖЕ \n4.ОЗЕРО КАИНДЫ \n5.ПОЮЩИЙ БАРХАН", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/charyn.jpg', 'rb'))
    elif message.text == "Места для бега в Алматы":
        bot.reply_to(message, "1.Ботанический сад \n2.Терренкур \n3.Аллея вдоль Весновки \n4.Берег озера Сайран \n5.Стадион «Динамо» \n6.Парк Первого Президента \n7.Спортивно-тренировочный комплекс фонда Первого Президента РК \n8.Роща Баума \n9.Парк имени Ганди \n10.Лестница на Медеу ", reply_markup=markup_menu)  
        bot.send_photo(message.chat.id, open('photos/beg.jpg', 'rb'))    
    elif message.text == "Антикафе": 
        bot.reply_to(message, "1.Time cafe Relax \n2.Time Cafe на Мира \n3.Time Cafe Глобус \n4.Некафе USE \n5.Некафе на Маркова \n6.Некафе на Фурманова \n7.Некафе на Жандосова \n8.Антикафе «Ваниль» \n9.EastClub \n10.Антикафе «Как дома» ", reply_markup=markup_menu) 
        bot.send_photo(message.chat.id, open('photos/anticafe.jpg', 'rb'))
    elif message.text == "Музеи": 
        bot.reply_to(message, "1.Музей народных музыкальных инструментов имени Ыхласа \n2.Музей Искусств Республики Казахстан им. Кастеева \n3.Центральный государственный музей республики Казахстан \n4.Музей археологии \n5.Музей занимательных наук Экспериментум ", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/muzey.jpg', 'rb'))   
    elif message.text == "Природа и парки": 
        bot.reply_to(message, "1.Кольсайские озера \n2.Парк имени 28-ми гвардейцев-панфиловцев \n3.Гора Кок Тобе \n4.Озеро Иссык \n5.Алматинский терренкур", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/park.jpg', 'rb'))
    elif message.text == "Квесты": 
        bot.reply_to(message, "1.Карательная психиатрия. Часть 1 \n2.Приют: Пропавшие без вести \n3.Коллекционер страха \n4.Игра престолов \n5.Карты, деньги, два ствола \n6.Сон \n7.Цирк Кейна ", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/kvest.jpg', 'rb'))
    elif message.text == "Караоке": 
        bot.reply_to(message, "1.Rock Crystal  \n2.Fa-Sol на Макатаева \n3.MEGA Karaoke Korea Sikdang \n4.Quartet \n5.Alma Blues \n6.Grand Osteria \n7.La Fondue", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/karaoke.jpg', 'rb'))
    elif message.text == "Кинотеатры": 
        bot.reply_to(message, "1.Cinema Towers 3D \n2.Star Cinema 3D \n3.Nomad Cinema \n4.Кинотеатр Арман \n5.Bekmambetov Cinema \n6.CINEMAX Dostyk Multiplex \n7.Kinopark 11 IMAX Esentai \n8.Кинотеатр Цезарь \n9.Chaplin Cinemas(Mega) \n10.Сары-Арка ", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/kino.jpg', 'rb'))
    else:
        bot.reply_to(message, "1.Аквапарк в парке им. Горького «Восьмое чудо света» \n2.Аквапарк Family Park \n3.Аквапарк Алматы «Дельфин» (летний бассейн) \n4.Аквапарк в Алматы «Hawaii» (крытый) \n5.Аквапарк Алматы «Мереке» (пос. Байсерке) \n6.Капчагайский аквапарк \n7.Аквапарк Алатау (крытый)", reply_markup=markup_menu)
        bot.send_photo(message.chat.id, open('photos/akva.jpg', 'rb'))

if __name__ == '__main__':

    print('Starting ALmacityBot')

    bot.polling()
