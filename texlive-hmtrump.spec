%global tl_name hmtrump
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Describe card games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/hmtrump
License:	cc-by-sa-4 other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hmtrump.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hmtrump.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a font with LuaLaTeX support for describing card
games.

