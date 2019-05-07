#!/usr/bin/python

import psutil
import commands
import argparse
import sys
import locale

def GetMetricsCpu():
	return psutil.cpu_times()

def GetMetricsMem():
	return psutil.virtual_memory()

def GetMetricsSwap():
	return psutil.swap_memory()

def CreateParser ():
        parser = argparse.ArgumentParser()
        parser.add_argument ('-n', '--name', type=str, default="null")
        return parser


def Program(listParam):
        local = str(locale.getdefaultlocale())
        delimeter = " "
        if(listParam[0]=="null"):
                print("##########################################")
                print("# Error. You need to use a key.          #")
                print("# -n Cpu for getting cpu metrics         #")
                print("# -n Mem for getting memory metrics      #")
                print("# Example:  python2.7 metrics.py -n Cpu  #")
                print("##########################################")

        if(listParam[0].lower()=="cpu"):
		metricsTemp = GetMetricsCpu()
		print("system.cpu.user " + str( metricsTemp.user))
                print("system.cpu.nice "+ str(metricsTemp.nice))
                print("system.cpu.system "+ str(metricsTemp.system))
                print("system.cpu.idle "+ str(metricsTemp.idle))
                print("system.cpu.iowait "+ str(metricsTemp.iowait))
                print("system.cpu.irq "+ str(metricsTemp.irq))
		print("system.cpu.softirq "+ str(metricsTemp.softirq))
		print("system.cpu.steal "+ str(metricsTemp.steal))
		print("system.cpu.guest "+ str(metricsTemp.guest))


        if(listParam[0].lower()=="mem"):
		metricsTempMem = GetMetricsMem()
		metricsTempSwap	= GetMetricsSwap()	
		print("system.mem.total " + str( metricsTempMem.total))
		print("system.mem.available "+ str(metricsTempMem.available))
		print("system.mem.percent "+ str(metricsTempMem.percent))
		print("system.mem.used "+ str(metricsTempMem.used))
		print("system.mem.free "+ str(metricsTempMem.free))
		print("system.mem.active "+ str(metricsTempMem.active))
		print("system.mem.inactive "+ str(metricsTempMem.inactive))
		print("system.mem.buffers "+ str(metricsTempMem.buffers))
		print("system.mem.cached "+ str(metricsTempMem.cached))
		print("system.mem.shared "+ str(metricsTempMem.shared))
		print("system.mem.slab "+ str(metricsTempMem.slab))
		print("system.swap.total "+ str(metricsTempSwap.total))
		print("system.swap.used "+ str(metricsTempSwap.used))
		print("system.swap.free "+ str(metricsTempSwap.free))
		print("system.swap.percent "+ str(metricsTempSwap.percent))
		print("system.swap.sin "+ str(metricsTempSwap.sin))
		print("system.swap.sout "+ str(metricsTempSwap.sout))

if __name__ == '__main__':
        parser = CreateParser()
        namespace = parser.parse_args(sys.argv[1:])
        listParams = list()
        listParams.append(namespace.name)
        try:
	        Program(listParams)
        except:
                print ("Error!")


