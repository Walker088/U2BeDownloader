item_id="$1"

if ls|grep "$item_id"
then
	echo "$item_id already exist"
else
	./get_plitem_url.py
fi	
