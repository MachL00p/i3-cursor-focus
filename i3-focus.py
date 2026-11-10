import i3ipc.aio
import subprocess

i3 = i3ipc.Connection()

def move_cursor(current_focused):
    if current_focused is None:
        return
    else:
        x = current_focused.rect.x + current_focused.rect.width // 2
        y = current_focused.rect.y + current_focused.rect.height // 2

        subprocess.run( ["xdotool", "mousemove", str(x), str(y)], stdout = subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def on_focus(conn, event):
    current_focused = i3.get_tree().find_focused()
    focused_workspace = current_focused.workspace()
    if current_focused.floating in ["auto_off","user_off"]:
        if len(focused_workspace.floating_nodes) == 0:
            move_cursor(current_focused)
    else:
        return

i3.on("window::focus", on_focus)
i3.on("window::move", on_focus)

i3.main()
