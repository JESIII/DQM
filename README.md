# DQM
# Getting Started:

Extract contents of DQM.zip to desktop of Raspberry Pi.

There are 3 Files that should be on the desktop: DQM_FirstTimeSetup, DQM_AfterRebootSetup, and DQM_Script.py

If it is the first time setting up the Pi you will open up the terminal and type: /home/pi/Desktop/DQM_FirstTimeSetup
Press enter and the script will partially setup the serial port and then reboot.

Upon reboot the DQM_AfterRebootSetup script will automatically run and finish setting up the serial port and install all dependencies for the main python script.

Once everything is installed the main sript will start automatically and will start every time you reboot or open up a terminal.

# Function:

A JSON String is sent to a log file in /home/pi/Documents/DQMLogs every 10 seconds.

Example JSON String:
{"DQM_Data":{"messages":[{"work_event":{"msg_time":"","ch_heading":"230.22","ch_latitude":"ch_lat","ch_longditude":"230   ","ch_depth":"230.22","ch_heading":"230","slurry_velocity":"230.22","slurry_density":"230.22","pump_rpm":"0      ","vacuum":"230.22","outlet_psi":"23.22 ","comment":"we_comment"}},{"contract_event":{"msg_time":"","contract_number":"we_comment","event_type":"we_comment","comment":"we_comment"}},{"station_event":{"msg_time":"","station_name":"station_name","comment":"se_comment"}},{"pipe_length_event":{"msg_time":"","length_floating":"230       ","length_submerged":"230       ","length_land":"230       ","comment":"ple_comment"}},{"booster_pump_event":{"msg_time":"","booster_total":"230       ","comment":"bpe_comment"}},{"advance_event":{"msg_time":"","advanced_daily":"230       ","comment":"ae_comment"}},{"outfall_position":{"msg_time":"","outfall_location":"test","outfall_latitude":"230   ","outfall_longitude":"230   ","outfall_heading":"230","outfall_elevation":"230.220001","comment":"test"}},{"non_eff_event":{"msg_start_time":"","msg_end_time":"","function_code":"test","comment":"test"}}]}

90 Days worth of logs are kept on the MicroSD Card in /home/pi/Documents/DQMLogs

Strings are sent at the same rate to a log file in /media/pi/USB STICK/DQMLogs

(Currently the USB STICK folder exists regardless of a USB Stick being plugged in and I need to do some tweaking to get it to only work when a USB Stick is actually plugged in. It is currently assumed that a stick is plugged in at all times)

At the end of every day (0000 / 12:00 AM) the log for the day is sent to the cloud storage which can be accessed at ftp://192.168.1.28

Logs are never purged from the cloud storage unless done manually.
