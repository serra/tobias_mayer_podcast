#!/usr/bin/env python
from audacity import PipeClient
import time

if __name__ == "__main__":
    aud = PipeClient()
    aud.write('Help: Command=Help')
    reply = ''

    while reply == '':
        time.sleep(0.1)
        reply = aud.read()

    print(reply)

    # open a source file
    # select all
    # apply amplify effect, with peak level set to -1.0
    pass
