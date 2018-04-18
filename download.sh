chmod +x *.py *.sh
sudo pip install --upgrade -r requirements.txt

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
sudo apt-get install -y libav-tools

./get_item.sh "item_id"
