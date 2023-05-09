import telebot
from models import Users
from markups import start_menu, back_, akses
from always_run import always


bot = telebot.TeleBot(token=" ")
@bot.message_handler(commands=["start"])
def start(message):
    user = Users.select().where(Users.uid == message.chat.id)
    if user:
        bot.send_message(message.chat.id,  f"Assalom aleykum {message.from_user.full_name}. \nXush kelibsiz botimizga! \nBu bot yordamida online meva sotib olishingiz mumkin!🛒🛒")
        bot.send_message(message.chat.id, "Quyidagilardan birini tanlang!", reply_markup=start_menu)
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
        bot.send_photo(i.uid, open("mrbean.webp", "rb").read(), caption="Mr Bean dan salom!")



@bot.callback_query_handler(lambda c: c.data)
def answer_chat(callback):
    if callback.data == "select":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Quyidagilardan birini tanlang!", reply_markup=akses)
    elif callback.data == "/help":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Bu botda hatolik yuz berdimi!, Admin bilan boglaning @dracula98", reply_markup=back_)
    elif callback.data == "sotibolish":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!", reply_markup=back_)

    elif callback.data == "back":
        bot.answer_callback_query(callback.id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Quyidagilardan birini tanlang!", reply_markup=start_menu)
    
    elif callback.data == "MandarinTurkiya":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 19 990 сум.(19 990 сум. за 1кг)
Tarixi: Ushbu o'simlik va uning mevalarining nomi ispancha " mandarino "dan kelib chiqqan bo'lib, u o'z navbatida" se mondar " – "tozalash oson" dan kelib chiqqan. Mandarinlarni yangi iste'mol qilish, quritish, quritish, ulardan shakarlamalar, sharbatlar tayyorlash mumkin. Pishirishda nafaqat pulpa, balki qobig'i ham mashhur. Mevalar shirinliklar, shirin va nordon soslar va marinadlar tayyorlash uchun ishlatiladi. Sharbat-alkogolli va alkogolsiz ichimliklarda
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)

    elif callback.data == "Turkiyaapelsinlari":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 24 990 сум.(24 990 сум. за 1кг)
Tarixi: Yarim kislotali shirin ta'mga ega suvli apelsinlar s vitaminiga boy, bu quvnoq sitrus mevalari butun organizmning ishini faollashtiradi, vitamin etishmasligi va charchoqqa qarshi kurashda yordam beradi.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "Anor":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 19 990 so'm.(19 990 so'm 1kg mi) 
Tarixi: Anor tarkibida C, B6, B12, P vitaminlari va kaltsiy, magniy, temir va boshqalar kabi mikroelementlar mavjud. Anor sharbati o'simlik kislotalari bilan to'yingan, shuning uchun u ishtahani qo'zg'atadi va oshqozonning past kislotaligi bilan ovqat hazm qilishga yordam beradi. Anor go'sht bilan yaxshi ketadi, shuning uchun go'sht idishlari uchun marinadlar va soslar tayyorlanadi. Bundan tashqari, don va anor sharbati qovurilgan, dimlangan va qaynatilgan idishlar, konservalar va pastillalarni tayyorlash uchun ishlatiladi.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "OlmaPinkLady":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 13,990(13,990. 1 kg uchun) 
Tarixi: Ushbu olma navi engil nordonlik va qulupnayning nozik xushbo'yligi bilan ajralib turadi. Meva go'shti tiniq va zich bo'lib, ularni salatlarda ham, pishirishda ham ishlatishga imkon beradi. Pushti xonim eng kech pishadigan navlardan biridir: olma faqat oktyabr oyining oxirida yig'ib olinadi. Bu xilma-xillik pushti rangga ega bo'lgan kuzning salqin kechalari. Ushbu pozitsiyada mahalliy ishlab chiqarilgan olma mavjud.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "ПомидорыPinkParadiseвес":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 24 990 so ' m.(24 990 so ' m) 1 kg uchun) 
Tarixi: Pushti navlarning pomidorlari katta o'lchamlari, go'shti, nozik va shirin ta'mi bilan ajralib turadi. Pushti pomidorlar yangi iste'mol qilish va salatlarga qo'shish uchun juda mos keladi. Biroq, ular tuzlangan, konservalangan va tuzlangan bo'lishi mumkin. Bu lazzat masalasidir.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "Limon":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi:  18 990 so ' m.(18 990 so ' m) 1 kg uchun)
Tarixi: Ushbu yorqin sariq mevalar uzoq vaqtdan beri dorivor xususiyatlari uchun eng yaxshi sotuvchi bo'lib kelgan. Axir, limonli bir piyola choy sovuq kunlarda isinadi, tanani ko'tarishga yordam beradi, farovonlikni yaxshilaydi va infektsiyalarga chidamliligini oshiradi. Bundan tashqari, limon pishirishda va qandolat mahsulotlarini ishlab chiqarishda eng ko'p terilgan lazzatlardan biridir. Ushbu limonlar og'irlik bilan sotiladi, faqat kerakli miqdordagi kg ni tanlang.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "Mango":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 20 990 so ' m.(20 990 so ' m) 1 dona uchun) 
Tarixi: Mango foydali moddalarga boy: rux, marganets, temir, fosfor, kaltsiy, shuningdek b vitaminlari (B1, B2, B5, B6, B9), A, D va S vitaminlari.bundan tashqari, undagi askorbin kislotasi limon sharbatiga qaraganda bir oz kamroq.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "EronKiwisi":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi: 19,990.(Men 19,990. 1 kg uchun) 
Tarixi: Kivi issiq iqlimi bo'lgan mamlakatlarda etishtiriladi — xususan, bu partiya Eronda pishgan. Meva ko'pincha xom ashyo bilan iste'mol qilinadi, ammo undan murabbo, pirojnoe va hatto go'shtli idishlar uchun tuzlamoq ham tayyorlash mumkin.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)
    
    elif callback.data == "GreypfrutTurkiya":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, """
Narxi:  26,990.Men 26,990. 1 kg uchun)  
Tarixi: Greypfrutning metabolizmni kuchaytirish qobiliyati va tanadagi yog'larning yonishi uni ko'plab moda parhezlarining majburiy atributiga aylantirdi. Meva pulpasida Xolesterolni parchalaydigan va qon shakarini kamaytiradigan moddalar mavjud. Kuz-qish davrida greyfurtdan foydalanish vitamin etishmasligidan qochishga va immunitetni qo'llab-quvvatlashga yordam beradi, yorqin rang va aniq yozgi hid sizni xursand qiladi.
Maxsulotlarni shu sayt:https://lebazar.uz/ orqali sotib olishingiz mumkin!!""", reply_markup=back_)

    else:
        bot.send_message(callback.message.chat.id, "Agar siz ushbu botdan foydalanishda muammolarga duch kelsangiz😤😡, Admin👉🏻👉🏻: @dracula98 bilan bog'lanishingiz mumkin!", reply_markup=back_)

always()
bot.infinity_polling()
