find ./static/sass/*.scss -printf "%f\n" | xargs -I@ sass static/sass/@:static/css/@.css
cat whitelist | xargs -I % cp -r % /var/www/amndeep.com/
sudo chown -R www-data:www-data /var/www/amndeep.com/
