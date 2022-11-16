Name:		texlive-hmtrump
Version:	54512
Release:	1
Summary:	Describe card games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hmtrump
License:	cc-by-sa-4 other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hmtrump.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hmtrump.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a font with LuaLaTeX support for
describing card games.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/hmtrump
%{_texmfdistdir}/fonts/truetype/public/hmtrump
%doc %{_texmfdistdir}/doc/lualatex/hmtrump

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
