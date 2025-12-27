import os
import sys
import shlex

def tts(message):
    message = str(message)
    escaped_message = shlex.quote(message)
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(f'{tts_engine} {escaped_message}')
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(f'{tts_engine} {escaped_message}')