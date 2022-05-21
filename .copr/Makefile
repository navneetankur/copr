srpm:
ifeq ($(notdir $(spec)), wayfire-git.spec)
	dnf -y install git-core
	git clone --depth=1 --recurse-submodules --shallow-submodules https://github.com/WayfireWM/wayfire
	tar cf wayfire.tar.gz wayfire/
	rpmbuild -bs "$(spec)" --define "_topdir ." --define "_sourcedir ." --define "_srcrpmdir $(outdir)"
endif
