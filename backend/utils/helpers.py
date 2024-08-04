import hashlib
import logging
import re
from datetime import datetime
from functools import wraps

from django.core.cache import cache

logger = logging.getLogger(__name__)


def snake_to_camel(snake_str: str) -> str:
    return "".join(
        word.capitalize() if i > 0 else word
        for i, word in enumerate(snake_str.split("_"))
    )


def dict_keys_snake_to_camel(d):
    if not isinstance(d, dict):
        return d

    def process_item(item):
        if isinstance(item, dict):
            return {snake_to_camel(k): process_item(v) for k, v in item.items()}

        if isinstance(item, list):
            return [process_item(i) for i in item]

        return item

    return process_item(d)


def generate_hash(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def clear_html(text: str) -> str:
    return re.sub(r"(<[^>]*>)|(&quot;)", "", text)


def timeit(func):
    def __normalize_path(code) -> str:
        return str(code).split('"')[-2]

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        func_path = __normalize_path(func.__code__)
        logger.info(
            f"Функция {func_path} -> <{func.__name__}> выполнилась за {end - start} секунд"
        )
        return result

    return wrapper


def singleton_task(task_name):
    """
    Singleton decorator for tasks
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            lock_id = f"{task_name}_lock"

            # Добавляем в кеш на 24 часа, иначе кеш может очиститься сам
            got_lock = cache.add(lock_id, "true", timeout=60 * 60 * 24)

            if not got_lock:
                logger.info(f"Task {task_name} is already running")
                return

            logger.info(f"Task {task_name} is starting execution")
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Task {task_name} raised an exception: {e}")
            finally:
                cache.delete(lock_id)

        return wrapper

    return decorator
