import os
import shutil
import time
from tqdm import tqdm
from dashboards.models import User, Item
from model_bakery import baker


role_names = ["Actor", "Producer", "Screenwriter"]


def clear_migrations() -> None:
    """Удаляет папки migrations и создает новые с файлом __init__.py."""
    dirs_path = ["./dashboards/migrations"]
    for dir_path in dirs_path:
        try:
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))

        os.mkdir(dir_path)
        with open(dir_path + "/__init__.py", "w"):
            pass  # noqa


def remove_sqlite3() -> None:
    """Удаляет и создает новый файл db.sqlite3."""
    try:
        os.remove("./config/db.sqlite3")
    except FileNotFoundError:
        pass
    finally:
        with open("./config/db.sqlite3", "w"):
            pass  # noqa


def create_superuser() -> None:
    """Создание супер пользователя."""
    user = User.objects.create(email="mail@example.com")
    user.set_password("password")
    user.is_superuser = True
    user.is_staff = True
    user.save()


def makemigrations_migrate() -> None:
    """Начальные миграции."""
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")


def gen_users(count: int) -> None:
    print(count)
    """Generate users"""
    pbar = tqdm(total=2, initial=1, desc="gen_users:build_batch")
    baker.make(
        "dashboards.User",
        # first_name=baker.seq("FirstName: "),
        # last_name=baker.seq("LastName: "),
        _quantity=count,
        _bulk_create=True,
    )
    pbar.update()
    pbar.close()


def gen_items(count: int) -> None:
    """Generate items"""
    pbar = tqdm(total=2, initial=1, desc="gen_items:build_batch")
    baker.make(
        "dashboards.Item",
        _quantity=count,
        _bulk_create=True,
    )
    pbar.update()
    pbar.close()


def start_gen(users=1000, items=10000, clear=True, superuser=True) -> None:
    if clear:
        remove_sqlite3()
        clear_migrations()
        makemigrations_migrate()
    if superuser:
        create_superuser()

    start_time = time.time()
    # gen_users(users)
    gen_items(items)

    print("--- %s seconds --- create objects" % (time.time() - start_time))
    print("--- superuser: mail@example.com, password: password ---")
