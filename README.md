# SDTLConverter
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ThomasThelen/sdtl-converter/master)

A python script for turning SDTL in JSON-LD into ProvONE/Prov.

### Status

Things seems to work fine with commands that aren't using data from
other commands. Support for commands that use other data is under
development. I recently did a refactor and pulled the retrospective
provenance out, but will re-add it once I get data usage working (to
reduce complexity).

### Try it Out

The following examples are currently working.

`single_command`

`two_commads`

`three_commands`

`load_command`

To run an example, open `converter.py`, scroll to the bottom and replace the SDTL filename with the one you're interested in.
