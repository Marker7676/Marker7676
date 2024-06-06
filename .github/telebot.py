import os
os.system('pip install requests')
import requests
os.system('pip install telebot')
import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

os.system('clear')

TOKEN = "6903667250:AAGQyUHDZr1yTYkC0B-WaEOW1vrMKZVwv-Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    user_username = message.from_user.username
    print("kulanıcı mesajı: {start_message} ")

    reply_text = f"╭━━━━━━━━━━━━━━━━━━\n┃➥Merhaba , {user_name}\n╰━━━━━━━━━━━━━━━━━━\n╭━━━━━━━━━━━━━━━━━━\n┃➥@kingmodturkiye Sorgu Botuna \n┃Hoş Geldin.\n┃\n┃Bot Şuan V0.2 Sürümündedir\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥komutları görmek icin /help komutunu \n┃girin\n╰━━━━━━━━━━━━━━━━━━"

    # Buton ekleme
    keyboard = InlineKeyboardMarkup()
    url_button = InlineKeyboardButton(text="Kanala Katıl", url="https://t.me/kingmodturkiye")
    keyboard.add(url_button)

    bot.send_message(message.chat.id, reply_text, reply_markup=keyboard)
    print( f"bot mesajı: {reply_text}")

@bot.message_handler(commands=['help'])
def help(message):
    help_text = (
        "╭━━━━━━━━━━━━━━━━━━\n┃➥İŞTE KOMUTLAR\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥/adsoyadililce komutuyla ad \n┃soyad il ve içe bilgilerine \n┃erişebilirsiniz\n┃\n┃➥/adsoyadil komutuyla ad soyad il ┃girerek sorgu atabilirsiniz\n┃\n┃➥/adsoyad komutuyla sadece ad \n┃soy ad girerek bilgilere \n┃erişebilirsiniz\n┃\n┃➥/tc komutuyla tc bilgileri e ┃erişebilirsiniz\n┃\n┃➥/tcpro komutuyla detayli tc sorgu ┃atabilirsiniz\n┃\n┃➥/aile komutuyla aile sorgu \n┃atabilirsiniz\n┃\n┃➥/ailepro komutuyla detaylı alie \n┃sorgu atabilirsiniz\n┃\n┃➥/tcdengsm komutunu kulanarak\n┃tc kimlik bilgisiyle kisinin bilgisine\n┃erişebilirsiniz\n┃\n┃➥/gsmdentc komutuyla telefon ┃numarasıyla tc kimlik bilgilerine ┃erişebilirsinizi\n╰━━━━━━━━━━━━━━━━━━"
    )
    bot.send_message(message.chat.id, help_text)
    print( f"bot mesajı: {help_text}")


@bot.message_handler(commands=["tc"])
def tc(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC kimlik numarası girmek \n┃gereklidir.\n┃\n┃➥Lütfen /tc komutunu kullanarak \n┃TC kimlik numarası girin\n╰━━━━━━━━━━━━━━━━━━\n╭━━━━━━━━━━━━━━━━━━\n┃➥Örnek: /tc 11111111111\n╰━━━━━━━━━━━━━━━━━━")
        return

    tc_number = message.text.split(' ')[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")
    response = requests.get(f'http://172.208.52.218/api/legaliapi/tc.php?tc={tc_number}')
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            formatted_text = f"╭━━━━━━━━━━━━━━━━━━\n┃➥Adı: {data['data'].get('ADI', 'Bilgi bulunamadı')}\n┃➥Soyadı: {data['data'].get('SOYADI', 'Bilgi bulunamadı')}\n┃➥TC Kimlik Numarası: {data['data'].get('TC', 'Bilgi bulunamadı')}\n┃➥Doğum Tarihi: {data['data'].get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n┃➥Doğum Yeri: {data['data'].get('NUFUSIL', 'Bilgi bulunamadı')} / {data['data'].get('NUFUSILCE', 'Bilgi bulunamadı')}\n┃➥Anne Adı: {data['data'].get('ANNEADI', 'Bilgi bulunamadı')}\n┃➥Anne TC Kimlik Numarası: \n┃➥{data['data'].get('ANNETC', 'Bilgi bulunamadı')}\n┃➥Baba Adı: {data['data'].get('BABAADI', 'Bilgi bulunamadı')}\n┃➥Baba TC Kimlik Numarası: \n┃➥{data['data'].get('BABATC', 'Bilgi bulunamadı')}\n┃➥Uyruk: {data['data'].get('UYRUK', 'Bilgi bulunamadı') or 'Bilgi bulunamadı'}\n╰━━━━━━━━━━━━━━━━━━"
            chat_id = message.chat.id
            bot.send_message(chat_id, formatted_text)
            print( f"bot mesajı: {formatted_text}")
            bot.send_message(message.chat.id, "👍sorgu başaıiyla sonuçlandı👍")
        else:
            bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC kimlik numarasına ilişkin veriler ┃➥bulunamadı.\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥tc kimlik numarasını doğru girin\n┃\n┃➥örnek: tc 11111111111\n╰━━━━━━━━━━━━━━━━━━")
    else:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\nTC kimlik numarasına ilişkin veriler alınamadı.\n╰━━━━━━━━━━━━━━━━━━")

@bot.message_handler(commands=["tcpro"])
def tcpro(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC kimlik numarası girmek \n┃gereklidir.\n┃\n┃➥Lütfen /tcpro komutunu kullanarak \n┃TC kimlik numarası girin\n╰━━━━━━━━━━━━━━━━━━\n╭━━━━━━━━━━━━━━━━━━\n┃➥Örnek: /tcpro 11111111111\n╰━━━━━━━━━━━━━━━━━━")
        return

    tc_number = message.text.split(' ')[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")
    response = requests.get(f'http://172.208.52.218/api/legaliapi/tcpro.php?tc={tc_number}')
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            formatted_text = f"╭━━━━━━━━━━━━━━━━━━\n┃➥Adı: {data['data'].get('ADI', 'Bilgi bulunamadı')}\n┃➥Soyadı: {data['data'].get('SOYADI', 'Bilgi bulunamadı')}\n┃➥TC Kimlik Numarası: {data['data'].get('TC', 'Bilgi bulunamadı')}\n┃➥Doğum Tarihi: {data['data'].get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n┃➥Doğum Yeri: {data['data'].get('NUFUSIL', 'Bilgi bulunamadı')} / {data['data'].get('NUFUSILCE', 'Bilgi bulunamadı')}\n┃➥Anne Adı: {data['data'].get('ANNEADI', 'Bilgi bulunamadı')}\n┃➥Anne TC Kimlik Numarası: \n┃{data['data'].get('ANNETC', 'Bilgi bulunamadı')}\n┃➥Baba Adı: {data['data'].get('BABAADI', 'Bilgi bulunamadı')}\n┃➥Baba TC Kimlik Numarası: \n┃{data['data'].get('BABATC', 'Bilgi bulunamadı')}\n┃➥Uyruk: {data['data'].get('UYRUK', 'Bilgi bulunamadı') or 'Bilgi bulunamadı'}\n╰━━━━━━━━━━━━━━━━━━"
            chat_id = message.chat.id
            bot.send_message(chat_id, formatted_text)
            print( f"bot mesajı: {formatted_text}")
            bot.send_message(message.chat.id, "👍sorgu başaıiyla sonuçlandı👍")
        else:
            bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\nTC pro bilgileri bulunamadı.\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥doğru girdiğinize emin olun\n┃\n┃➥örnek: /tcpro 11111111111\n╰━━━━━━━━━━━━━━━━━━")
    else:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC pro bilgileri alınamadı.\n╰━━━━━━━━━━━━━━━━━━")


@bot.message_handler(commands=["aile"])
def aile(message):
    parts = message.text.split()
    if len(parts) == 1:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥TC kimlik numarası girmek gereklidir.\n"
            "┃\n"
            "┃➥Lütfen /aile komutunu kullanarak TC\n"
            "┃kimlik numarasını girin.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Örnek: /aile 11111111111\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    tc_number = parts[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")

    try:
        response = requests.get(f'http://172.208.52.218/api/legaliapi/aile.php?tc={tc_number}')
        response.raise_for_status()
    except requests.RequestException:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥aile bilgileri alınamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    data = response.json()
    if data.get('success'):
        formatted_text = ""
        for member in data['data']:
            formatted_text += (
                f"╭━━━━━━━━━━━━━━━━━━\n"
                f"┃➥Adı: {member.get('ADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Soyadı: {member.get('SOYADI', 'Bilgi bulunamadı')}\n"
                f"┃➥TC Kimlik Numarası: {member.get('TC', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Tarihi: {member.get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Yeri: {member.get('NUFUSIL', 'Bilgi bulunamadı')} / {member.get('NUFUSILCE', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne Adı: {member.get('ANNEADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne TC Kimlik Numarası: {member.get('ANNETC', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba Adı: {member.get('BABAADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba TC Kimlik Numarası: {member.get('BABATC', 'Bilgi bulunamadı')}\n"
                f"┃➥Uyruk: {member.get('UYRUK', 'Bilgi bulunamadı')}\n"
                f"┃➥Yakınlık: {member.get('Yakınlık', 'Bilgi bulunamadı')}\n"
                f"╰━━━━━━━━━━━━━━━━━━\n"
            )

        max_message_length = 4096
        for i in range(0, len(formatted_text), max_message_length):
            bot.send_message(message.chat.id, formatted_text[i:i + max_message_length])
            time.sleep(4)
            print( f"bot mesajı: {formatted_text}")

        bot.send_message(message.chat.id, "👍 Sorgu başarıyla sonuçlandı 👍")
    else:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃aile bilgileri bulunamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Doğru girdiğinize emin olun\n"
            "┃\n"
            "┃➥Örnek: /aile 11111111111\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )


@bot.message_handler(commands=["ailepro"])
def ailepro(message):
    parts = message.text.split()
    if len(parts) == 1:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥TC kimlik numarası girmek gereklidir.\n"
            "┃\n"
            "┃➥Lütfen /ailepro komutunu kullanarak TC\n"
            "┃kimlik numarasını girin.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Örnek: /ailepro 11111111111\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    tc_number = parts[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")

    try:
        response = requests.get(f'http://172.208.52.218/api/legaliapi/ailepro.php?tc={tc_number}')
        response.raise_for_status()
    except requests.RequestException:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥ailepro bilgileri alınamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    data = response.json()
    if data.get('success'):
        formatted_text = ""
        for family_group in data['data']:
            for member in family_group:
                formatted_text += (
                    f"╭━━━━━━━━━━━━━━━━━━\n"
                    f"┃➥Adı: {member.get('ADI', 'Bilgi bulunamadı')}\n"
                    f"┃➥Soyadı: {member.get('SOYADI', 'Bilgi bulunamadı')}\n"
                    f"┃➥TC Kimlik Numarası: {member.get('TC', 'Bilgi bulunamadı')}\n"
                    f"┃➥Doğum Tarihi: {member.get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n"
                    f"┃➥Doğum Yeri: {member.get('NUFUSIL', 'Bilgi bulunamadı')} / {member.get('NUFUSILCE', 'Bilgi bulunamadı')}\n"
                    f"┃➥Anne Adı: {member.get('ANNEADI', 'Bilgi bulunamadı')}\n"
                    f"┃➥Anne TC Kimlik Numarası: {member.get('ANNETC', 'Bilgi bulunamadı')}\n"
                    f"┃➥Baba Adı: {member.get('BABAADI', 'Bilgi bulunamadı')}\n"
                    f"┃➥Baba TC Kimlik Numarası: {member.get('BABATC', 'Bilgi bulunamadı')}\n"
                    f"┃➥Uyruk: {member.get('UYRUK', 'Bilgi bulunamadı')}\n"
                    f"┃➥Yakınlık: {member.get('Yakınlık', 'Bilgi bulunamadı')}\n"
                    f"┃➥GSM: {', '.join(member.get('gsm', ['Bilgi bulunamadı']))}\n"
                    f"╰━━━━━━━━━━━━━━━━━━\n"
                )

        max_message_length = 4096
        for i in range(0, len(formatted_text), max_message_length):
            bot.send_message(message.chat.id, formatted_text[i:i + max_message_length])
            time.sleep(4)
            print( f"bot mesajı: {formatted_text}")

        bot.send_message(message.chat.id, "👍 Sorgu başarıyla sonuçlandı 👍")
    else:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃aile pro bilgileri bulunamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Doğru girdiğinize emin olun\n"
            "┃\n"
            "┃➥Örnek: /ailepro 11111111111\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )


@bot.message_handler(commands=["adsoyad"])
def adsoyad(message):
    parts = message.text.split()
    if len(parts) < 3:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Ad ve soyad girmek gereklidir. Lütfen \n"
            "┃/adsoyad komutunu kullanarak ad ve\n"
            "┃soyadını girin.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥ Örneğin: /adsoyad Ali Veli\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    ad, soyad = parts[1], parts[2]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")

    try:
        response = requests.get(f'http://172.208.52.218/api/legaliapi/adsoyad.php?ad={ad}&soyad={soyad}')
        response.raise_for_status()
    except requests.RequestException:
        bot.send_message(
            message.chat.id, 
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥adsoyad bilgileri alınamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    data = response.json()
    if data.get('status') == 'success' and data.get('data'):
        message_text = ""
        for person in data['data']:
            formatted_text = (
                f"╭━━━━━━━━━━━━━━━━━━\n"
                f"┃➥Adı: {person.get('ADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Soyadı: {person.get('SOYADI', 'Bilgi bulunamadı')}\n"
                f"┃➥TC Kimlik Numarası: {person.get('TC', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Tarihi: {person.get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Yeri: {person.get('NUFUSIL', 'Bilgi bulunamadı')} / {person.get('NUFUSILCE', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne Adı: {person.get('ANNEADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne TC Kimlik Numarası: {person.get('ANNETC', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba Adı: {person.get('BABAADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba TC Kimlik Numarası: {person.get('BABATC', 'Bilgi bulunamadı')}\n"
                f"╰━━━━━━━━━━━━━━━━━━\n"
            )
            message_text += formatted_text

        # Mesaj uzunluğunu kontrol et ve gerekirse böl
        max_message_length = 4096
        for i in range(0, len(message_text), max_message_length):
            bot.send_message(message.chat.id, message_text[i:i + max_message_length])
            time.sleep(4)
            print( f"bot mesajı: {formatted_text}")

        bot.send_message(message.chat.id, "👍 Sorgu başarıyla sonuçlandı 👍")
    else:
        bot.send_message(
            message.chat.id, 
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃adsoyad bilgileri bulunamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Doğru girdiğinize emin olun\n"
            "┃\n"
            "┃➥Örnek: /adsoyad Ali Veli\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )


@bot.message_handler(commands=["adsoyadililce"])
def adsoyadil(message):
    parts = message.text.split()
    if len(parts) < 5:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Ad, soyad, il ve ilçe bilgilerini girmek\n"
            "┃gereklidir.\n"
            "┃Lütfen /adsoyadililce komutunu kullanarak\n"
            "┃ad, soyad, il ve ilçe bilgilerini girin.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Örneğin: /adsoyadililce Metin Kara\n"
            "┃İstanbul Ümraniye\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    ad, soyad, il, ilce = parts[1], parts[2], parts[3], parts[4]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")

    try:
        response = requests.get(f'http://172.208.52.218/api/legaliapi/adsoyadil.php?ad={ad}&soyad={soyad}&il={il}&ilce={ilce}')
        response.raise_for_status()
    except requests.RequestException:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥adsoyadililce bilgileri alınamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    data = response.json()
    if data.get('status') == 'success' and data.get('data'):
        message_text = ""
        for person in data['data']:
            formatted_text = (
                f"╭━━━━━━━━━━━━━━━━━━\n"
                f"┃➥Adı: {person.get('ADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Soyadı: {person.get('SOYADI', 'Bilgi bulunamadı')}\n"
                f"┃➥TC Kimlik Numarası: {person.get('TC', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Tarihi: {person.get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Yeri: {person.get('NUFUSIL', 'Bilgi bulunamadı')} / {person.get('NUFUSILCE', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne Adı: {person.get('ANNEADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne TC Kimlik Numarası: {person.get('ANNETC', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba Adı: {person.get('BABAADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba TC Kimlik Numarası: {person.get('BABATC', 'Bilgi bulunamadı')}\n"
                f"╰━━━━━━━━━━━━━━━━━━\n"
            )
            message_text += formatted_text

        max_message_length = 4096
        for i in range(0, len(message_text), max_message_length):
            bot.send_message(message.chat.id, message_text[i:i + max_message_length])
            time.sleep(4)
            print( f"bot mesajı: {formatted_text}")

        bot.send_message(message.chat.id, "👍 Sorgu başarıyla sonuçlandı 👍")
    else:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃adsoyadililce bilgileri bulunamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Doğru girdiğinize emin olun\n"
            "┃\n"
            "┃➥Örnek: /adsoyadililce Ali Veli Konya Merkez\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )


@bot.message_handler(commands=["adsoyadil"])
def adsoyadil(message):
    parts = message.text.split()
    if len(parts) < 4:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Ad, soyad ve il bilgilerini girmek\n"
            "┃gereklidir.\n"
            "┃➥Lütfen /adsoyadil komutunu kullanarak \n"
            "┃ad, soyad ve il bilgilerini girin.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥ Örnek: /adsoyadil metin kara \n"
            "┃İstanbul\n"
            "╰━━━━━━━━━━━━━━━━━━\n"
        )
        return

    ad = parts[1]
    soyad = parts[2]
    il = parts[3]

    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")

    try:
        response = requests.get(f'http://172.208.52.218/api/legaliapi/adsoyadil.php?ad={ad}&soyad={soyad}&il={il}')
        response.raise_for_status()
    except requests.RequestException:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥adsoyadil bilgileri alınamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )
        return

    data = response.json()
    if data.get('status') == 'success':
        formatted_text = ""
        for person in data['data']:
            formatted_text += (
                f"╭━━━━━━━━━━━━━━━━━━\n"
                f"┃➥Adı: {person.get('ADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Soyadı: {person.get('SOYADI', 'Bilgi bulunamadı')}\n"
                f"┃➥TC Kimlik Numarası: {person.get('TC', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Tarihi: {person.get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n"
                f"┃➥Doğum Yeri: {person.get('NUFUSIL', 'Bilgi bulunamadı')} / {person.get('NUFUSILCE', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne Adı: {person.get('ANNEADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Anne TC Kimlik Numarası: {person.get('ANNETC', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba Adı: {person.get('BABAADI', 'Bilgi bulunamadı')}\n"
                f"┃➥Baba TC Kimlik Numarası: {person.get('BABATC', 'Bilgi bulunamadı')}\n"
                f"╰━━━━━━━━━━━━━━━━━━\n"
            )

        max_message_length = 4096
        for i in range(0, len(formatted_text), max_message_length):
            bot.send_message(message.chat.id, formatted_text[i:i + max_message_length])
            time.sleep(4)
            print( f"bot mesajı: {formatted_text}")

        bot.send_message(message.chat.id, "👍 Sorgu başarıyla sonuçlandı 👍")
    else:
        bot.send_message(
            message.chat.id,
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃adsoyadil bilgileri bulunamadı.\n"
            "╰━━━━━━━━━━━━━━━━━━\n\n"
            "╭━━━━━━━━━━━━━━━━━━\n"
            "┃➥Doğru girdiğinize emin olun\n"
            "┃\n"
            "┃➥Örnek: /adsoyadil Ali Veli Konya\n"
            "╰━━━━━━━━━━━━━━━━━━"
        )

@bot.message_handler(commands=["gsmdentc"])
def gsmdentc(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥Telefon numarası girmek gereklidir.\n┃➥ Lütfen /gsmdentc komutunu kullanarak \n┃telefon numarasını girin\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥örnek: 5055555555\n╰━━━━━━━━━━━━━━━━━━")
        return

    gsm_number = message.text.split(' ')[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")
    response = requests.get(f'http://172.208.52.218/api/legaliapi/gsmdetay.php?gsm={gsm_number}')
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            formatted_text = f"╭━━━━━━━━━━━━━━━━━━\n┃➥TC Kimlik Numarası: {data['Data'].get('TC', 'Bilgi bulunamadı')}\n┃➥Adı: {data['Data'].get('ADI', 'Bilgi bulunamadı')}\n┃➥Soyadı: {data['Data'].get('SOYADI', 'Bilgi bulunamadı')}\n┃➥Doğum Tarihi: {data['Data'].get('DOGUMTARIHI', 'Bilgi bulunamadı')}\n┃➥Doğum Yeri: {data['Data'].get('NUFUSIL', 'Bilgi bulunamadı')} / {data['Data'].get('NUFUSILCE', 'Bilgi bulunamadı')}\n┃➥Anne Adı: {data['Data'].get('ANNEADI', 'Bilgi bulunamadı')}\n┃➥Anne TC Kimlik Numarası: \n┃{data['Data'].get('ANNETC', 'Bilgi bulunamadı')}\n┃➥Baba Adı: {data['Data'].get('BABAADI', 'Bilgi bulunamadı')}\n┃➥Baba TC Kimlik Numarası: \n┃{data['Data'].get('BABATC', 'Bilgi bulunamadı')}\n┃➥Uyruk: {data['Data'].get('UYRUK', 'Bilgi bulunamadı')}\n╰━━━━━━━━━━━━━━━━━━\n"
            bot.send_message(message.chat.id, formatted_text)
            print( f"bot mesajı: {formatted_text}")
            bot.send_message(message.chat.id, "👍sorgu başaıiyla sonuçlandı👍")
        else:
            bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\ngsmdentc bilgileri bulunamadı.\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥doğru girdiğinize emin olun\n┃\n┃➥örnek: /gsmdentc 5055555555\n╰━━━━━━━━━━━━━━━━━━")
    else:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥gsmdentc bilgileri alınamadı.\n╰━━━━━━━━━━━━━━━━━━")

@bot.message_handler(commands=["tcdengsm"])
def tcdengsm(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC kimlik numarası girmek gereklidir. \n┃➥Lütfen /tcdengsm komutunu kullanarak\n┃ TC kimlik numarasını girin.\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥örnek: /tcdengsm 11111111111\n╰━━━━━━━━━━━━━━━━━━")
        return

    tc_number = message.text.split(' ')[1]
    print(f"Kullanıcı mesajı: {message.text} ")
    bot.send_message(message.chat.id, "Sorgu alındı, lütfen bekleyin. İşlem süresi biraz uzun olabilir.")
    response = requests.get(f'http://172.208.52.218/api/legaliapi/tcgsm.php?tc={tc_number}')
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            formatted_text = ""
            for entry in data['data']:
                if entry.get('id') and entry.get('TC') and entry.get('GSM'):  # Boş olmayan verileri kontrol edin
                    formatted_text += f"╭━━━━━━━━━━━━━━━━━━\n┃➥ID: {entry['id']}\n┃➥TC Kimlik Numarası: \n┃{entry['TC']}\n┃➥GSM: {entry['GSM']}\n╰━━━━━━━━━━━━━━━━━━\n"
            if formatted_text:  # Eğer formatlı metin boş değilse gönder
                bot.send_message(message.chat.id, formatted_text)
                print( f"bot mesajı: {formatted_text}")
                bot.send_message(message.chat.id, "👍sorgu başaıiyla sonuçlandı👍")
            else:
                bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\ntcdengsm bilgileri bulunamadı.\n╰━━━━━━━━━━━━━━━━━━\n\n╭━━━━━━━━━━━━━━━━━━\n┃➥doğru girdiğinize emin olun\n┃\n┃➥örnek: /tcdengsm 11111111111\n╰━━━━━━━━━━━━━━━━━━.")
        else:
            bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥tcdengsm bilgileri alınamadı.\n╰━━━━━━━━━━━━━━━━━━")
    else:
        bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━━━━━━\n┃➥TC kimlik numarasına ilişkin GSM bilgileri alınamadı.\n╰━━━━━━━━━━━━━━━━━━")

print('bot çalışıyor')

import requests,random
logo='''
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤🔥⣀⠀⠀⢸⣷⡄⠀🔥⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
TELEGRAM | @kingmodturkiye
'''
colors = ["\033[91m", "\033[94m", "\033[92m", "\033[93m", "\033[38;5;208m", "\033[95m", "\033[97m", "\033[37m"]
random_color = random.choice(colors)
print(random_color+logo)

def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Hata oluştu: {e}")
            time.sleep(15)  # Bir süre bekleyip tekrar dene

if __name__ == '__main__':
    main()
# Botun çalıştırılması
bot.polling()
