import keyboard as kb
import pygetwindow as gw
import time
import mouse as ms

chromePage = "supabase"
openPrograms = ["Visual Studio Code", "Google Chrome"]


def work_mode():

    minimizePrograms = gw.getAllTitles()

    # minimize all programs in list
    for program in minimizePrograms:
        if program == "":
            continue
        apps: list[gw.Win32Window] = gw.getWindowsWithTitle(program)
        for app in apps:

            if any(p in app.title for p in openPrograms):
                break

            app.minimize()

    # open all programs in list
    for program in openPrograms:
        apps: list[gw.Win32Window] = gw.getWindowsWithTitle(program)
        for app in apps:
            kb.send("alt")
            app.activate()
            app.maximize()

            if program == "Google Chrome":
                kb.send("ctrl + shift + a")
                time.sleep(0.15)
                kb.write(chromePage)
                time.sleep(0.15)
                kb.send("enter")


def mouse_check():
    if ms.is_pressed("left"):
        work_mode()


ms.on_right_click(mouse_check)
kb.wait("esc")
