from googletrans import Translator
import flet as ft
import pickle

def main(page: ft.Page):

    # Page Propierties -----------------------

    page.title = "Translate Everthing - Main app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # -----------------------------------------

    # Lang Labels -----------------------------

    with open("TranslateEverthing/assets/variables.pkl", "rb") as f:
        lang_code = pickle.load(f)

    lang_labels = {
        'lang_code' : lang_code["code"],
        'text_input': "Ingrese el texto a traducir",
        'translate_options_label': "Idioma",
        'translate_options_hint': "Selecciona el lenguaje al que traducir"
    }
    
    print("LOG >> ", lang_labels)
    # -----------------------------------------

    # Code ------------------------------------
    
    text_input = ft.TextField(label=lang_labels["text_input"])

    translator = Translator()

    translated_text = ""
    

    def lang_code_checker(lang):
        if lang == "Español":
            code = "es"
        elif lang == "English":
            code = "en"

        return code
    

    def translate(e):
        if text_input.value != None:
            translated_text = translator.translate(text=text_input.value, dest=lang_code_checker(translate_options.value))

        print("LOG >> ", text_input.value)
        print("LOG >> ", translated_text)


    translate_button = ft.ElevatedButton(text="Traducir", on_click=translate)
    
    text_output = ft.Text(f"Resultado: {translated_text}", size=20)

    translate_options = ft.Dropdown(
            label=translator.translate(lang_labels["translate_options_label"], lang_labels["lang_code"]),
            hint_text=translator.translate(lang_labels["translate_options_label"], lang_labels["lang_code"]),
            options=[
                ft.dropdown.Option("Español", data="es"),
                ft.dropdown.Option("English", data="en"),
            ],
            autofocus=True,
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