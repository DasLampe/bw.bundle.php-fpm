# Bundlewrap php-fpm
Install php7.0-fpm on Debian Stretch

__Don't use this for production! It's still work in progress!__

## Dependencies
[apt-Bundle](https://github.com/sHorst/bw.bundle.apt)

## Metadata
```python
    'php-fpm': {
        'pools': {
            'pool_name': {
                'user': 'www-data',
                'group': 'www-data',
                'mode': '0666',
                'pm': {
                    'mode': 'dynamic',
                    'max_children': '5',
                    'start_server': '2',
                    'min_spare_server': '1',
                    'max_spare_server': '3',
                    'proccess_idle_timeout': '10',
                    'max_request': '0',
                }

                'access_log': False,
                'access_format': '%R - %u %t \"%m %r\" %s',

                'slow_log': '',

                'disable_functions': False,

                'php_admin_value': {
                    'name': 'value',
                },
                'php_admin_flag': {
                    'flag': 'value',
                },
            },
        },
    },
```

Option disable_functions, disable ```shell_exex, system, exec, proc_open, popen, passthru, stream_socket_server, dl, phpinfo, posix_* apache_child_terminate apache_setenv, virtual```.
