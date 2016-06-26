find ./static/sass/*.scss -printf "%f\n" | xargs -I@ sass static/sass/@:static/css/@.css
sudo restart amndeepcom
sudo service nginx restart
