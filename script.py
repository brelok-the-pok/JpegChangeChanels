from turbojpeg import TurboJPEG


def change_channels(bgr_array):
    arr = bgr_array.copy()
    for h in arr:
        for w in h:
            b, g, r = w[0], w[1], w[2]
            w[0], w[1], w[2] = g, r, b
    return arr


# using default library installation
jpeg = TurboJPEG('turbojpeg.dll')

# decoding input.jpg to BGR array
in_file = open('33.jpg', 'rb')
bgr_array = jpeg.decode(in_file.read())
in_file.close()


new_bgr_array = change_channels(bgr_array)
new_bgr_array = bgr_array

# encoding BGR array to output.jpg with quality level i.
qualities = [100, 10]
for quality in qualities:
    out_file = open('output_3/3_out_{}.jpg'.format(quality), 'wb')
    out_file.write(jpeg.encode(new_bgr_array, quality=quality))
    out_file.close()
