# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

"""Run BioSQL tests using PostgreSQL."""

import unittest

import requires_internet

# Really do want "import *" to get all the test classes:
from common_BioSQL import *  # noqa: F403
from common_BioSQL import check_config

# Import these explicitly to avoid flake8 F405 below:
from common_BioSQL import load_biosql_ini
from common_BioSQL_online import *  # noqa: F403
from common_BioSQL_online import share_config

requires_internet.check()

DBDRIVER = "psycopg2"
DBTYPE = "pg"
DBHOST, DBUSER, DBPASSWD, TESTDB = load_biosql_ini(DBTYPE)

# This will abort if driver not installed etc:
check_config(DBDRIVER, DBTYPE, DBHOST, DBUSER, DBPASSWD, TESTDB)
share_config(DBDRIVER, DBTYPE, DBHOST, DBUSER, DBPASSWD, TESTDB)

if __name__ == "__main__":
    # Run the test cases
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
