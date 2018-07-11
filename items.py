pkg_apt = {
    'php-fpm': {},
}
svc_systemv = {
    'php7.0-fpm': {
        'needs': [
            'pkg_apt:php-fpm',
        ],
    },
}

files = {}

for pool_name,pool in node.metadata.get('php-fpm', {}).get('pools', {}).items():
    files['/etc/php/7.0/fpm/pool.d/{}.conf'.format(pool_name)] = {
        'source': 'etc/php/7.0/fpm/pool.d/pool.conf',
        'content_type': 'mako',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'context': {
            'pool_name': pool_name,
            'pool': pool,
        },
        'triggers': [
            'svc_systemv:php7.0-fpm:reload',
        ],
    }
