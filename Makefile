# Makefile for Anki add-ons
#
# Prepares zip file for upload to AnkiWeb
# 
# Copyright: (c) 2017-2018 Glutanimate <https://glutanimate.com/>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

VERSION = `git describe HEAD --tags --abbrev=0`
ADDON = mini-format-pack
ADDONDIR = mini_format_pack


###

all: zip

clean: cleanbuild cleanzips

zip: cleanbuild ui builddir buildzip

release: cleanbuild builddir buildrelease

###

cleanzips:
	rm -f *-anki2*.zip

cleanbuild:
	rm -rf build
	find . \( -name '*.pyc' -o -name '*.pyo' -o -name '__pycache__' \) -delete

ui:
	PYENV_VERSION=anki21tools ./tools/build_ui.sh "$(ADDONDIR)" 5

builddir:
	mkdir -p build/dist

buildzip:
	rm -f *-current-anki2*.zip
	cp -r "src/$(ADDONDIR)" build/dist/
	rm -rf "build/dist/$(ADDONDIR)/forms5"
	cd build/dist && zip -r "../../$(ADDON)-current-anki21.zip" *
	rm -rf build

buildrelease:
	rm -f *-release-$(VERSION)-anki2*.zip
	git archive --format tar $(VERSION) | tar -x -C build/dist/
	rm -rf "build/dist/$(ADDONDIR)/forms5"
	cd build/dist &&  \
		PYENV_VERSION=anki21tools ../../tools/build_ui.sh "$(ADDONDIR)" 5 &&\
		cd src/"$(ADDONDIR)" && \
		zip -r "../../../../$(ADDON)-release-$(VERSION)-anki21.zip" *
	rm -rf build
