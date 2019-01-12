# Gnu General Public License - see LICENSE.TXT

from __future__ import absolute_import, division, unicode_literals

from resources.lib.simple_logging import SimpleLogging
from resources.lib.functions import mainEntryPoint

log = SimpleLogging('default')

log.debug("About to enter mainEntryPoint()")

mainEntryPoint()

# clear done and exit.
# sys.modules.clear()
