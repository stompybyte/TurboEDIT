from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
import os

# ---------- НАСТРОЙКИ ----------
FONT_FILE = "PressStart2P-Regular.ttf"
BG_COLOR = (0.0, 0.2, 0.8, 1)
TEXT_COLOR = (1, 1, 1, 1)
FONT_SIZE = 14
WINDOW_SIZE = (1024, 768)
# --------------------------------


class TurboEDITApp(App):
    title = "TurboEDIT"

    def build(self):
        # ОКНО
        Window.title = "TurboEDIT"
        Window.size = WINDOW_SIZE
        Window.clearcolor = BG_COLOR

        # ШРИФТ
        base_path = os.path.dirname(os.path.abspath(__file__))
        resource_add_path(base_path)
        LabelBase.register(name="PS2P", fn_regular=FONT_FILE)

        self.editor = TextInput(
            font_name="PS2P",
            font_size=FONT_SIZE,
            foreground_color=TEXT_COLOR,
            background_color=BG_COLOR,
            cursor_color=TEXT_COLOR,
            selection_color=(1, 1, 1, 0.3),
            multiline=True,
            padding=(12, 12),
            use_bubble=False,
            use_handles=False,
            text=""
        )

        root = BoxLayout()
        root.add_widget(self.editor)

        Window.bind(on_key_down=self.on_key_down)
        return root

    # ---------- HOTKEYS ----------
    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        # F1 — OPEN
        if key == 282:
            self.open_file()
            return True

        # F2 — SAVE
        if key == 283:
            self.save_file()
            return True

        # CTRL комбинации
        if 'ctrl' in modifiers:
            if key == ord('c'):
                self.copy()
                return True
            if key == ord('v'):
                self.paste()
                return True
            if key == ord('x'):
                self.cut()
                return True

        return False

    # ---------- CLIPBOARD ----------
    def copy(self):
        if self.editor.selection_text:
            Clipboard.copy(self.editor.selection_text)

    def cut(self):
        if self.editor.selection_text:
            Clipboard.copy(self.editor.selection_text)
            self.editor.delete_selection()

    def paste(self):
        text = Clipboard.paste()
        if text:
            self.editor.insert_text(text)

    # ---------- OPEN ----------
    def open_file(self):
        chooser = FileChooserListView(path=os.getcwd())
        btn = Button(text="OPEN", size_hint_y=None, height=40)

        box = BoxLayout(orientation="vertical")
        box.add_widget(chooser)
        box.add_widget(btn)

        popup = Popup(
            title="OPEN FILE",
            content=box,
            size_hint=(0.9, 0.9),
            background_color=BG_COLOR
        )

        def do_open(instance):
            if chooser.selection:
                try:
                    with open(chooser.selection[0], "r", encoding="utf-8") as f:
                        self.editor.text = f.read()
                except Exception as e:
                    self.editor.text = f"ERROR OPENING FILE:\n{e}"
                popup.dismiss()

        btn.bind(on_release=do_open)
        popup.open()

    # ---------- SAVE ----------
    def save_file(self):
        chooser = FileChooserListView(path=os.getcwd())
        btn = Button(text="SAVE", size_hint_y=None, height=40)

        box = BoxLayout(orientation="vertical")
        box.add_widget(chooser)
        box.add_widget(btn)

        popup = Popup(
            title="SAVE FILE",
            content=box,
            size_hint=(0.9, 0.9),
            background_color=BG_COLOR
        )

        def do_save(instance):
            if chooser.selection:
                try:
                    with open(chooser.selection[0], "w", encoding="utf-8") as f:
                        f.write(self.editor.text)
                except Exception as e:
                    self.editor.text += f"\n\nERROR SAVING FILE:\n{e}"
                popup.dismiss()

        btn.bind(on_release=do_save)
        popup.open()


if __name__ == "__main__":
    TurboEDITApp().run()
