%global tl_name amscdx
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2x
Release:	%{tl_revision}.1
Summary:	Enhanced commutative diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/amscdx
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The original amscd package provides a CD environment that emulates the
commutative diagram capabilities of AMS-TeX version 2.x. This means that
only simple rectangular diagrams are supported, with no diagonal arrows
or more exotic features. This enhancement package implements double
("fat"), dashed, and bidirectional arrows (left-right and up-down), and
color attributes for arrows and their annotations. The restriction to
rectangular geometry remains. This nevertheless allows the drawing of a
much broader class of "commutative-diagram-like" diagrams. This update,
2.2x of 2019-07-02, fixes the dashed-arrows parts placement bug, and
adds the package option 'lyx', for use with lyx to prevent conflict with
the already loaded amscd. The packages xcolor and graphicx are made
required.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/amscdx
%dir %{_datadir}/texmf-dist/source/latex/amscdx
%dir %{_datadir}/texmf-dist/tex/latex/amscdx
%doc %{_datadir}/texmf-dist/doc/latex/amscdx/README
%doc %{_datadir}/texmf-dist/doc/latex/amscdx/amscdx.pdf
%doc %{_datadir}/texmf-dist/source/latex/amscdx/amscdx.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscdx/amscdx.ins
%{_datadir}/texmf-dist/tex/latex/amscdx/amscdx.sty
