import requests
import json

def lambda_handler(event, context):
        user = "Jahaziel"
        forecastReports = json.loads(json.dumps(event))
        text = "Hola " + user + " este es el reporte diario del clima:";
    
        for report in forecastReports:
            text += "\n" + str(report["date"]) + " - " + str(report["temperature"]);

        telegramBot = "1651993391:AAH_CG_bSdXgzsUiB4QSY7E1-7pr4Ndlrz8"
        chatId = "1498424230";
        params = {'chat_id': chatId, 'text': text}
        telegramResponse = requests.post('https://api.telegram.org/bot1651993391:AAH_CG_bSdXgzsUiB4QSY7E1-7pr4Ndlrz8/sendMessage',params=params)
        return telegramResponse.json()

    
    