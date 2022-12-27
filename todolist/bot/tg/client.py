import requests

from bot.tg.dc import GetUpdatesResponse, SendMessageResponse, get_updates_schema, send_message_schema


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str) -> str:
        """
        URL метод для запроса к telegram боту

        Args:
            method: какой запрос будет отправлен боту

        Returns:
            str
        """
        return f"https://api.telegram.org/bot{self.token}/{method}"

    # def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
    #     """
    #     Получения входящих обновлений от пользователя.
    #     Args:
    #         offset: int
    #         timeout: int
    #     Returns:
    #         GetUpdatesResponse
    #     """
    #     response = requests.get(self.get_url(f"getUpdates?offset={offset}&timeout={timeout}&"
    #                                          f"allowed_updates=['update_id','message']"))
    #     json_data = response.json()
    #     print(json_data)
    #     result = get_updates_schema().load(json_data)
    #
    #     return result

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        url = self.get_url('getUpdates')
        response = requests.get(url, params={'offset': offset, 'timeout': timeout})
        print(response.json())
        return get_updates_schema.load(response.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        """
        Отправление сообщения пользователю от бота.

        Args:
            chat_id: int
            text: int

        Returns:
            SendMessageResponse
        """
        response = requests.get(self.get_url(f"sendMessage?chat_id={chat_id}&text={text}"))
        json_data = response.json()
        result = send_message_schema().load(json_data)
        print(response.json())

        return result
