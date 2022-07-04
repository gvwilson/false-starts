## ---- : ----

MANIFESTS = $(dir $(wildcard */MANIFEST.md) $(wildcard */data/MANIFEST.md) $(wildcard */results/MANIFEST.md))

## manifests : Check that all manifests are up to date.
manifests :
	bin/checkmanifest.py ${MANIFESTS}
