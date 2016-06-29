find ./static/sass/*.scss -printf "%f\n" | xargs -I@ sass static/sass/@:static/css/@.css
sudo cp amndeepcom.service /etc/systemd/system/amndeepcom.service
sudo systemctl restart amndeepcom
sudo systemctl restart nginx
