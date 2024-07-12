import getpass
import hashlib
import logging

logger = logging.getLogger('password_checker')
symbols = '!@#$%^&*()-+=_'

def input_and_check():
    logger.debug('Начало input_and_check_password')
    password: str = getpass.getpass()

    symbol_counter = 0
    has_uppercase = False
    if not password:
        logger.warning('Вы ввели пустой пароль.')
        return False
    
    try:
        hasher = hashlib.md5()
        logger.warning('Мы успешно создали объект hasher.')
        if len(password) >= 8:    
            for symbol in password:
                if symbol in symbols:
                    symbol_counter += 1
                if symbol.isupper():
                    has_uppercase = True
            if symbol_counter >= 1: 
                print('OK')
            else:
                logger.warning('В пароле должны присутствовать эти символы: {}'.format(symbols))
            if has_uppercase == True:
                print("OK")
            else:
                logger.warning('В пароле должны быть заглавные буквы')
        else:
            logger.warning("Длина пароля должна быть от 8 символов")


        hasher.update(password.encode('latin-1'))
        logger.warning('Обновление объекта hasher.')

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    
    except ValueError as error:
        logger.exception('В пароле должны присутствовать только латинские символы!', exc_info=str(error))

    return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Вы пытаетесь войти в камеру')
    amount = int(input('Сколько попыток вам потребуется?(от 2 до 10): '))
    if amount >= 2 and amount <= 10:
        count_number: int = amount
        logger.info('У вас есть {} попытки'.format(count_number))

        while count_number > 0:
            if input_and_check():
                exit(0)
            count_number -= 1
        logger.error('Пользователь {} раза ввёл не правильный пароль!'.format(amount))
        exit(1)
    else:
        logger.warn('Количество попыток может быть от 2 до 10')
        
    
