from imgui_sdl_wrapper import ImguiSdlWrapper
import imgui

if __name__ == "__main__":
    app = ImguiSdlWrapper("My App", 1280, 720)
    while app.running:
        app.main_loop_begin()
        imgui.show_demo_window()
        app.main_loop_end()
    app.destroy()
