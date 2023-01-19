#!/usr/bin/env python
import subprocess
import os
clone_list = [
    ('git://code.qt.io/yocto/meta-boot2qt','e59a2e2069'),
    ('https://github.com/Freescale/meta-freescale','3158e7f2b5'),
    ('https://github.com/Freescale/meta-freescale-3rdparty','a690b71'),
    ('git://git.yoctoproject.org/meta-intel','4d5791d9ff'),
    ('git://git.yoctoproject.org/meta-mingw','422b96cb2b'),
    ('git://git.openembedded.org/meta-openembedded','f72a73b42'),
    ('git://git.openembedded.org/meta-python2','810d6d8'),
    ('git://code.qt.io/yocto/meta-qt6','3890ffe5e1'),
    ('git://git.yoctoproject.org/meta-raspberrypi','b4ec97e'),
    ('https://github.com/OE4T/meta-tegra','7992b966'),
    ('git://git.toradex.com/meta-toradex-bsp-common','789e231'),
    ('git://git.toradex.com/meta-toradex-nxp','c2de495'),
    ('git://git.yoctoproject.org/poky','c40ac16d79')
]

if __name__ == '__main__':
    for uri, git_hash in clone_list:
        base_name = os.path.basename(uri)
        proc = subprocess.Popen('git clone %s' % (uri), shell=True)
        ret = proc.communicate()
        if proc.returncode != 0:
            print('Error clone %s' % base_name)
            exit(1)
        origin_dir = os.getcwd()
        os.chdir(base_name)
        proc = subprocess.Popen('git checkout %s' % (git_hash), shell=True)
        ret = proc.communicate()
        if proc.returncode != 0:
            print('Error checkout to %s in %s' % (git_hash, base_name))
            exit(1)
        os.chdir(origin_dir)


