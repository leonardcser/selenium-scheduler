#!bin/sh

set -xe

DEST_DIR=~/.selenium_scheduler
LAUNCH_AGENT_DIR=~/Library/LaunchAgents
LAUNCH_AGENT_NAME="selenium_scheduler.startup.cronjob.plist"

if [ -d "$DEST_DIR" ]; then
  rm -rf $DEST_DIR
fi

if [ -e "$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME" ]; then
  launchctl unload "$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME"
  rm "$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME"
fi

echo "Successfully uninstalled!"
