from .pycorrelate import pcorrelate, ucorrelate, make_loglags, pnormalize


__author__ = """Antonino Ingargiola"""
__email__ = 'tritemio@gmail.com'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
