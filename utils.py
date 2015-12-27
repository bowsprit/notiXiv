"""General utility methods.

Classes
-------

Functions
---------

"""

import logging
import inspect
import numpy as np


class IndentFormatter(logging.Formatter):
    """Logging formatter where the depth of the stack sets the message indentation level.
    """
    def __init__(self, fmt=None, datefmt=None):
        logging.Formatter.__init__(self, fmt, datefmt)
        self.baseline = None

    def format(self, rec):
        stack = inspect.stack()
        if self.baseline is None: self.baseline = len(stack)
        indent = (len(stack)-self.baseline)
        addSpace = ((indent > 0) & (not rec.msg.startswith(" -")))
        rec.indent = ' -'*indent + ' '*addSpace
        out = logging.Formatter.format(self, rec)
        del rec.indent
        return out


def getLogger(name, strLevel=logging.WARNING, fileLevel=logging.DEBUG, tofile=None):
    """Create a standard logger object which logs to file and or stdout stream.

    If logging to output stream (stdout) is enabled, an `IndentFormatter` object is used.

    Arguments
    ---------
    name : str,
        Handle for this logger, must be distinct for a distinct logger.
    strLevel : int,
        Logging level for stream.
    fileLevel : int,
        Logging level for file.
    tofile : str or `None`,
        Filename to log to (turned off if `None`).

    Returns
    -------
    logger : ``logging.Logger`` object,
        Logger object to use for logging.

    """

    logger = logging.getLogger(name)
    # Make sure handlers don't get duplicated (ipython issue)
    while len(logger.handlers) > 0: logger.handlers.pop()
    # Prevents duplication or something something...
    logger.propagate = 0

    # Determine and Set Logging Levels
    if fileLevel is None: fileLevel = logging.DEBUG
    if strLevel is None: strLevel = logging.WARNING
    #     Logger object must be at minimum level (cast to int to avoid error)
    useLevel = int(np.min([fileLevel, strLevel]))
    logger.setLevel(useLevel)

    dateFmt = '%Y/%m/%d %H:%M:%S'
    fileFmt = "%(asctime)s %(levelname)8.8s [%(filename)20.20s:"
    fileFmt += "%(funcName)-20.20s]%(indent)s%(message)s"
    strFmt = "%(indent)s%(message)s"

    # Log to file
    # -----------
    if tofile is not None:
        fileFormatter = IndentFormatter(fileFmt, datefmt=dateFmt)
        fileHandler = logging.FileHandler(tofile, 'w')
        fileHandler.setFormatter(fileFormatter)
        fileHandler.setLevel(fileLevel)
        logger.addHandler(fileHandler)
        #     Store output filename to `logger` object
        logger.filename = tofile

    # Log To stdout
    # -------------
    strFormatter = IndentFormatter(strFmt, datefmt=dateFmt)
    strHandler = logging.StreamHandler()
    strHandler.setFormatter(strFormatter)
    strHandler.setLevel(strLevel)
    logger.addHandler(strHandler)

    return logger
