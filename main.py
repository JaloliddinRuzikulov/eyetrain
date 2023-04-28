import pystray
import PIL.Image

image = PIL.Image.open('crying.png')


def on_clicked(icon, item):
    if str(item) == 'Say hello!':
        print('Hello world!')
    elif str(item) == 'Exit':
        icon.stop()


icon = pystray.Icon(
    'walkies',
    image,
    menu=pystray.Menu(
        pystray.MenuItem(
            'Say hello!', on_clicked
        ),
        pystray.MenuItem(
            'Exit', on_clicked
        )

    )
)
icon.run()
