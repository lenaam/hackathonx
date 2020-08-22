import requests
import datetime




class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1342801484:AAFPiteYIxAoeD1gMrzbR26vQQiu-L4vZwU'  # Token of bot
ewaan_bot = BotHandler(token)  # bot's name

def start( bot , update):
    ewaan_bot.send_message(chat_id = update.Message.chat_id , text= "اهلا انا عوان و كيف اقدر اساعد")

def main():
    new_offset = 0
    print('اهلا انا عوان و كيف اقدر اساعدك')
# prints welcoming msg if there are new mgs from user
    while True:
        all_updates = ewaan_bot.get_updates(new_offset)
# msg classification
        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'اهلا':
                    ewaan_bot.send_message(first_chat_id, 'اهلا انا عوان، كيف اقدر اساعدك  ' + first_chat_name)
                    new_offset = first_update_id + 1
                else:
                    ewaan_bot.send_message(first_chat_id, 'كيف اقدر اساعدك ' + first_chat_name)
                    new_offset = first_update_id + 1

                if first_chat_text == 'واجب':
                    ewaan_bot.send_message(first_chat_id, 'تفضل هذا الفيديو يساعدك في طريقة حل و رفع الواجب '
                                                          'https://www.youtube.com/watch?v=vg10oH3JXO0 ')
                elif first_chat_text ==  'الواجب':
                   ewaan_bot.send_message(first_chat_id, 'تفضل هذا الفيديو يساعدك في طريقة حل و رفع الواجب '
                                                         'https://www.youtube.com/watch?v=vg10oH3JXO0 ' )
                   new_offset = first_update_id + 1
                elif first_chat_text == 'حل الواجب':
                    ewaan_bot.send_message(first_chat_id, 'تفضل هذا الفيديو يساعدك في طريقة حل و رفع الواجب '
                                                          'https://www.youtube.com/watch?v=vg10oH3JXO0 ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'بوابة عين':
                    ewaan_bot.send_message(first_chat_id, 'تفضل دليل المستخدم لبوابة عين '
                                                          'https://ien.edu.sa/Content/%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D8%AE%D8%AF%D9%85%20%D9%84%D8%A8%D9%88%D8%A7%D8%A8%D8%A9%20%D8%B9%D9%8A%D9%86.pdf')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'منصات التعليم عن بعد':
                    ewaan_bot.send_message(first_chat_id, 'منصات التعليم عن بعد هي: '
                                                          '١-منظومة التعليم الموحدة '
                                                          '  https://vschool.sa/'
                                                           "\n"
                                                          '٢-عين بوابة التعليم الوطنية'
                                                          'https://ien.edu.sa/')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'قناة عين':
                    ewaan_bot.send_message(first_chat_id, 'شبكة قنوات (عين) الفضائية التابعة لوزارة التعليم السعودية | 20 قناة تعليمية | تردد: عرب سات 12437 عمودي '
                                                          'https://youtu.be/Dnz2SHfh4z0'
                                                         )
                    new_offset = first_update_id + 1





if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()