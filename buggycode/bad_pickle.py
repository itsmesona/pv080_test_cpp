"""
idk
"""
# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas
#-in-python-and-how-to-avoid-them-e19fbe265e03
import base64
import subprocess
import cPickle



def transcode_file(request, filename):
    """
    Input injection
    """
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


def fooo(request, user):
    """
    # Assert statements
    """
    assert user.is_admin
    # secure code...



class RunBinSh(object):
    """
    Pickles
    """
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))


print(base64.b64encode(cPickle.dumps(RunBinSh())))
