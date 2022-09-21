#!bin/sh

set -xe

DEST_DIR=~/.selenium_scheduler
LAUNCH_AGENT_DIR=~/Library/LaunchAgents
LAUNCH_AGENT_NAME="selenium_scheduler.startup.cronjob.plist"

sh ./scripts/uninstall.sh

mkdir $DEST_DIR

cp -r ./selenium_scheduler $DEST_DIR
cp ./entrypoint.py "$DEST_DIR/entrypoint.py"
cp ./.env "$DEST_DIR/.env"
cp ./scripts/run.sh "$DEST_DIR/run.sh"
chmod +x "$DEST_DIR/run.sh"

python3 -m venv "$DEST_DIR/.venv"
source "$DEST_DIR/.venv/bin/activate"
pip install --upgrade pip
pip install -r ./requirements/requirements.txt

cp "./scripts/$LAUNCH_AGENT_NAME" $LAUNCH_AGENT_DIR
sed -i.bak "s/USER/$USER/g" "$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME"

launchctl load "$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME"

echo "Done!"
