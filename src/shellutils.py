'''
Created on Nov 2, 2012

@author: peng
'''
import subprocess


def run_command(command, block=False):
    '''run command'''
    if isinstance(command, basestring):
        command = [command]
    p = subprocess.Popen(' '.join(command), bufsize=2048, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if block:
        p.wait()
    return p
