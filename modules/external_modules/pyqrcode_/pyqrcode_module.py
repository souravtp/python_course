import pyqrcode

x = "Hello, world!"
qr = pyqrcode.create(x)
qr.svg("myqrcode.svg", scale=8)


s = f'https://images.pexels.com/photos/60597/dahlia-red-blossom-bloom-60597.' \
    f'jpeg?cs=srgb&dl=pexels-pixabay-60597.jpg&fm=jpg'
url = pyqrcode.create(s)
url.svg("myimage.svg", scale=8)
