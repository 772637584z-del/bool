from flet import*

def main(page:Page):
    page.title = "Rakwan python"
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left =960
    page.window.width = 390
    page.window.height =740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT


    flashlight = Flashlight()
    page.overlay.append(flashlight)

    ph = PermissionHandler()
    page.overlay.append(ph)

    def open_app(e):
        ph.open_app_settings()


    page.add(
        AppBar(
            title = Text('Flash Light [RK]'),
            color='white',
            bgcolor='#e3113e',
            actions=[
                IconButton(Icons.SETTINGS,on_click=open_app)
            ]
        ),

        Row([
            Text('\n\nFlash Light App',size=31,color='black')
        ],alignment=MainAxisAlignment.CENTER),

       

        Row([

            ElevatedButton(
                "ON",
                width=100,
                icon=Icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on()
            ),

             ElevatedButton(
                "OFF",
                width=100,
                icon=Icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_off()
            )
        
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text('\n\nrakwan python apss 2025',size=12,color='black')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text('\nحسام للبرمجيات \n784089909-784089909a@gmail.com',size=12,color='blue')
        ],alignment=MainAxisAlignment.CENTER),

    )




    page.update()
app(main)
