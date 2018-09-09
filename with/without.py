text = None
try:
    text = open("text.txt", 'w')
    try:
        text.write('without nandayo')
    except:
        raise
finally:
    if text:
        text.close()

