import googletrans as tl
import flet as ft

def main(page: ft.Page):

    # Page Propierties -----------------------

    page.title = "Translate Everthing"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # -----------------------------------------

    # Code ------------------------------------

    translator = tl.Translator()
    translated_text
    
    text_input = ft.TextField(label="Texto a traducir")
    text_output = ft.Text()



    # -----------------------------------------