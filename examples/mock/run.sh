#!/bin/bash

BASE=$(dirname $0)
SOAPUI_HOME=/opt/soapui

jybot --pythonpath $BASE/../..:$SOAPUI_HOME/bin/soapui-4.0.1.jar:$SOAPUI_HOME/lib/STAR.jar --escape star:STAR --variable PRJ:$BASE/tempconvert-soapui-project.xml --variable SUITE:suite --variable CASE:case --variable MOCK:mock $BASE/test.txt
