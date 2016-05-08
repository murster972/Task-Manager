import os
import psutil

class Processes(object):
	def __init__(self):
		pass

	def OptionsMenu(self):
		os.system("clear")
		print "[1] Display Processes"
		print "[2] Terminate Process"
		print "[3] Main Menu"
		try:
			opt = int(raw_input("Option: "))

			try:
				optsDict = {1: lambda: Processes.DisplayProccess(self), 2:  lambda: Processes.GetUserProccess(self), 3: lambda: main()}
				optsDict[opt]()

			except KeyError:
				print "Invalid Option."
				pause = raw_input()
				Processes.OptionsMenu(self)

		except ValueError:
			print "Invalid Option."
			pause = raw_input()
			Processes.OptionsMenu(self)

	def DisplayProccess(self):
		proccess = os.popen('ps -ef').readlines()

		for i in proccess:
			print i

		pause = raw_input()
		Processes.OptionsMenu(self)

	def GetUserProccess(self):
		killMethod = raw_input("kill by ID or process: ")
		killProccess = raw_input("process: ")

		if len(killProccess) > 0 and killMethod == "ID" or killMethod == "process":
			Processes.validateProccess(self, killMethod, killProccess)

		else:
			print "Invalid Process or Process Method."
			pause = raw_input()
			Processes.OptionsMenu(self)

	def validateProccess(self, method, procc):
		if method == "ID":
			try:
				proc = int(procc)
				PIDS = psutil.get_pid_list()
				x = 0

				while x < (len(PIDS) + 1):
					if x != len(PIDS):
						if PIDS[x] == proc:
							Processes.TerminateProccess(self, method, proc)
							#print PIDS[x]
							break

						else:
							pass

					else:
						print "Invalid Process or Process Method."

					x += 1



			except ValueError:
				print "Invalid Process or Process Method."

		else:
			Processes.TerminateProccess(self, method, procc)

	def TerminateProccess(self, killBy, proccess):
		killMethods = {"ID": "kill", "process": "pkill"}

		try:
			os.system(killMethods[killBy] + " " + str(proccess))
			print "'%s' successfully killed" % str(proccess)
			pause = raw_input()
			Processes.OptionsMenu(self)

		except RuntimeError:
			print "Failed to kill '%s'" % str(proccess)
			pause = raw_input()
			Processes.OptionsMenu(self)

class SysInfo(object):
	def __init__(self):
		pass

	def OptionsMenu(self):
		os.system("clear")
		print "[1] CPU Information"
		print "[2] Ram Information"
		print "[3] Network Information"
		print "[4] Main Menu"

		try:
			opt = int(raw_input("option: "))

			try:
				optsDict = {1: lambda: SysInfo.Cpu(self), 2: lambda: SysInfo.Ram(self), 3: lambda: SysInfo.Network(self), 4: lambda: main()}

				optsDict[opt]()

			except KeyError:
				print "Invalid Option."
				pause = raw_input()
				SysInfo.OptionsMenu(self)

		except ValueError:
			print "Invalid Option."
			pause = raw_input()
			SysInfo.OptionsMenu(self)

	def Cpu(self):
		cpuPerc = psutil.cpu_percent(percpu = True)
		print "Number of CPU's: " + str(psutil.NUM_CPUS)
		print "CPU 1: %s, CPU 2: %s" % (str(cpuPerc[0]), str(cpuPerc[1]))
		pause = raw_input()
		SysInfo.OptionsMenu(self)

	def Ram(self):
		VirMemInfo = {0: "Total: ", 1: "Available: ", 2: "Percent: ", 3: "Used: ", 4: "Free: ", 5: "Active: ", 6: "Inactive: ", 7: "Buffers: ", 8: "Cached: "}
		VirMem = psutil.virtual_memory()

		for x in range(len(VirMem)):
			print VirMemInfo[x] + str(VirMem[x])

		pause = raw_input()
		SysInfo.OptionsMenu(self)

	def Network(self):
		netInfo = {0: "Bytes Sent: ", 1: "Bytes Received: ", 2: "Packets Sent: ", 3: "Packets Received: ", 4: "Errors While Receiving: ", 5: "Errors While Sending: ", 6: "Incoming Packets Dropped: ", 7: "Outgoing Packets Dropped: ", 8: "Cached: "}
		net = psutil.net_io_counters(False)

		for x in range(len(net)):
			print netInfo[x] + str(net[x])

		pause = raw_input()
		SysInfo.OptionsMenu(self)

def main():
	os.system("clear")
	print "====__Basic Task Manager__===="
	print "[1] Processes"
	print "[2] Computer Info"

	try:
		option = int(raw_input("Option: "))

		if option == 1:
			run = Processes()
			run.OptionsMenu()

		elif option == 2:
			run = SysInfo()
			run.OptionsMenu()

		else:
			print "Invalid Option."
			pause = raw_input()
			main()

	except ValueError:
		print "Invalid Option."
		pause = raw_input()
		main()

if __name__ == '__main__':
	main()