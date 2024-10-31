import subprocess
import flet as ft



def login(page: ft.Page):


    # PROPIEDADES DE LA PÁGINA ------------------------------------------
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximized = True

    page.title = "Translate Everthing - Login"
    page.bgcolor = ft.colors.TRANSPARENT

    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "assets/images/background_img.png",
            fit = ft.ImageFit.COVER,
            opacity = 0.7
            )
        )
    
    # -------------------------------------------------------------------

    usuarios = {
        'user': "test",
        'password': "test"
        }

    # LOGIN PANEL -------------------------------------------------------

    global login_panel
    global error_no_account

    complete_login = ft.ElevatedButton(icon=ft.icons.LOGIN, text="Iniciar sesión", on_click= lambda _: login_click())
    username_input = ft.TextField(label="Usuario o Correo", width=300, border_color=ft.colors.WHITE, bgcolor=ft.colors.GREY_600, label_style=ft.TextStyle(color=ft.colors.BLACK))
    password_input = ft.TextField(label="Contraseña", width=300, border_color=ft.colors.WHITE, bgcolor=ft.colors.GREY_600, label_style=ft.TextStyle(color=ft.colors.BLACK), password=True, can_reveal_password=True)

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
        if username_input.value == usuarios["user"] and password_input.value == usuarios["password"]:
            page.window.close()
            subprocess.Popen(["python", "./lang_selector.py"])
        
        else:
            page.open(error_no_account)

    # -------------------------------------------------------------------


    page.add(
        login_panel,
        error_no_account,
    )

    # -----------------------------------------------------------------------
    
        
ft.app(login)
