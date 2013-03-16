#!/usr/bin/env python

from fabric.api import env, sudo, local
from fabric.operations import put, run
from fabric.context_managers import cd

def hyde_gen():
    local('hyde gen')

def server():
    env.hosts = ['razz.hotnudiegirls.com']

def deploy():
    hyde_gen()
    put('deploy/*', '/var/www/', use_sudo=True)

def clean():
    # This is probably a terrible idea...
    local('rm -rf deploy')
