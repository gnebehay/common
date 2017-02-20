#!/bin/bash

apt-get update >> /var/log/deb-update.log
apt-get upgrade -y >> /var/log/deb-upgrade.log
