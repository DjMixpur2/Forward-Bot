echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/DjMixpur2/Forward-Bot DjMixpur2/Forward-Bot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/DjMixpur2/Forward-Bot -b $BRANCH /Ultra-Forward-Bot
fi
cd DjMixpur2/Forward-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
