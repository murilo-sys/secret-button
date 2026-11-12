import keyboard as kb
import pygetwindow as gw

minimizePrograms = ["Google Chrome"]
openPrograms = ["Visual Studio Code"]


def work_mode():
    print(gw.getAllTitles())
    # minimize all programs in list
    for program in minimizePrograms:
        apps: list[gw.Win32Window] = gw.getWindowsWithTitle(program)
        for app in apps:
            app.minimize()
    # open all programs in list
    for program in openPrograms:
        apps: list[gw.Win32Window] = gw.getWindowsWithTitle(program)
        for app in apps:
            app.restore()
            app.activate()
            app.maximize()


work_mode()
