import subprocess
import pickle


import flet as ft



def selector(page: ft.Page):

    #from APP.MODULES.DB_Manager import check_creds

    # PROPIEDADES DE LA PÁGINA ------------------------------------------
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximized = True

    page.title = "Translate Everthing - Login"
    page.bgcolor = ft.colors.TRANSPARENT

    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "TranslateEverthing/assets/images/background_img.png",
            fit = ft.ImageFit.COVER,
            opacity = 0.7
            )
        )
    
    # -------------------------------------------------------------------


    # LOGIN PANEL -------------------------------------------------------

    global login_panel
    global error_no_account

    complete_login = ft.ElevatedButton(icon=ft.icons.LOGIN, text="Iniciar sesión", on_click= lambda _: login_click())
    username_input = ft.TextField(label="Usuario o Correo", width=300, border_color=ft.colors.WHITE, bgcolor=ft.colors.GREY)
    password_input = ft.TextField(label="Contraseña", width=300, border_color=ft.colors.WHITE, bgcolor=ft.colors.GREY, password=True, can_reveal_password=True)

    
    login_panel = ft.Column(
        controls=[
            username_input,
            password_input,
            complete_login,
        ]
    )


    # --------------- SNACKBARS ----------------- #
    
    error_no_account = ft.SnackBar(
        content= ft.Text(
            value= "Credenciales incorrectas o inexistentes",
            color= ft.colors.RED,
            bgcolor = ft.colors.GREY,
                        )
    )

    # ---------------------------------------------------#


    def login_click():
        page.window.close()
        subprocess.Popen(["python", "TranslateEverthing/lang_selector.py"])

    # -------------------------------------------------------------------


    page.add(
        login_panel,
        error_no_account,
    )

    return page


def add_page(page):
    page.add(
    login_panel,
    error_no_account,
    )
    return page

    # -----------------------------------------------------------------------
    
        




if __name__ == '__main__':
    ft.app(
        target=selector,
        port=8550)
