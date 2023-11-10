# Example Login/Register using Appium Application README

Welcome to the application ! This README provides instructions on how to set up and run the application on your machine.

## Prerequisites

Before running the Appium application, ensure that the following prerequisites are met on your machine:

- **Python:** Install Python on your machine. You can download it from [python.org](https://www.python.org/).

- **Open JDK:** Ensure that Open JDK is installed on your machine, and the `JAVA_HOME` environment variable is properly set.

- **Microsoft C++ Buildtools (for Windows):** If you are running the application on Windows, you need to install Microsoft C++ Buildtools. Follow these steps:

    1. Download the file from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
    
    2. Install the downloaded file.

    3. Choose Workloads:
        - Tick on **Desktop Development with C++**.

    4. Tick the following items:
        - Windows 10 SDK
        - MSVC v143 -VS 2022 C++
        - C++ CMake tools for Windows

    5. Click Install and wait until the installation is finished.

- **Appium Server:** Ensure that the Appium server is already installed on your machine. You can find the installation instructions on the [Appium official website](http://appium.io/).

## Installation

1. Clone or download the Appium application from the repository.

2. Navigate to the project directory in the terminal.

3. Install the required Python libraries by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- Set up the `udid` inside the `config` folder in the `configuration.py` file. Update the file with the appropriate device UDID.
- To join the Telegram group and receive alerts, click https://t.me/+h9PxYVJguFlkYWRl.

## Running the Application

Once you have completed the installation and configuration, you can run the Appium application. Ensure that the Appium server is already installed and running on your machine.

Execute the following command to run the application:

```bash
python test_runner.py
```
