import flet as ft
import subprocess
import pickle


def lang_code_checker(lang):
        if lang == "Español":
            code = "es"
        elif lang == "English":
            code = "en"
        elif lang == "Português":
            code = "pt"
        else:
            code = "es"
        return code

def main(page: ft.Page):

    # Page Propierties -----------------------

    page.title = "Translate Everthing - Language Selector"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximized = True
    page.window.icon = "icon.ico"
    
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "assets/images/background-2.png",
            fit = ft.ImageFit.COVER,
            opacity = 0.7
            )
        )
    

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
                ft.dropdown.Option(key="es", text="Español"),
                ft.dropdown.Option(key="en", text="English"),
                ft.dropdown.Option(key="pt", text="Português"),
            ],
            autofocus=True,
            width=300,
            bgcolor=ft.colors.WHITE
        )

    

    def change_page(e):
        if selector.value != None:
            with open("./assets/variables.pkl", "wb") as f:
                pickle.dump(lang_code_checker(selector.value), f)
            page.window.close()
            subprocess.Popen(["python", "./main.py"])

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