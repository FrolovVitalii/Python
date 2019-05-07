#!/usr/bin/python

import commands
import argparse
import sys
import locale
import re
import json

def GetMetricsCpu():
        return commands.getoutput("top -p 1 -n 1 | grep Cpu")

def GetMetricsMem():
        return commands.getoutput("top -p 1 -n 1 | grep Mem:")

def GetMetricsSwap():
        return commands.getoutput("top -p 1 -n 1 | grep Swap:")


def CreateParser ():
        parser = argparse.ArgumentParser()
        parser.add_argument ('-n', '--name', type=str, default="null")
        return parser

def ForDebug(inputMetrics, deviceName):
         print("For Debug " + deviceName + "Metrics")
         print("---------")
         counter = 0
         for metric in inputMetrics:
                print (counter)
                print (metric)
                counter = counter+1
         print("---------")

def ConvertDictMetricsToJson(dictData):
        return json.dumps(dictData)

def ReturnDataStruct(listParam):
        local = str(locale.getdefaultlocale())
        delimeter = " "
        if(listParam[0]=="null"):
                print("##########################################")
                print("# Error. You need to use a key.          #")
                print("# -n Cpu for getting cpu metrics         #")
                print("# -n Mem for getting memory metrics      #")
                print("# Example:  python2.7 metrics.py -n Cpu  #")
                print("##########################################")

        if(listParam[0]=="Cpu"):
                cpuMetrics = GetMetricsCpu()
		arrTempMetricCpu = cpuMetrics.split("  ")
                q1 = arrTempMetricCpu[3].split(delimeter)[2]
                q2 = arrTempMetricCpu[1].split(delimeter)[0]
                q3 = arrTempMetricCpu[5].split(delimeter)[0]
                q4 = arrTempMetricCpu[4].split(delimeter)[0]
                q5 = arrTempMetricCpu[7].split(delimeter)[0]
                q6 = arrTempMetricCpu[2].split(delimeter)[0]
                dictCpuUse = {"system.cpu.idle":q1, "system.cpu.user":q2, "system.cpu.guest":q3, "system.cpu.iowait":q4, "system.cpu.stolen":q5, "system.cpu.system":q6}
                return dictCpuUse

        if(listParam[0]=="Mem"):
		tempMem = re.findall(r'\b\d+\b', GetMetricsMem())
		tempSwap = re.findall(r'\b\d+\b', GetMetricsSwap())
#		print(tempMem)
#		print(tempSwap)
                q1 = tempMem[1]
                q2 = tempMem[4]
                q3 = tempMem[7]
                q4 = tempMem[10]
                q5 = tempSwap[1]
                q6 = tempSwap[4]
                q7 = tempSwap[7]
       	        q8 = tempSwap[10]
                dictMemUse = {"virtual.total":q1, "virtual.used":q2, "virtual.free":q3, "virtual.buffers":q4, "swap.total":q5, "swap.used":q6, "swap.free":q7, "swap.cached":q8}
                return dictMemUse


if __name__ == '__main__':
        parser = CreateParser()
        namespace = parser.parse_args(sys.argv[1:])
        listParams = list()
        listParams.append(namespace.name)
        try:
                testMetrics = ReturnDataStruct(listParams)
                for itemMetric in testMetrics:
                        result = str(itemMetric) + " : " + str(testMetrics[itemMetric])
                        print (result)
        except:
                print ("Error!")


