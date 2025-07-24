#!/usr/bin/env python3

import json
import sys

def main():
    inventory = {
        "_meta": {
            "hostvars": {
                "host1": {
                    "fly_rod": True
                }
            }
        },
        "all": {
            "children": [
                "groupA",
                "ungrouped"
            ]
        },
        "groupA": {
            "hosts": [
                "host1", "host2", "host3", "host4", "host5",
                "host6", "host7", "host8", "host9", "host10",
                "host11", "host12", "host13", "host14", "host15",
                "host16", "host17", "host18", "host19", "host20",
                "host21", "host22", "host23", "host24", "host25"
            ]
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    if '--list' in sys.argv:
        main()
    elif '--host' in sys.argv:
        # Not used since all hostvars are in _meta, which is needed for controller
        print(json.dumps({}))
    else:
        print("Usage: script.py --list or --host <hostname>", file=sys.stderr)
        sys.exit(1)
