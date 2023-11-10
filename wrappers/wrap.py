import os
import datetime
from utils import logger
from telegram import Bot
from bs4 import BeautifulSoup as BS
from utils import htmlreport as report
from dotenv import load_dotenv
from config import configuration as config

# logging
logs = logger.AutomationTestLogging()
logger = logs.logger

# get date
now = datetime.datetime.now()
datenow = now.strftime("%d-%m-%Y")
formatted_date = now.strftime('%Y-%m-%d')
timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

# Load environment variables from .env file
env_path = os.getcwd()+os.path.join('/config','.env')
load_dotenv(env_path)

def cheeky_new(line):
    """Check new lines on logs"""
    if line != 0:
        return "\n"
    return ""

def write_file(file, strlist):
    """Write and saving file"""
    line = 0
    lines = []
    while line < len(strlist):
        lines.append(cheeky_new(line) + strlist[line])
        line += 1
    file = open(file, "a+")
    file.writelines(lines)
    file.close()

def print_log_file(text):
    """Writing logs to file"""
    filename = "Execution_Logs_" + datenow + ".txt"
    path = os.getcwd() + os.path.join("/", "logs", filename)
    if config.config.get("logging"):
        if not bool(BS(text, "html.parser").find()):
            logger.info(text)
            write_file(path, ["[" + timestamp + "]" + text + "\n \n"])
    else:
        logger.info("Seems the Logging is being disable")

def init_extent_report(feature_title):
    parent = report.uiparent
    extent = report.extent
    log_status = report.LogStatus
    sub_parent = parent.createNode(feature_title)
    return extent, parent, log_status, sub_parent

def init_test_cases(parent_nodes, testcase_title):
    parent = parent_nodes.createNode(testcase_title)
    return parent

def extent_end_test(extent):
    extent.flush()

async def send_result_to_telegram():
    bot = Bot(token=f'{os.getenv("BOT_TOKEN")}')
    group_chat_id = f'{os.getenv("CHAT_ID")}'
    await bot.initialize()
    file_path = os.getcwd()+os.path.join('/reports','HTML Report', f'Mobile_Test_Report_{datenow}.html')
    try:
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id=group_chat_id, document=file, caption=f'Here are Mobile Application test result for {formatted_date} !')
    except Exception as e:
        print(f"Error: {e}")