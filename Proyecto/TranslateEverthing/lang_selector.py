import flet as ft
import subprocess
import pickle


def main(page: ft.Page):

    # Page Propierties -----------------------

    page.title = "Translate Everthing - Language Selector"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # -----------------------------------------
    
    # Snackbars -------------------------------
    
    error_no_lang_selected = ft.SnackBar(
        content= ft.Text(
            value= "Please, select a valid language",
            color= ft.colors.RED,
            bgcolor = ft.colors.GREY_100,
                        )
    )

    # -----------------------------------------

    # Code ------------------------------------
    selector = ft.Dropdown(
            label="Language",
            hint_text="Choose your language",
            options=[
                ft.dropdown.Option("Español", data="es"),
                ft.dropdown.Option("English", data="en"),
            ],
            autofocus=True,
        )

    def lang_code_checker(lang):
        if lang == "Español":
            code = "es"
        elif lang == "English":
            code = "en"
        else:
            code = "es"
        return code

    def change_page(e):
        if selector.value == "Español" or selector.value == "English":
            with open("TranslateEverthing/assets/variables.pkl", "wb") as f:
                pickle.dump({"code": lang_code_checker(selector.value)}, f)
            page.window.close()
            subprocess.Popen(["python", "TranslateEverthing/main.py"])

        else:
            page.open(error_no_lang_selected)


    finish_button = ft.ElevatedButton(
        text="Seleccionar",
        on_click= change_page
    )


    page.add(
        ft.Column([
            selector,
            finish_button,
        ]),
        error_no_lang_selected
    )

    # -----------------------------------------

ft.app(main)