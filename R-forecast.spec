#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-forecast
Version  : 8.5
Release  : 10
URL      : https://cran.r-project.org/src/contrib/forecast_8.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/forecast_8.5.tar.gz
Summary  : Forecasting Functions for Time Series and Linear Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-forecast-lib = %{version}-%{release}
Requires: R-gtable
Requires: R-lazyeval
Requires: R-munsell
Requires: R-plyr
Requires: R-quadprog
Requires: R-quantmod
Requires: R-scales
Requires: R-tibble
BuildRequires : R-RcppArmadillo
BuildRequires : R-colorspace
BuildRequires : R-fracdiff
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-lazyeval
BuildRequires : R-lmtest
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : R-quadprog
BuildRequires : R-quantmod
BuildRequires : R-scales
BuildRequires : R-tibble
BuildRequires : R-timeDate
BuildRequires : R-tseries
BuildRequires : R-urca
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
forecast <img src="man/figures/logo.png" align="right" />
======================

%package lib
Summary: lib components for the R-forecast package.
Group: Libraries

%description lib
lib components for the R-forecast package.


%prep
%setup -q -c -n forecast

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552875210

%install
export SOURCE_DATE_EPOCH=1552875210
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forecast
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forecast
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library forecast
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  forecast || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/forecast/CITATION
/usr/lib64/R/library/forecast/DESCRIPTION
/usr/lib64/R/library/forecast/INDEX
/usr/lib64/R/library/forecast/Meta/Rd.rds
/usr/lib64/R/library/forecast/Meta/data.rds
/usr/lib64/R/library/forecast/Meta/features.rds
/usr/lib64/R/library/forecast/Meta/hsearch.rds
/usr/lib64/R/library/forecast/Meta/links.rds
/usr/lib64/R/library/forecast/Meta/nsInfo.rds
/usr/lib64/R/library/forecast/Meta/package.rds
/usr/lib64/R/library/forecast/Meta/vignette.rds
/usr/lib64/R/library/forecast/NAMESPACE
/usr/lib64/R/library/forecast/NEWS.md
/usr/lib64/R/library/forecast/R/forecast
/usr/lib64/R/library/forecast/R/forecast.rdb
/usr/lib64/R/library/forecast/R/forecast.rdx
/usr/lib64/R/library/forecast/data/Rdata.rdb
/usr/lib64/R/library/forecast/data/Rdata.rds
/usr/lib64/R/library/forecast/data/Rdata.rdx
/usr/lib64/R/library/forecast/doc/JSS2008.R
/usr/lib64/R/library/forecast/doc/JSS2008.Rmd
/usr/lib64/R/library/forecast/doc/JSS2008.pdf
/usr/lib64/R/library/forecast/doc/index.html
/usr/lib64/R/library/forecast/help/AnIndex
/usr/lib64/R/library/forecast/help/aliases.rds
/usr/lib64/R/library/forecast/help/figures/logo.png
/usr/lib64/R/library/forecast/help/forecast.rdb
/usr/lib64/R/library/forecast/help/forecast.rdx
/usr/lib64/R/library/forecast/help/paths.rds
/usr/lib64/R/library/forecast/html/00Index.html
/usr/lib64/R/library/forecast/html/R.css
/usr/lib64/R/library/forecast/tests/testthat.R
/usr/lib64/R/library/forecast/tests/testthat/test-accuracy.R
/usr/lib64/R/library/forecast/tests/testthat/test-acf.R
/usr/lib64/R/library/forecast/tests/testthat/test-arfima.R
/usr/lib64/R/library/forecast/tests/testthat/test-arima.R
/usr/lib64/R/library/forecast/tests/testthat/test-armaroots.R
/usr/lib64/R/library/forecast/tests/testthat/test-bats.R
/usr/lib64/R/library/forecast/tests/testthat/test-boxcox.R
/usr/lib64/R/library/forecast/tests/testthat/test-calendar.R
/usr/lib64/R/library/forecast/tests/testthat/test-clean.R
/usr/lib64/R/library/forecast/tests/testthat/test-dshw.R
/usr/lib64/R/library/forecast/tests/testthat/test-ets.R
/usr/lib64/R/library/forecast/tests/testthat/test-forecast.R
/usr/lib64/R/library/forecast/tests/testthat/test-forecast2.R
/usr/lib64/R/library/forecast/tests/testthat/test-ggplot.R
/usr/lib64/R/library/forecast/tests/testthat/test-graph.R
/usr/lib64/R/library/forecast/tests/testthat/test-hfitted.R
/usr/lib64/R/library/forecast/tests/testthat/test-mforecast.R
/usr/lib64/R/library/forecast/tests/testthat/test-modelAR.R
/usr/lib64/R/library/forecast/tests/testthat/test-msts.R
/usr/lib64/R/library/forecast/tests/testthat/test-newarima2.R
/usr/lib64/R/library/forecast/tests/testthat/test-nnetar.R
/usr/lib64/R/library/forecast/tests/testthat/test-refit.R
/usr/lib64/R/library/forecast/tests/testthat/test-season.R
/usr/lib64/R/library/forecast/tests/testthat/test-spline.R
/usr/lib64/R/library/forecast/tests/testthat/test-subset.R
/usr/lib64/R/library/forecast/tests/testthat/test-tbats.R
/usr/lib64/R/library/forecast/tests/testthat/test-thetaf.R
/usr/lib64/R/library/forecast/tests/testthat/test-tslm.R
/usr/lib64/R/library/forecast/tests/testthat/test-wrangle.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/forecast/libs/forecast.so
/usr/lib64/R/library/forecast/libs/forecast.so.avx2
/usr/lib64/R/library/forecast/libs/forecast.so.avx512
