#!/bin/sh
set -ex

ssh deploy@pycon.jp uptime
# please replace for deployment commands
ssh deploy@pycon.jp sh /opt/workspace/deploy-scripts/update.sh production 2016

