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


def parse_and_remove_arg(arg_str_repr_list, base_args):

    # validate --zone=value or '--zone value' format and exit on error
    arg_val = None
    for i in range(len(base_args)):
        for arg_str in arg_str_repr_list:
            if arg_str == base_args[i]:
                base_args.remove(base_args[i])
                try:
                    arg_val = base_args[i]
                    base_args.remove(base_args[i])
                except IndexError:
                    arg_val = None
                break
        if arg_val is not None:
            break


    return arg_val

def parse_extra_args():
    zone = parse_and_remove_arg(['-z', '--zone'], sys.argv)
    config = parse_and_remove_arg(['-c', '--config'], sys.argv)
    #print zone, config
    if zone is None or config is None:
        print "missing required arg"
        exit(1)

    creds = get_openrc(config)
    creds['region-name'] = zone.upper()
    f_creds = format_cmd(creds)

    #sys.argv[0] = 'nova'
    sys.argv[1:1] =  f_creds
    return sys.argv



