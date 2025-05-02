### Запуск через докер

``` docker-compose up -d ```

### Для запуска локально

Откорректировать файл .env-sample и сохранить под именем .env

```poetry install ```

```litestar database upgrade head --no-prompt ```

```litestar run ```

### Проверка

Открыть бразузер и перейти по адресу:

```http://localhost:8000/schema/swagger```