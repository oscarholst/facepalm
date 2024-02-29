#!/bin/bash
set -Eeuo pipefail
# =======================================================================
# Facepalm for Linux installation script.
#
# Source code is available at https://github.com/docker/docker-install/
#
# =======================================================================

do_install() {
    echo "Hello world, executing installation script!"
    curl -s https://raw.githubusercontent.com/oscarholst/facepalm/main/facepalm.py -o /usr/share/pyshared/facepalm.py
    chmod +x /usr/share/pyshared/facepalm.py
    curl -s https://raw.githubusercontent.com/oscarholst/facepalm/main/facepalm.service -o /etc/systemd/system/facepalm.service
    systemctl daemon-reload
    systemctl start facepalm
    systemctl enable faceplam
    echo "Installation complete!"
}
do_install