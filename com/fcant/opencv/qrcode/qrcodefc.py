import qrcode

image = qrcode.make('hello, qrcode')
image.save('test.png')