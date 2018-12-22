# vim: set fileencoding=utf-8:
import logging
import commands
import os

if not os.path.exists('logs'):
    commands.getoutput('mkdir logs')

log_file = 'logs/' + args.target_host + ".log"
if os.path.exists(log_file):
    commands.getoutput('echo "" > ' + log_file)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(log_file)
logger.addHandler(fh)

formatter = logging.Formatter("%(asctime)s : %(name)s : %(lineno)d : %(levelname)s : %(message)s")
fh.setFormatter(formatter)
