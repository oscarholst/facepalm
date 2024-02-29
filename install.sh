#!/bin/bash
set -Eeuo pipefail
# =======================================================================
# Facepalm for Linux installation script.
#
# https://github.com/oscarholst/facepalm/
#
# =======================================================================

do_install() {
    echo "Hello world, executing installation script!"
    curl -s https://raw.githubusercontent.com/oscarholst/facepalm/main/dist/facepalm -o /usr/bin/facepalm
    chmod +x /usr/bin/facepalm
    curl -s https://raw.githubusercontent.com/oscarholst/facepalm/main/facepalm.service -o /etc/systemd/system/facepalm.service
    systemctl daemon-reload
    systemctl start facepalm
    systemctl enable facepalm
    echo "Installation complete!"
}
do_install