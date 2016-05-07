## i3blocks-openweather

Is a i3blocks blocklet script to output the current weather type and temperature.

### Dependecies
* fonts-font-awesome
* python3
* pyowm

### Suggested
* i3 ( >= 4.3 )
* i3blocks ( >= 1.4 )

### Appearance

![](https://raw.githubusercontent.com/p-hash/i3blocks-openweather/master/images/1.png)

### Usage
1. Clone repo
2. Add your `api_key` to `weather.py`. If you dont have an `api_key`, get it [here](http://openweathermap.org/appid).
3. Copy `i3blocks.conf` contents into your i3blocks configuration file.
4. Replace `5128638` with your city ID. 
List of city ID city.list.json.gz can be downloaded [here](http://bulk.openweathermap.org/sample/)

### Example config for New York
```INI
[weather]
command=$SCRIPT_DIR/weather.py
markup=pango
instance=5128638
interval=3600
```
