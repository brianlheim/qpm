""" Qpm minor utilities. """
import os

def default_sclang_path():
    return os.getenv('QPM_SCLANG') or os.getcwd()

path_arg_help = 'Path to SuperCollider executable. Default: the value in $QPM_SCLANG, or, if unset'\
    ', the current directory.'
