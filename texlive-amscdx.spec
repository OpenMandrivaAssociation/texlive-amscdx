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
BuildSystem:	texlive
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

