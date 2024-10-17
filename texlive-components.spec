Name:		texlive-components
Version:	63184
Release:	2
Summary:	Components of TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/components
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An introduction to the components and files users of TeX may
encounter.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/generic/components

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
