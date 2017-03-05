#!/usr/bin/env python2

import sys

from novaclient.shell import main

def get_openrc(file_path):
    try:
        with open(file_path) as f:
            creds = {}
            for line in f:
                if len(line) > 2:
                    line = line.strip('\n').split()[-1]
                    line = line.replace("'", "")
                    line = line.encode('ascii','ignore')
                    if '=' in line:
                        key_pair = line.split('=')
                        creds[key_pair[0]] = key_pair[1]
    except:
        print "Can't open config file: {}".format(file_path)
        exit()

    d = {}
    d['version'] = '2'
    d['username'] = creds['OS_USERNAME']
    d['password'] = creds['OS_PASSWORD']
    d['auth-url'] = creds['OS_AUTH_URL']
    d['tenant-name'] = creds['OS_TENANT_NAME']
    return d


def format_cmd(creds):
    base = '--os-region {} --os-auth-url {} --os-username {} --os-password {} --os-tenant-name {}'

    ret_val = base.format(creds['region-name'], creds['auth-url'], creds['username'], creds['password'], creds['tenant-name'])
    return ret_val.split()


def parse_zone_in_args(base_args):

    # validate --zone=value or '--zone value' format and exit on error
    zone = 'empty'
    for i in range(len(base_args)):
        if '-z=' in base_args[i]:
            zone = base_args[i]
            zone = zone.replace('-z=', '')
            base_args.remove(base_args[i])
            break
        elif '-z' == base_args[i]:
            base_args.remove(base_args[i])
            zone = base_args[i]
            base_args.remove(base_args[i])
            break
    if zone == 'brute':
        return zone

    if zone is 'empty':
        print 'no zone privided\nUSAGE: proxy_nova.py -z zone_name <args>'
        exit()

    return zone.upper()


if __name__ == '__main__':

    zone = parse_zone_in_args(sys.argv)
    creds = get_openrc('/home/sublime/dev/os-test/openrc')
    creds['region-name'] = zone
    f_creds = format_cmd(creds)

    sys.argv[0] = 'nova'
    sys.argv[1:1] =  f_creds
    sys.exit(main())


