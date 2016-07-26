# [Spack](https://github.com/LLNL/spack) package repo for LVC software packaging

This holds a set of Spack packages for the Ligo-Virgo Collaboration (LVC) software.  It relies
on Spack and the builtin Spack packages, some of which may be overridden
by this repo.

## Getting started

Initial setup like:

```bash
cd /path/to/big/disk
git clone https://github.com/LLNL/spack.git
cd spack/var/spack/repos
git clone https://github.com/paulhopkins/lvc-spack.git
cd -
./spack/bin/spack compiler add /usr/bin/gcc
./spack/bin/spack repo add spack/var/spack/repos/lvc-spack
```

To not have to type a full path to `spack` and to gain some other shell-level features do

```bash
$ source spack/share/spack/setup-env.sh
```
