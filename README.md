# syslog-ng pushbullet destination

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Pushbullet](https://www.pushbullet.com) logging destination for [syslog-ng](https://www.syslog-ng.com).
This Python module enables sending log messages to Pushbullet clients.

## Installation

``` shell
sudo ./setup.py install
```

## Example

You can use `syslogng-pushbullet` to get a notification to your phone whenever
`sshd` accepts a key:

```
destination pushbullet {
  python(
    class("syslogng_pushbullet.PushbulletDestination")
    on-error("fallback-to-string")
    options(
      api_key("Your Pushbullet API key")
      device("Device nickname")
    )
  );
};

filter ssh_accept {
  program("sshd") and match("^Accepted key" value("MESSAGE"))
};

log { source(src); filter(ssh_accept); destination(pushbullet); };
```

