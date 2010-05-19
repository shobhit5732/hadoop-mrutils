#
# bootstrap.py:
# This script should be placed in the home directory of a cluster's master node and run there. Your
# keypair file should also exist in your home directory.
# 
# emr/run_cluster.py should take care of these dependencies.

import os
import commands

from BeautifulSoup import BeautifulSoup

CMDS = ["sudo yum install R"]
MACHINES_URL = "http://localhost:9100/machines.jsp"
KEYPAIR_FILE = "./emr-keypair.pem"

# Get all the slave node URLs.
cmd = "curl %s" % MACHINES_URL
status, output = commands.getstatusoutput(cmd)
if status != 0: raise Exception("Couldn't curl %s" % MACHINES_URL)

doc = BeautifulSoup(output)
slaves = []
for tr in doc.table.findAll("tr")[2:]:
    slaves.append(tr.findAll("td")[1].contents[0])

# Set up slave nodes.
for slave in slaves:
    for cmd in CMDS:
        cmd = "ssh -o StrictHostKeyChecking=no -i %s hadoop@%s '%s'" % (cmd)
        print cmd
        status, output = commands.getstatusoutput(cmd)
    



