%define tarname   lkn_pdf
Summary:	Linux Kernel In A Nutshell Book
Summary(pl.UTF-8):	Książka "Linux Kernel In A Nutshell" (Jądro Linuksa w pigułce)
Name:		linux-kernel-nutshell
Version:	1
Release:	32
License:	Other uncritical OpenSource License, Creative Commons Attribution Sharealike License Version 2.5
Group:		Documentation/Other
Source0:	http://www.kernel.org/pub/linux/kernel/people/gregkh/lkn/lkn_pdf.tar.bz2
# Source0-md5:	fa043b05e9839aa0e840be123af2e91d
URL:		http://www.kroah.com/lkn/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Written by a leading developer and maintainer of the Linux kernel,
Linux Kernel in a Nutshell is a comprehensive overview of kernel
configuration and building, a critical task for Linux users and
administrators.

No distribution can provide a Linux kernel that meets all users'
needs. Computers big and small have special requirements that require
reconfiguring and rebuilding the kernel. Whether you are trying to get
sound, wireless support, and power management working on a laptop or
incorporating enterprise features such as logical volume management on
a large server, you can benefit from the insights in this book.

Linux Kernel in a Nutshell covers the entire range of kernel tasks,
starting with downloading the source and making sure that the kernel
is in sync with the versions of the tools you need. In addition to
configuration and installation steps, the book offers reference
material and discussions of related topics such as control of kernel
options at runtime.

A key benefit of the book is a chapter on determining exactly what
drivers are needed for your hardware. Also included are recipes that
list what you need to do to accomplish a wide range of popular tasks.

%description -l pl.UTF-8
"Linux Kernel in a Nutshell" (Jądro Linuksa w pigułce) to książka
napisana przez wiodącego programistę i maintainera jądra Linuksa,
będąca obszernym przeglądem procesu konfiguracji i budowania jądra -
zadania krytycznego dla użytkowników i administratorów Linuksa.

Dystrybucje nie są w stanie dostarczyć jądra pasującego do absolutnie
wszystkich potrzeb. Małe i duże komputery mają specjalne wymagania
wymagające czasem rekonfiguracji i przebudowania jądra. Przy próbach z
uruchamianiem dźwięku, sieci bezprzewodowej czy zarządzaniem energią
na laptopie albo wdrażaniu poważnych podsystemów takich jak
zarządzanie wolumenami logicznymi w dużym serwerze przydaje się
znajomość zagadnień przedstawionych w tej książce.

"Linux Kernel in a Nutshell" pokrywa cały zakres zadań związanych z
jądrem, począwszy od ściągnięcia źródeł i upewnienia się, że wersja
jądra odpowiada wersjom potrzebnych narzędzi. Oprócz kroków
konfiguracji i instalacji książka zawiera materiał referencyjny i
omówienie pobliskich zagadnień, takich jak sterowanie opcjami jądra
w czasie działania.

Istotną zaletą książki jest rozdział poświęcony określaniu jakie
dokładnie sterowniki są potrzebne dla danego sprzętu. Ponadto
dołączone są listy kroków potrzebnych do wykonania wielu popularnych
zadań.

%prep
%setup -q -n %{tarname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf
