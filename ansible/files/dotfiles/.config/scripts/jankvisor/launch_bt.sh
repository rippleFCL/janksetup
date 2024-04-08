#!/bin/bash
ssh vmaudio@10.0.1.30 -X -i ~/.ssh/id_hva_ed25519 bash "killall -q 'blueman-applet'; killall -q 'blueman-manager'; sleep 1; blueman-applet & blueman-manager; killall -q 'blueman-applet'"
