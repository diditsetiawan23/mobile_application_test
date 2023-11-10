import os
import jpype as jp
import datetime
import socket
import platform

class StartReporting:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.datenow = self.now.strftime("%d-%m-%Y")
        # Define report path
        self.reportpath = os.path.join(
            "reports", "HTML Report", f"Mobile_Test_Report_{self.datenow}.html"
        )

        # Get environtment
        env = "Development"
        # Get hostname
        hostname = socket.gethostname()

        lib_dir = os.path.join(os.getcwd(), "lib")
        list_of_jars = [
            "extentreports-5.1.1.jar",
            "freemarker-2.3.32.jar",
            "gson-2.10.1.jar",
            "lombok-1.18.26.jar",
            "reactive-streams-1.0.4.jar",
            "rxjava-3.1.6.jar",
        ]
        # Get username
        current_platform = platform.system()

        if current_platform == 'Windows':
            username = os.getlogin()
        elif current_platform == 'Linux':
            # Get the effective user ID (UID)
            import pwd
            uid = os.geteuid()
            username = pwd.getpwuid(uid).pw_name
        else:
            username = "Unknown Environtment"

        jars_path = [os.path.join(lib_dir, jar) for jar in list_of_jars]
        self.classpath = os.pathsep.join(jars_path)

        jp.startJVM(
            jp.getDefaultJVMPath(), "-ea", f"-Djava.class.path={self.classpath}"
        )

        self.ExtentReports = jp.JClass("com.aventstack.extentreports.ExtentReports")
        self.ExtentTest = jp.JClass("com.aventstack.extentreports.ExtentTest")
        self.LogStatus = jp.JClass("com.aventstack.extentreports.Status")
        self.Reporters = jp.JClass("com.aventstack.extentreports.reporter.ExtentSparkReporter")
        self.Theme = jp.JClass("com.aventstack.extentreports.reporter.configuration.Theme")

        self.html = self.Reporters(self.reportpath)
        self.extent = self.ExtentReports()
        html_config = self.html.config()
        self.extent.attachReporter(self.html)
        self.extent.setSystemInfo("Host Name", f"{hostname}")
        self.extent.setSystemInfo("Environment", f"{env}")
        self.extent.setSystemInfo("User Name", f"{username}")
        html_config.setDocumentTitle("API Automation Report")
        html_config.setReportName(f"API Automation Report on {env} Environtment")
        html_config.setTheme(self.Theme.STANDARD)	

# initiate StoreReporting class
test_suite = StartReporting()
LogStatus = test_suite.LogStatus
extent = test_suite.extent
uiparent = extent.createTest("Example Login Register")
