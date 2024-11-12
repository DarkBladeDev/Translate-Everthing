import flet as ft
from deep_translator import GoogleTranslator
import pickle
import os
import subprocess


def main(page: ft.Page):

    # Page Propierties -----------------------

    page.title = "Translate Everthing - Main app"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.bgcolor = ft.colors.TRANSPARENT
    page.window.maximized = True
    page.window.icon = "icon.ico"

    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "./assets/images/background-1.jpg",
            fit = ft.ImageFit.COVER,
            opacity = 0.7
            )
        )
    

    # -----------------------------------------

    # Lang Labels -----------------------------

    lang_code = "es"

    lang_labels = {
        'lang_code' : lang_code,
        'text_input': "Ingrese el texto a traducir",
        'translate_options_label': "Idioma",
        'translate_options_hint': "Selecciona el lenguaje al que traducir",
        'translate_button_text' : "Traducir",
        'language_icon_tooltip' : "Cambiar idioma",
        'exit_icon_tooltip' : "Cerrar aplicación",
    }


    # Cargar el código de idioma desde pickle ---------------------
    pickle_path = "./assets/variables.pkl"
    if os.path.exists(pickle_path):
        try:
            with open(pickle_path, "rb") as f:
                lang_code = pickle.load(f)
                print(f"LOG >> Lenguaje cargado: {lang_code}")  # Para depuración
        except Exception as e:
            print(f"LOG >> Error al cargar el archivo pickle: {e}")
    else:
        print(f"LOG >> El archivo {pickle_path} no existe.")

    # -----------------------------------------

    # Code ------------------------------------

    def change_page(e):
        page.window.close()
        subprocess.Popen(["python", "./lang_selector.py"])

    translated_text = ""

    translator = GoogleTranslator(source='auto', target=lang_code)

    text_input = ft.TextField(label=translator.translate(lang_labels["text_input"]))

    text_output = ft.Text(f"{translator.translate("Resultado")}: {translated_text}", size=20)


    def translate(e):
        global translated_text

        if text_input.value != None:
            translated_text = GoogleTranslator(source='auto', target=translate_options.value).translate(text=text_input.value)
            text_output.value = f"{translator.translate("Resultado")}: {translated_text}"

        print("LOG >> Input: ", text_input.value)
        print("LOG >> Output: ", translated_text)

        page.update()
        

    translate_button = ft.ElevatedButton(text=translator.translate(lang_labels["translate_button_text"]), on_click=translate)
    
    def debug_key(e):
        print(f"LOG >> key: {translate_options.key} text: {translate_options.value}")

    translate_options = ft.Dropdown(
            label=translator.translate(lang_labels["translate_options_label"]),
            hint_text=translator.translate(lang_labels["translate_options_label"]),
            options=[
                ft.dropdown.Option(key="es", text="Español"),
                ft.dropdown.Option(key="en", text="English"),
                ft.dropdown.Option(key="pt", text="Português"),
            ],
            #on_change=debug_key,
            autofocus=True,
        )
    


    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TRANSLATE),
        leading_width=40,
        title=ft.Text("Translate Everthing", color=ft.colors.GREEN_200),
        center_title=False,
        bgcolor=ft.colors.LIGHT_BLUE_800,
        actions=[
            ft.IconButton(ft.icons.LANGUAGE, hover_color=ft.colors.GREEN, tooltip=translator.translate(lang_labels["language_icon_tooltip"]), on_click=lambda e: change_page(e)),
            ft.IconButton(ft.icons.EXIT_TO_APP, hover_color=ft.colors.RED, tooltip=translator.translate(lang_labels["exit_icon_tooltip"]), on_click=lambda e: page.window.close()),
            ],
        )


    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                text_input,
                translate_options
            ]),
            translate_button,
            text_output,
        ])
    )
    # -----------------------------------------

ft.app(main)