# -*- coding:utf-8 -*-
from datetime import datetime
from convert_1 import get_kurs, get_nominal, respons, valid_code, spros

kod_valute = spros()
valid_code(kod_valute)
get_kurs(kod_valute)
get_nominal(kod_valute)