Name:		texlive-amscdx
Version:	51532
Release:	2
Summary:	Enhanced commutative diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/amscdx
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscdx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The original amscd package provides a CD environment that
emulates the commutative diagram capabilities of AMS-TeX
version 2.x. This means that only simple rectangular diagrams
are supported, with no diagonal arrows or more exotic features.
This enhancement package implements double ("fat"), dashed, and
bidirectional arrows (left-right and up-down), and color
attributes for arrows and their annotations. The restriction to
rectangular geometry remains. This nevertheless allows the
drawing of a much broader class of "commutative-diagram-like"
diagrams. This update, 2.2x of 2019-07-02, fixes the
dashed-arrows parts placement bug, and adds the package option
'lyx', for use with lyx to prevent conflict with the already
loaded amscd. The packages xcolor and graphicx are made
required.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/amscdx
%{_texmfdistdir}/tex/latex/amscdx
%doc %{_texmfdistdir}/doc/latex/amscdx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
