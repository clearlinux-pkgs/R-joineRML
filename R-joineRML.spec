#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-joineRML
Version  : 0.4.2
Release  : 8
URL      : https://cran.r-project.org/src/contrib/joineRML_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/joineRML_0.4.2.tar.gz
Summary  : Joint Modelling of Multivariate Longitudinal Data and
Group    : Development/Tools
License  : GPL-3.0
Requires: R-joineRML-lib = %{version}-%{release}
Requires: R-MatrixModels
Requires: R-foreach
Requires: R-ggplot2
Requires: R-gtable
Requires: R-lazyeval
Requires: R-mime
Requires: R-minqa
Requires: R-munsell
Requires: R-mvtnorm
Requires: R-nloptr
Requires: R-plyr
Requires: R-rngWELL
Requires: R-scales
Requires: R-statmod
Requires: R-tibble
BuildRequires : R-JM
BuildRequires : R-MatrixModels
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-cobs
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-joineR
BuildRequires : R-lazyeval
BuildRequires : R-lme4
BuildRequires : R-mime
BuildRequires : R-minqa
BuildRequires : R-munsell
BuildRequires : R-mvtnorm
BuildRequires : R-nloptr
BuildRequires : R-plyr
BuildRequires : R-randtoolbox
BuildRequires : R-rngWELL
BuildRequires : R-scales
BuildRequires : R-statmod
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
joineRML <img src="man/figures/hex.png" width = "175" height = "200" align="right" />
=====================================================================================

%package lib
Summary: lib components for the R-joineRML package.
Group: Libraries

%description lib
lib components for the R-joineRML package.


%prep
%setup -q -c -n joineRML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552892123

%install
export SOURCE_DATE_EPOCH=1552892123
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library joineRML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library joineRML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library joineRML
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  joineRML || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/joineRML/DESCRIPTION
/usr/lib64/R/library/joineRML/INDEX
/usr/lib64/R/library/joineRML/LICENSE
/usr/lib64/R/library/joineRML/Meta/Rd.rds
/usr/lib64/R/library/joineRML/Meta/data.rds
/usr/lib64/R/library/joineRML/Meta/features.rds
/usr/lib64/R/library/joineRML/Meta/hsearch.rds
/usr/lib64/R/library/joineRML/Meta/links.rds
/usr/lib64/R/library/joineRML/Meta/nsInfo.rds
/usr/lib64/R/library/joineRML/Meta/package.rds
/usr/lib64/R/library/joineRML/Meta/vignette.rds
/usr/lib64/R/library/joineRML/NAMESPACE
/usr/lib64/R/library/joineRML/NEWS.md
/usr/lib64/R/library/joineRML/R/joineRML
/usr/lib64/R/library/joineRML/R/joineRML.rdb
/usr/lib64/R/library/joineRML/R/joineRML.rdx
/usr/lib64/R/library/joineRML/data/Rdata.rdb
/usr/lib64/R/library/joineRML/data/Rdata.rds
/usr/lib64/R/library/joineRML/data/Rdata.rdx
/usr/lib64/R/library/joineRML/doc/index.html
/usr/lib64/R/library/joineRML/doc/joineRML.R
/usr/lib64/R/library/joineRML/doc/joineRML.Rmd
/usr/lib64/R/library/joineRML/doc/joineRML.html
/usr/lib64/R/library/joineRML/doc/technical.Rnw
/usr/lib64/R/library/joineRML/doc/technical.pdf
/usr/lib64/R/library/joineRML/help/AnIndex
/usr/lib64/R/library/joineRML/help/aliases.rds
/usr/lib64/R/library/joineRML/help/figures/hex.png
/usr/lib64/R/library/joineRML/help/joineRML.rdb
/usr/lib64/R/library/joineRML/help/joineRML.rdx
/usr/lib64/R/library/joineRML/help/paths.rds
/usr/lib64/R/library/joineRML/html/00Index.html
/usr/lib64/R/library/joineRML/html/R.css
/usr/lib64/R/library/joineRML/tests/testthat.R
/usr/lib64/R/library/joineRML/tests/testthat/Rplots.pdf
/usr/lib64/R/library/joineRML/tests/testthat/test-ancillary.R
/usr/lib64/R/library/joineRML/tests/testthat/test-boot.R
/usr/lib64/R/library/joineRML/tests/testthat/test-inputs.R
/usr/lib64/R/library/joineRML/tests/testthat/test-models.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/joineRML/libs/joineRML.so
/usr/lib64/R/library/joineRML/libs/joineRML.so.avx2
/usr/lib64/R/library/joineRML/libs/joineRML.so.avx512
