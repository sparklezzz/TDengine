###################################################################
#           Copyright (c) 2016 by TAOS Technologies, Inc.
#                     All rights reserved.
#
#  This file is proprietary and confidential to TAOS Technologies.
#  No part of this file may be reproduced, stored, transmitted,
#  disclosed or used in any form or by any means other than as
#  expressly provided by the written permission from Jianhui Tao
#
###################################################################

# -*- coding: utf-8 -*-

import sys
import taos
from util.log import *
from util.cases import *
from util.sql import *
import numpy as np


class TDTestCase:
    def init(self, conn, logSql):
        tdLog.debug("start to execute %s" % __file__)
        tdSql.init(conn.cursor())

        self.rowNum = 10
        self.ts = 1537146000000
        
    def run(self):
        tdSql.execute("use db")

        intData = []        
        floatData = []

        for i in range(self.rowNum):
            intData.append(i + 1)            
            floatData.append(i + 0.1)                        

        # sum verifacation 
        tdSql.error("select sum(ts) from test")
        tdSql.error("select sum(col7) from test")
        tdSql.error("select sum(col8) from test")
        tdSql.error("select sum(col9) from test")

        tdSql.query("select sum(col1) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col2) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col3) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col4) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col11) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col12) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col13) from test")
        tdSql.checkData(0, 0, np.sum(intData))
        tdSql.query("select sum(col14) from test")
        tdSql.query("select sum(col5) from test")
        tdSql.checkData(0, 0, np.sum(floatData)) 
        tdSql.query("select sum(col6) from test")
        tdSql.checkData(0, 0, np.sum(floatData))              

    def stop(self):
        tdSql.close()
        tdLog.success("%s successfully executed" % __file__)

tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())
