# from unittest.mock import MagicMock
#
# from django.core import mail
#
# from main.tasks import mail_send_9am
#
#
# def test_mail_send_9am(mocker):
#     requests_get_patcher = mocker.patch('requests.get')
#     requests_get_patcher.return_value = MagicMock(
#         text="Mocked Text."
#
#     )
#     emails = ["koka@gmail.com"]
#     mail_send_9am()
#     assert len(mail.outbox) > 0
