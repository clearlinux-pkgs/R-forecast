#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v12
# autospec commit: 381dfd8
#
Name     : R-forecast
Version  : 8.23.0
Release  : 64
URL      : https://cran.r-project.org/src/contrib/forecast_8.23.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/forecast_8.23.0.tar.gz
Summary  : Forecasting Functions for Time Series and Linear Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-forecast-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-colorspace
Requires: R-fracdiff
Requires: R-generics
Requires: R-ggplot2
Requires: R-lmtest
Requires: R-magrittr
Requires: R-timeDate
Requires: R-tseries
Requires: R-urca
Requires: R-withr
Requires: R-zoo
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-colorspace
BuildRequires : R-fracdiff
BuildRequires : R-generics
BuildRequires : R-ggplot2
BuildRequires : R-lmtest
BuildRequires : R-magrittr
BuildRequires : R-timeDate
BuildRequires : R-tseries
BuildRequires : R-urca
BuildRequires : R-withr
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
univariate time series forecasts including exponential smoothing
             via state space models and automatic ARIMA modelling.

%package lib
Summary: lib components for the R-forecast package.
Group: Libraries

%description lib
lib components for the R-forecast package.


%prep
%setup -q -n forecast
pushd ..
cp -a forecast buildavx2
popd
pushd ..
cp -a forecast buildavx512
popd
pushd ..
cp -a forecast buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718987759

%install
export SOURCE_DATE_EPOCH=1718987759
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/R/library/forecast/libs/forecast.so
/V4/usr/lib64/R/library/forecast/libs/forecast.so
/VA/usr/lib64/R/library/forecast/libs/forecast.so
/usr/lib64/R/library/forecast/libs/forecast.so
