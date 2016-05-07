i3blocks-openweather is an i3blocks blocklet script to output the current weather type and temperature.

Dependencies: fonts-font-awesome, python3, pyowm

Suggested: i3 ( >= 4.3 ), i3blocks ( >= 1.4 )

It looks like this:

![](https://raw.githubusercontent.com/p-hash/i3blocks-openweather/master/images/1.png)

To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[weather]
command=$SCRIPT_DIR/weather.py
markup=pango
# instance=CITYID
instance=5128638
interval=3600
```
