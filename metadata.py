@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        metadata['apt']['packages']['php-fpm'] = {'installed': True}

    return metadata, DONE

@metadata_processor
def add_extensions_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        for ext in node.metadata.get('php-fpm', {}).get('extensions', []):
            metadata['apt']['packages'][ext] = {'installed': True}

    return metadata, DONE