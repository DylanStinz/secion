import flet as ft

def main(page: ft.Page):
    page.title = "Ficha alumno"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        value="Inicio de sesión",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK
    )

    email = ft.TextField(
            label="Email",
            hint_text="usuario@gmail.com",
             prefix_icon=ft.Icons.EMAIL
             )

    contra = ft.TextField(
        label="Ingrese su contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.PASSWORD
    )
    
    boton = ft.ElevatedButton(
       "Iniciar sesión",
       icon=ft.Icons.LOGIN
    )
    boton2 = ft.ElevatedButton(
       "¿Olvidaste tu contraseña?",
       icon=ft.Icons.KEY
       
    )


    page.add(
        titulo,
        email,
        contra,
        boton,
        boton2
    )

if __name__ == "__main__":
    ft.app(target=main)