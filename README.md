Small set of tools to work with multiple Openstack zones. These are all basically wrappers that add extra arguments to be able to work on multiple zones

# Tools:
- mneutron
- mnova
- mglance
- mcinder

All of them have two extra arguments:
    -c/--config <path>    Selects the config file (openrc)
    -z/--zone <zonename>  Selects the zone to work with


Example:

```bash
mnova.py -z bhs1 -c openrc list
mneutron.py -z bhs1 -c openrc subnet-list
mglance.py -z bhs1 -c openrc image-list
mcinder.py -z bhs1 -c openrc list
```

I personaly alias these to make them easier to use:

```bash
alias novabhs1="~/bin/mnova.py --zone bhs1 --config ~/cfg/openrc"
alias neutronbhs1="~/bin/mneutron.py --zone bhs1 --config ~/cfg/openrc"
alias cinderbhs1="~/bin/mcinder.py --zone bhs1 --config ~/cfg/openrc"
alias glancebhs1="~/bin/mglance.py --zone bhs1 --config ~/cfg/openrc"


alias novagra1="~/bin/mnova.py --zone gra1 --config ~/cfg/openrc"
alias neutrongra1="~/bin/mneutron.py --zone gra1 --config ~/cfg/openrc"
alias cindergra1="~/bin/mcinder.py --zone gra1 --config ~/cfg/openrc"
alias glancegra1="~/bin/mglance.py --zone gra1 --config ~/cfg/openrc"
```
