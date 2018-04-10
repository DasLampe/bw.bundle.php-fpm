files = {}
actions = {}
pkg_apt = {}

if node.metadata.get('php-fpm', False):
    version = node.metadata['php-fpm'].get('version', '7')

    # Use dotdebt for jessie and php7
    if version == 7 and node.os_version[0] == 8:
        actions['dotdeb_trustkey'] = {
            'command': "wget https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg",
            'triggered': True,
            'triggers': {
                'action:force_update_apt_cache',
            }
        }
        files['/etc/apt/sources.list.d/dotdeb.list'] = {
            'content': "deb http://packages.dotdeb.org jessie all\n"\
                       "deb-src http://packages.dotdeb.org jessie all",
            'mode': '0660',
            'owner': 'root',
            'group': 'root',
            'triggers': {
                'action:dotdeb_trustkey',
            },
            'needed_by': {
                'pkg_apt:',
            }
        }

    #Install/Uninstall modules
    for module,status in node.metadata['php-fpm'].get('modules', {}).items():
        pkg_apt[module] = {'installed': status}

    #Install PHP Version
    if version == 7:
        svc_systemd = {
            "php7.0-fpm": {
                'needs': ['pkg_apt:php7.0-fpm'],
            }
        }
        pkg_apt = {
            'php7.0-fpm': {
                'installed': True,
            }
        }
        files['/etc/php/7.0/fpm/pool.d/www.conf'] = {
            'source': 'etc/php/7.0/fpm/pool.d/www.conf',
            'triggers': [
                'svc_systemd:php7.0-fpm:restart',
            ]
        }

    if version == 5:
        svc_systemd = {
            "php5-fpm": {
                'needs': ['pkg_apt:php5-fpm'],
            }
        }
        pkg_apt = {
            'php5-fpm': {
                'installed': True,
            }
        }
        files['/etc/php5/fpm/pool.d/www.conf'] = {
            'source': 'etc/php5/fpm/pool.d/www.conf',
            'triggers': [
                'svc_systemd:php5-fpm:restart',
            ]
        }