# Bundlewrap php-fpm
Install php7.0-fpm or php5-fpm on Debian Jessie.

__Don't use this for production! It's still work in progress!__

## Options
```json
'php-fpm': {
    'version': 7,
    'modules': {
        'php7.0-gd': True,
        'php7.0-mysql': False,
    },
}
```
