* вместо `from django.contrib.auth.models import User` использовать get_user_model() и `AUTH_USER_MODEL`
* PEP8 линтер в vscode
* поля модели должны быть `Quiz` -> `quiz`
* модели в единственном числе: `Results` -> `Result`
* убрать из view пакеты которые не используется (после PEP8 это будет легче сделать)
* Все файлы из CRLF -> LF
* Подтюнить админку (search_fields, filter_list)
* Themes template на bootstrap 5.x
* Register form bootstrap
* вывести через `for` messages в base.html из login.html + добавить ERROR в tags через settings.py
* добавить удаление через `DeleteView`, добавить проверку, что удалять юзер может только свои квизы (через get_queryset).
