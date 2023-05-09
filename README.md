import telebot
from models import Users
from markaps import start_menu, back_, akses
from always_run import always


bot = telebot.TeleBot(token=" ")

@bot.message_handler(commands=["start"])
def start(message):
    user = Users.select().where(Users.uid == message.chat.id)
    if user:
        bot.send_message(message.chat.id,   f"Привет {message.from_user.full_name}. \nПриходите к нашему роботу. \nС помощью этого бота можно приобрести компьютерные аксессуары, ноутбуки, игровые наборы!")
        bot.send_message(message.chat.id, "Выберите один из следующих вариантов", reply_markup=start_menu)
    else:
        Users(
            firstname = message.from_user.first_name,
            lastname = message.from_user.last_name,
            username = message.from_user.username,
            uid = message.from_user.id
        ).save()


@bot.message_handler(commands=["yubor"])
def yubor(message):
    foydalanuvchilar = Users.select()
    for i in foydalanuvchilar:
        bot.send_photo(i.uid, open("upg.mp4", "rb").read(), caption="UPG jamoasidan salom!")

        
        
@bot.callback_query_handler(lambda c: c.data)
def answer_chat(callback):
    if callback.data == "select":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Выберите один из следующих вариантов!", reply_markup=akses)
    elif callback.data == "/help":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Если у вас возникли проблемы с использованием этого бота, вы можете связаться с @dracula98!", reply_markup=back_)
    elif callback.data == "back":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Выберите один из следующих вариантов!", reply_markup=start_menu)
    
    elif callback.data == "ИгровыеСборки":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """Сборка #5 |12700/3060Ti/16GB/250GB/1TB New 
Стильный и производительный игровой компьютер с видеокартой RTX 3060 Ti 8GB и процессором Intel Core i7 12700.
‼️ ТЕСТЫ В ИГРАХ ‼️
Параметры: 
MB: Z690
CPU: Intel Core i7 12700
Cooler: DeepCool AK620 
RAM: 2x8=16GB 3200Mhz 
SSD: NVMe 250GB
HDD: 1TB
GPU: RTX 3060Ti 8GB
PSU: Zalman 750W 
Case: MSI Gungnir 110M
Цена:14 775 000 сум
Для заказа:https://upg.uz/ru/products/sborkaa5""")
        bot.send_message(callback.message.chat.id, """Сборка #4 |12400F/3060Ti/16GB/250GB New
Стильный и производительный игровой компьютер с видеокартой RTX 3060 Ti 8GB и процессором Intel Core i5 12400F.
‼️ ТЕСТЫ В ИГРАХ ‼️
Параметры: 
MB: B660M
CPU: Intel Core i5 12400F
Cooler: AC90D4
RAM: 2x8=16GB 3200Mhz 
SSD: NVMe 250GB
GPU: RTX 3060Ti 8GB
PSU: Zalman 700W 
Case: DeepCool CC560 ARGB
Цена:10 352 000 сум
Для заказа:https://upg.uz/ru/products/sborkaa4""")
        bot.send_message(callback.message.chat.id, """Сборка #2 |10400F/2060S/16GB/250GB New
Стильный и производительный игровой компьютер с видеокартой RTX 2060 SUPER 8GB и процессором Intel Core i5 10400F.
‼️ ТЕСТЫ В ИГРАХ ‼️
Параметры:
MB: H510M
CPU: Intel Core i5 10400F
Cooler: AC90D4
RAM: 2x8=16GB 2666Mhz 
SSD: NVMe 250GB
GPU: RTX 2060 SUPER 8GB
PSU: Zalman 600W 
Case: MG11TG RGB
Цена:7 684 000 сум
Для заказа:https://upg.uz/ru/products/sborka-2""")

        bot.send_message(callback.message.chat.id, """Сборка #1 |10400F/1650/16GB/250GB New
Стильный и производительный игровой компьютер с видеокартой GTX 1650 4GB и процессором Intel Core i5 10400F.
‼️ ТЕСТЫ В ИГРАХ ‼️
Параметры: 
MB: H510M
CPU: Intel Core i5 10400F
Cooler: AC90D4
RAM: 2x8=16GB 2666Mhz 
SSD: NVMe 250GB
GPU: GTX 1650 4GB
PSU: Zalman 500W 
Case: MG02TG RGB
Цена:5 814 000 сум
Для заказа:https://upg.uz/ru/products/sborka-1""", reply_markup=akses)


    elif callback.data == "Клавиатуры":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Logitech PRO KDA GX-Brown 
Тип клавиатуры	Механическая
Тип переключателей GX Brown Tactile
Интерфейс USB
Внутренняя память Есть
Подсветка  RGB
Подставка для рук Нет
Укладка кабеля	Нет
Количество клавиш 87
Длина провода 1.8 м
Размеры	361 х 153 х 34 мм
Вес 980 г
Цена: 1 824 000 сум
Для заказа:https://upg.uz/ru/products/logitech-pro-lol-kda""")
        bot.send_message(callback.message.chat.id, """
Logitech G PRO X LoL Keyboard
Тип клавиатуры	Механическая
Тип переключателей Logitech GX Brown
Интерфейс USB
Подсветка RGB
Внутренняя память Есть
Подставка для рук Нет
Укладка кабеля	Нет
Количество клавиш 89
Длина провода 1.8 м
Размеры	361 х 153 х 34 мм
Вес 980г
Цена:1 653 000 сум
Для заказа: https://upg.uz/ru/products/g-pro-lol""")
        bot.send_message(callback.message.chat.id, """
AKKO 3087 Mirror of the Sky Cherry MX Red/RU/Blue
Тип клавиатуры	Механическая
Тип переключателей Cherry MX Red
Интерфейс USB
Подсветка Нет
Внутренняя память	
Подставка для рук Нет
Укладка кабеля	Нет
Количество клавиш 87
Длина провода 1.8 м
Размеры	360 х 140 х 40 мм
Вес 950г
Цена:1 243 000 сум
Для заказа: https://upg.uz/ru/products/akko-3087-mirror-of-the-sky-cherry-mx-red-ru""")
        bot.send_message(callback.message.chat.id, """
2E Gaming KG350 Black
ип клавиатуры Мембранная
Тип переключателей	
Интерфейс USB
Подсветка RGB
Внутренняя память Есть
Подставка для рук Нет
Укладка кабеля	Нет
Количество клавиш 68
Длина провода 1.6 м
Размеры	323x106x35 мм
Вес 350г
Цена: 206 000 сум
Для заказа: https://upg.uz/ru/products/2e-gaming-kg350-black""", reply_markup=akses)
    
    
    
    elif callback.data == "Ноутбуки":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
ASUS X515J
Процессор Intel Core i3-1005G1
Оперативная память DDR4 4GB
Хранилище PCIEG3 512GB
Видеокарта	
Экран 15.6 FHD (1920x1080), 60hz
Доп	
Wi-Fi	Wi-Fi IEEE 802.11ac, Bluetooth 4.2
Цена: 4 332 000 сум
Для заказа: https://upg.uz/ru/products/x515j""")
        bot.send_message(callback.message.chat.id, """
Asus TUF Gaming A17 (P/N 90NR0972-M001N0) JAEGER GRAY
Процессор	AMD Ryzen 7 6800H
Оперативная память	DDR5 2x8GB (16GB) 4800
Хранилище	1TB NVMe SSD Gen3x4
Видеокарта	RTX 3060 GDDR6 6GB
Экран	17.3 FHD (1920x1080), 144hz IPS
Доп	
Wi-Fi	
Цена: 10 032 000 сум
Для заказа: https://upg.uz/ru/products/fx506hc-hn011""")
        bot.send_message(callback.message.chat.id, """
Asus TUF Gaming F15 (P/N 90NR0753-M007U0) Eclipse Gray
Ноутбук TUF Gaming F15 представляет собой особо надежную геймерскую платформу, которая поможет вам добиться победы в любой игре. Современная конфигурация делает его универсальным устройством, которое готово обеспечить отличную скорость в широком спектре приложений, будь то игры, стриминг или что-то иное.
Корпус TUF Gaming F15 стал более компактным и легким, чем у предыдущих моделей серии, однако в него встроен аккумулятор большей емкости, что обеспечивает длительное время автономной работы. Малый вес и емкий аккумулятор делают данный ноутбук подлинно мобильным устройством.
Цена: 17 556 000 сум
Для заказа:https://upg.uz/ru/products/90nr0972-m001n0""", reply_markup=akses)
    
    
    elif callback.data == "Наушники":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Sony PlayStation Pulse 3D
Тип наушников Полноразмерные
Режим работы 2.4 ГГц
Тип звучания Стерео
Размер динамиков (мм) 50 мм
Частотный диапазон наушников	
Сопротивление наушников	
Чувствительность наушников	
Чувствительность микрофона	
Подключение, разъемы USB-C (только питание)/mini jack 3.5 mm combo
Звуковая карта	
Длина провода	
Подсветка	Нет
Вес 600 г 
Цена: 1 368 000 сум
Для заказа:https://upg.uz/ru/products/playstation-pulse-3d""")
        bot.send_message(callback.message.chat.id, """
Sony PlayStation Pulse 3D Black
Тип наушников Полноразмерные
Режим работы 2.4 ГГц
Тип звучания Стерео
Размер динамиков (мм) 50 мм
Частотный диапазон наушников	
Сопротивление наушников	
Чувствительность наушников	
Чувствительность микрофона	
Подключение, разъемы USB-C (только питание) / mini jack 3.5 mm combo
Звуковая карта	
Длина провода	
Подсветка  Нет
Вес 600 г
Цена:1 368 000 сум
Для заказа:https://upg.uz/ru/products/pulse-3d-black""")
        bot.send_message(callback.message.chat.id, """
Logitech G733 White
Тип наушников Полноразмерные
Режим работы 2.4 ГГц, Провод
Тип звучания Виртуальный объемный звук 7.1
Размер динамиков (мм) 40 мм
Частотный диапазон наушников 20 - 20000 Гц
Сопротивление наушников	39 Ом
Чувствительность наушников 87.5 дБ SPL
Частотный диапазон микрофона 100 - 10000 Гц
Чувствительность микрофона
Подключение, разъемы
Звуковая карта	Встроенная
Длина провода
Подсветка RGB
Вес 278 г
Цена:1 881 000 сум
Для заказа:https://upg.uz/ru/products/logitech-g733-kda""")
        bot.send_message(callback.message.chat.id, """
Logitech G PRO X LoL Headset
Тип наушников Полноразмерные
Режим работы Проводной
Тип звучания DTS HEADPHONE:X 2.0
Размер динамиков (мм) 50 мм
Частотный диапазон наушников 20 - 20 000 Гц
Сопротивление наушников	35 Ом
Чувствительность наушников 91.7 дБ SPL
Частотный диапазон микрофона 100 - 10000 Гц
Чувствительность микрофона	
Подключение, разъемы 3.5 мм или USB
Звуковая карта	
Длина провода 2 м
Подсветка	Нет
Вес	320 г
Цена:1 585 000 сум
Для заказа:https://upg.uz/ru/products/981-001105""", reply_markup=akses)
    
    
    elif callback.data == "Мышки":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """ 
Xtrfy MZ1 RGB White Rail
Особенности:
- Разработана вместе с известным видеоблогером Rocket Jump Ninja.
- Имеет необычную форму, которая совсем непохожа на другие мышки.
- Легкая конструкция и хорошая начинка.
- Быстрый и точный оптический сенсор — Pixart 3389.
Цена: 1 015 000 сум
Для заказа: https://upg.uz/ru/products/xtrfy-mz1-rgb-white-rail""")
        bot.send_message(callback.message.chat.id, """ 
Xtrfy M4 Pink RGB
Серия Project 4
Xtrfy M4 — это часть линейки игровых мышек под названием Project 4. Вся серия задумывалась с целью предложить геймерам что-то абсолютно новое с точки зрения расцветок, ведь большинство девайсов на рынке в основном выполнены в одних и тех же стандартных цветах. А с M4 все наоборот, ведь она гораздо оригинальнее других благодаря необычным цветовым решениям разработчиков.
Цена: 741 000 сум
Для заказа: https://upg.uz/ru/products/xtrfy-m4-pink-rgb""")
        bot.send_message(callback.message.chat.id, """ 
Logitech G PRO Wireless LoL Mouse
Тип сенсора Оптический HERO 25K
Максимальное разрешение DPI/CPI	25600
Количество кнопок 8
Частота опроса	1000 Гц
Акселерация (максимальное ускорение) 40 G
Подсветка RGB
Внутренняя память Есть
Режим работы 2.4 ГГц, Провод
Тип провода	
Длина провода 1.8 м
Вес с кабелем	
Вес без кабеля 80г
Размеры	125 x 63 x 40 мм
Цена: 1 824 000 сум
Для заказа: https://upg.uz/ru/products/910-006449""")
        bot.send_message(callback.message.chat.id, """ 
2E Gaming HyperSpeed Lite RGB Retro White
Тип сенсора Оптический PixArt PMW 3325
Максимальное разрешение DPI/CPI	10000
Количество кнопок 6
Частота опроса 1000 Гц
Акселерация (максимальное ускорение) 20 G
Подсветка RGB
Внутренняя память Есть
Режим работы Проводной
Тип провода Нейлоновая оплетка USB 2.0
Длина провода 1.8 м
Вес с кабелем 68г
Вес без кабеля	
Размеры	126 x 68 x 39 мм
Цена: 274 000 сум
Для заказа: https://upg.uz/ru/products/2egaming-hyperspeed-lite-retro-white""", reply_markup=akses)
    else:
        bot.send_message(callback.message.chat.id, "Если у вас возникли проблемы с использованием этого бота, вы можете связаться с @!", reply_markup=back_)

always()
bot.infinity_polling()
