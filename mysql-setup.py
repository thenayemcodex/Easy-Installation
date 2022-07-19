import time, sys  , os
from os import system as commandprompt
class Main_Process:
	title = """\n
The easiest way to install Kivy is with pip, which installs Kivy using either a pre-compiled wheel, if available,\n"""

	def console(self,arg):
		for i in arg:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(.008)
	def Run_Again(self):
		self.Ask_User = input("\nDo you want run again ? ")
		if self.Ask_User == "y" or self.Ask_User == "Y":
			self.setup()
		elif self.Ask_User =="n" or self.Ask_User == "N":
			self.console("\nThank You For Using")
			sys.exit()
		else:
			sys.exit()
	def Kivy_Installation(self):
		self.console("\nInstallation for Kivy has been started")
			
		self.console("\nInstalling  source dependencies for Kivy")
		commandprompt("sudo apt-get install -y \ libsdl2-dev \ libsdl2-image-dev \ libsdl2-mixer-dev \ libsdl2-ttf-dev \ libportmidi-dev \ libswscale-dev \ libavformat-dev \ libavcodec-dev \ zlib1g-dev")
		commandprompt("sudo apt-get install -y \ libgstreamer1.0 \ gstreamer1.0-plugins-base \ gstreamer1.0-plugins-good")
		self.console('\nAll dependencies are installed')
			
		try:
			commandprompt('python -m pip install --pre "kivy[full]"')
			self.console("\nKivy has been Installed\n")
		except:
			commandprompt("pip3 install kivy")
			self.console('\nKivy installed successfully\n')
		self.console('\nRebooting Your System\n')
		commandprompt('sudo reboot')
		self.Run_Again()
	def KivyMD_Installation(self):
		self.console("\nInstallation for KivyMD has been started")
			
		self.console("\nInstalling  source dependencies for KivyMD")
		commandprompt("sudo apt-get install -y \ libsdl2-dev \ libsdl2-image-dev \ libsdl2-mixer-dev \ libsdl2-ttf-dev \ libportmidi-dev \ libswscale-dev \ libavformat-dev \ libavcodec-dev \ zlib1g-dev")
		commandprompt("sudo apt-get install -y \ libgstreamer1.0 \ gstreamer1.0-plugins-base \ gstreamer1.0-plugins-good")
		self.console('\nAll dependencies are installed')
			
		try:
			commandprompt("pip3 install kivymd")
			self.console('\nKivyMD has been installed\n')
		except exception as e:
			self.console('\nFailed to install KIVYMD\n', e)
		self.Run_Again()
	def MySQL_Installation(self):
		self.console("\nMysql install process started")
		
		commandprompt("sudo apt-get install mysql-server mysql-client -y")
		self.console("\nMysql-server and Mysql-client installed in your system")
		
		self.console('\nInstalling MYSQL-CONNECTOR')
		commandprompt("pip3 install mysql-connector")
		self.console("\nMysql connector installed")
		self.console("\n[1] Open New Tab\nModify this mysqld.cnf in this directory /etc/mysql/mysql.conf.d/mysqld.cnf\nIn your case may file name defferent.\nYou will filen a line or variable as 'bind-address = 127.0.0.1' comment out this line as '#bind-address = 127.0.0.1' [CTRL + X + Y] for save the file.Exit from the terminal . \n[2] Open terminal login into mysql as root user 'sudo mysql -u root -p' Enter sudo password . After successfully logged in you will see a command propmt like 'mysql>' \n[3] Now Create A New User for connecting from python file. \n$ show databases;\n$ use mysql\n$ select user,host,plugin from mysql.user;[6] Create New user:\n$ create user 'username'@'localhost' identified by 'password';\n$ grant all privileges on *.* to 'username'@'localhost';\n$ flush privileges\n$ exit and close the terminal\n[4] Open new terminal. now login into mysql without sudo  as 'mysql -u username -p' Enter mysql user password . Now you can access your mysql databases from python file. \n")
		self.Run_Again()
		
		
	def setup(self):
		self.console("\nUse root password for update your system")
		commandprompt('sudo apt-get update && apt-get dist-upgrade -y')
		self.console('\nyour system has been upgraded succesfully')
		
		self.console("\nupdating your pip and setuptools")
		commandprompt("python -m pip install --upgrade pip setuptools virtualenv")
		self.console("\nupgrading pip , setuptools and virtualenv is successful")
		
		self.virtual_environment_name = input("\nEnter Virtual Env. Name >> ")
		self.console("\nNow let's create a virtual environment for virtualization our system\n")
		commandprompt(f"python -m virtualenv {self.virtual_environment_name}")
		self.console("\nYour Virtual Environment is created successfully")
		
		 
		
		self.console("\nChose a option to activate your Virtual environment\n[1] Using Windows Machine CMD.\n[2] Using Bash terminal in Windows machine.\n[3] Using Ubuntu/Linux.")
		while True:
			self.activate_command = input("Choose terminal Caatagory >> ")
			
			self.console("\nPlease wait, Activating your environment")
			if self.activate_command == "1":
				commandprompt(f"{self.virtual_environment_name}\Scripts\activate")
				self.console("\nYour Virtual Environment is activated")
				break
			elif self.activate_command == "2":
				commandprompt(f"source {self.virtual_environment_name}/Scripts/activate")
				self.console("\nYour Virtual Environment is activated")
				break
			elif self.activate_command == "3":
				commandprompt(f'source {self.virtual_environment_name}/bin/activate')
				self.console("\nYour Virtual Environment is activated")
				break
			else:
				self.console('\nInvalid Option has been Chosen.\nPlease Chose Between this three')
		
		self.console("\n[1] Install Kivy[full]\n[2] Install KivyMD\n[3] Install MYSQL and Configure it")
		while True:
			self.Installation_choice = input("\nChoose terminal Caatagory >> ")
			
			self.console("\nPlease wait, Activating your environment")
			if self.Installation_choice == "1":
				self.Kivy_Installation()
				break
			elif self.Installation_choice == "2":
				self.KivyMD_Installation()
				break
			elif self.Installation_choice == "3":
				self.MySQL_Installation()
				break
			else:
				self.console('\nInvalid Option has been Chosen.\nPlease Chose Between this three')
		
		
		
			
		
prograssing = Main_Process()
prograssing.setup()




