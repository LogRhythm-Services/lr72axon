# LogRhythm7 To Axon Migration

## Installation

1. Download python:
https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

   Make sure to install pip in the advanced options of the installer and add the binaries to your $PATH environmental variable.


2. Unzip this Project into a directory, e.g. C:\LogRhythm\lr72axon


3. Open a CMD terminal and navigate to the directory where you unzipped the project
    ```cd C:\LogRhythm\lr72axon```


4. Inside that you must have a file called "requirements.txt", we will use this file to install the required python packages:

    ```pip install -r requirements.txt```

   This step is only the first time and may take a while. 
   If you get an error about "Access Denied" you may need to run the command prompt as an administrator.


5. Now install the package:

    ```pip install .```


6. If you're going to use the API I suggest saving your LogRhythm API key in the environment variable "LR_API_KEY" and the AXON API Key into the variable "AXON_API_KEY".

```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
```


## How to Use The AIE Conversion Tool

### Getting Help

```
python -m lr72axon.AIE2AxonRule -h

usage: AIE2AxonRule.py [-h] (-f FILE | -d DIRECTORY | -a) [--ids RULEID] [--lr-url LR_URL] [--lr-api-key APIKEY] [-x] --axon-api-key AXON_API_KEY [--tenant-id TENANT_ID] [--axon-url AXON_URL]
                       [-c {default,nlp,vector}] [-O DIRECTORY] [-o] [-u]

CLI tool converting AIE Rules into Axon Rules

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify a single rule file to process.
  -d DIRECTORY, --directory DIRECTORY
                        Specify a directory containing the JSON exported AIERules
  -a, --api             Establish API Mode to gather the AIE Rule from LR API directly
  --ids RULEID          Comma-separated list of rule IDs or ranges e.g., '1,2,4-6' Only valid with -a/--api.
  --lr-url LR_URL       Base URL for the API
  --lr-api-key APIKEY   API key for authentication. Only valid with -a/--api.
  -x, --create          Create the Axon List if it does not exist
  --axon-api-key AXON_API_KEY
                        Axon API Key
  --tenant-id TENANT_ID
                        Axon Tenant ID
  --axon-url AXON_URL   Base URL for the API
  -c {default,nlp,vector}, --conversion-mode {default,nlp,vector}
                        Specify the conversion mode. Can be 'default', 'nlp', or 'vector'. Default is 'default'. Selecting nlp or vector may impact performance.
  -O DIRECTORY, --output-directory DIRECTORY
                        Specify an output directory. Default is c:\LogRhythm\AxonRules.
  -o, --skip-observables
                        Skip processing of observables.
  -u, --skip-unattributed
                        Skip processing of unattributed entities.
```                     

### Explaining the -x /--create flag
The latest version of this CLI tool includes an additional flag called -x or --create. 
This flag is used to create the Axon List if it does not exist. This is useful when you are converting AIE rules that contain lists that are not present in Axon.

Keep in mind that even if you don't specify this flag, the tool will still query the Axon API to check if the list exists, and if it doesn't, it will log a warning message and just create the filter for manual resolution.

First remember create your  API key in the LogRhythm Console, then you can run the following command:

```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.AIE2AxonRule -f examples\aie_rules\PCI.json  --create --axon-api-key %AXON_API_KEY% --tenant-id lrtraining -x --lr-url http://127.0.0.1:8505 --lr-api-key %LR_API_KEY%
 
2024-04-03 19:04:14,983 - INFO - Searching for Axon list: LR7Migration Users and type: ('STRING',)
2024-04-03 19:04:15,415 - INFO - Searching for Axon list: LR7Migration Users and type: ('LONG_TEXT',)
2024-04-03 19:04:15,776 - INFO - Searching for Axon list: LR7Migration Users and type: ('INTEGER',)
2024-04-03 19:04:16,125 - INFO - Searching for Axon list: LR7Migration Users and type: ('DATE',)
2024-04-03 19:04:16,462 - INFO - Searching for Axon list: LR7Migration Users and type: ('GEO_POINT',)
2024-04-03 19:04:16,804 - INFO - Searching for Axon list: LR7Migration Users and type: IP
2024-04-03 19:04:17,141 - INFO - List LR7Migration Users found or created in Axon, expanding now.
2024-04-03 19:04:17,141 - INFO - Returning new criteria: [{'origin.account.name in SUBLIST_ec4b349e-0fc3-44bc-9e4f-19f0e8290b2b_LR7Migration Users': 'origin.account.name in LIST;2191e5ec-c090-4dc1-a9dc-c238f80cf976;267b7d29-fd45-44de-a8bc-93079c93c05e'}]
2024-04-03 19:04:17,143 - INFO - Successfully saved Axon rule LR2A: PCI-DSS: Vendor Auth Failure Alert to c:\LogRhythm\AxonRules\PCI.json
2024-04-03 19:04:17,143 - INFO - Successfully conversion for  AIE rule LR2A: PCI-DSS: Vendor Auth Failure Alert
```

Given the fact AXON has dedicated values for the columns and sometimes into LR7 lists you may find IP's or Hostnames, in such cases the tool will create a new list in AXON with the same name and type as the LR7 list (for each value type) and then it will expand the rule to use the new list.

### Converting a Single Exported AIE Rule File
```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.AIE2AxonRule -f "examples\aie_rules\Brute Force Follow by Auth.json" --axon-api-key %AXON_API_KEY% --tenant-id lrtraining -x --lr-url http://127.0.0.1:8505 --lr-api-key %LR_API_KEY%

Block type ThresholdObserved is supported, converting AIE rule CSF: Ext Brute Force Sngl Host
Block type LogObserved is supported, converting AIE rule CSF: Ext Brute Force Sngl Host
Successfully saved Axon rule CSF: Ext Brute Force Sngl Host to c:\LogRhythm\AxonRules\Brute Focer Follow by Auth.json
```

### Converting a Directory of Exported AIE Rules
```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.AIE2AxonRule -d "examples\aie_rules" --axon-api-key %AXON_API_KEY% --tenant-id lrtraining -x --lr-url http://127.0.0.1:8505 --lr-api-key %LR_API_KEY%

Block type Trend - 13 is not supported, skipping AIE rule Attainment: Abnormal File Access
Block type LogObserved is supported, converting AIE rule All Operators
Successfully saved Axon rule All Operators to c:\LogRhythm\AxonRules\AllOperators.json
Block type ThresholdObserved is supported, converting AIE rule CSF: Ext Brute Force Sngl Host
Block type LogObserved is supported, converting AIE rule CSF: Ext Brute Force Sngl Host
Successfully saved Axon rule CSF: Ext Brute Force Sngl Host to c:\LogRhythm\AxonRules\Brute Focer Follow by Auth.json
Block type LogObserved is supported, converting AIE rule Exfiltration: UEBA and Sensitive Data (NGFW) Detection
Block type LogObserved is supported, converting AIE rule Exfiltration: UEBA and Sensitive Data (NGFW) Detection
Successfully saved Axon rule Exfiltration: UEBA and Sensitive Data (NGFW) Detection to c:\LogRhythm\AxonRules\Exfiltration_UEBA_and_Sensitive_Data_Detection.json
Block type UniqueValuesObserved is supported, converting AIE rule Recon: Failed Distributed Brute Force
Block type LogNotObservedCompound - 2 is not supported, skipping AIE rule Recon: Failed Distributed Brute Force
Block type ThresholdObserved is supported, converting AIE rule CCF: Large Outbound Transfer
Successfully saved Axon rule CCF: Large Outbound Transfer to c:\LogRhythm\AxonRules\Large Transfer.json
Block type ThresholdObserved is supported, converting AIE rule Recon: Multiple Lockouts
Successfully saved Axon rule Recon: Multiple Lockouts to c:\LogRhythm\AxonRules\Multiple Lockouts.json
Block type UniqueValuesObserved is supported, converting AIE rule Compromise: Multiple Unique Attack Events
Successfully saved Axon rule Compromise: Multiple Unique Attack Events to c:\LogRhythm\AxonRules\Multiple Unique Attacks.json
Block type LogObserved is supported, converting AIE rule T1489:Service Stop
Successfully saved Axon rule T1489:Service Stop to c:\LogRhythm\AxonRules\ObservedPattern.json
Block type LogObserved is supported, converting AIE rule All Operators Blank
Successfully saved Axon rule All Operators Blank to c:\LogRhythm\AxonRules\OperatorsBlank.json
Block type Statistical - 12 is not supported, skipping AIE rule HSS: Primary Eligible Professional Utilization Statistics
Block type LogObserved is supported, converting AIE rule T1053:Scheduled Task/Job
Successfully saved Axon rule T1053:Scheduled Task/Job to c:\LogRhythm\AxonRules\T1053_Schedule Task.json
```

### Converting AIE Rules from the API

First remember create your  API key in the LogRhythm Console, then you can run the following command:

```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.AIE2AxonRule --api --ids 1259-1270 --axon-api-key %AXON_API_KEY% --tenant-id lrtraining -x --lr-url http://127.0.0.1:8505 --lr-api-key %LR_API_KEY%

Block type ThresholdObserved is supported, converting AIE rule Disruption: Files Deleted by Admin
Successfully saved Axon rule Disruption: Files Deleted by Admin to c:\LogRhythm\AxonRules\1259 - Disruption_Files_Deleted_by_Admin.json
Block type Trend - 13 is not supported, skipping AIE rule Lateral: Abnormal Auth Behavior
Block type LogObserved is supported, converting AIE rule Compromise: Account Added to Admin Group
Successfully saved Axon rule Compromise: Account Added to Admin Group to c:\LogRhythm\AxonRules\1261 - Compromise_Account_Added_to_Admin_Group.json
Block type Statistical - 12 is not supported, skipping AIE rule Lateral: Admin Password Modified
Block type UniqueValuesObserved is supported, converting AIE rule Lateral: Auth After Dispersed Failed Auths
Block type LogObserved is supported, converting AIE rule Lateral: Auth After Dispersed Failed Auths
Successfully saved Axon rule Lateral: Auth After Dispersed Failed Auths to c:\LogRhythm\AxonRules\1263 - Lateral_Auth_After_Dispersed_Failed_Auths.json
Block type ThresholdObserved is supported, converting AIE rule Lateral: Brute Force Internal Auth Failure
Block type LogNotObservedCompound - 2 is not supported, skipping AIE rule Lateral: Brute Force Internal Auth Failure
Block type LogObserved is supported, converting AIE rule Lateral: External Attack then Account Creation
Block type LogObserved is supported, converting AIE rule Lateral: External Attack then Account Creation
Successfully saved Axon rule Lateral: External Attack then Account Creation to c:\LogRhythm\AxonRules\1265 - Lateral_External_Attack_then_Account_Creation.json
Block type UniqueValuesObserved is supported, converting AIE rule Lateral: Failed Auths then Success
Block type LogObserved is supported, converting AIE rule Lateral: Failed Auths then Success
Successfully saved Axon rule Lateral: Failed Auths then Success to c:\LogRhythm\AxonRules\1266 - Lateral_Failed_Auths_then_Success.json
Block type LogObserved is supported, converting AIE rule Lateral: Internal Attack then Account Creation
Block type LogObserved is supported, converting AIE rule Lateral: Internal Attack then Account Creation
Successfully saved Axon rule Lateral: Internal Attack then Account Creation to c:\LogRhythm\AxonRules\1267 - Lateral_Internal_Attack_then_Account_Creation.json
Block type LogObserved is supported, converting AIE rule Lateral: Internal Recon then Account Creation
Block type LogObserved is supported, converting AIE rule Lateral: Internal Recon then Account Creation
Successfully saved Axon rule Lateral: Internal Recon then Account Creation to c:\LogRhythm\AxonRules\1268 - Lateral_Internal_Recon_then_Account_Creation.json
Block type UniqueValuesObserved is supported, converting AIE rule Lateral: Multiple Account Passwords Modified by Admin
Successfully saved Axon rule Lateral: Multiple Account Passwords Modified by Admin to c:\LogRhythm\AxonRules\1269 - Lateral_Multiple_Account_Passwords_Modified_by_Admin.json
Block type UniqueValuesObserved is supported, converting AIE rule Lateral: Numerous and Dispersed Internal Failed Auths
Block type LogNotObservedCompound - 2 is not supported, skipping AIE rule Lateral: Numerous and Dispersed Internal Failed Auths
```

After running the api mode, you can find the rules in the output directory you specified and 2 log files where you run the command, these files contain the successfully converted rules and the rules that were skipped.

## How to Use The LogRhythm7 List Conversion Tool

### Getting Help

```
python -m lr72axon.LR7List2AxonList -h

usage: LR7List2AxonList.py [-h] (-n FILE | -a | -s SEARCH) --lr-api-key LR_API_KEY [--lr-url LR_URL] --axon-api-key AXON_API_KEY [--tenant-id TENANT_ID] [--axon-url AXON_URL] [-d]

CLI tool converting LogRhythm7 Lists to Axon Lists

options:
  -h, --help            show this help message and exit
  -n FILE, --name FILE  Specify The LogRhythm List to be Converted
  -a, --all             Convert All LogRhythm Lists
  -s SEARCH, --search SEARCH
                        Search for a List in Axon
  --lr-api-key LR_API_KEY
                        LogRhythm API Key
  --lr-url LR_URL       Base URL for the API
  --axon-api-key AXON_API_KEY
                        Axon API Key
  --tenant-id TENANT_ID
                        Axon Tenant ID
  --axon-url AXON_URL   Base URL for the API
  -d, --debug           Enable Debug Logging
```

### Converting a Single LogRhythm7 List
If you specify -d option it'll save the payload into the path: C:\LogRhythm\AxonLists\
```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.LR7List2AxonList -n "Demo Follow" --lr-api-key %LR_API_KEY% --axon-api-key %AXON_API_KEY%

2024-03-31 15:51:29,840 - INFO - Processing list: 7AADAEFE-BC3D-41E1-A79B-83028AC315BA - Name: Demo Follow
2024-03-31 15:51:29,859 - INFO - Processing nested list: 0365d611-aea9-4705-a099-a4b0fbd4dc35 from item: Abuse.ch : IP : Ransomware Command and Control
2024-03-31 15:51:29,860 - INFO - Processing list: 0365d611-aea9-4705-a099-a4b0fbd4dc35
2024-03-31 15:51:29,886 - INFO - Successfully saved Axon rule to C:\LogRhythm\AxonLists\Demo_Follow - 1
2024-03-31 15:51:29,893 - INFO - Successfully saved Axon rule to C:\LogRhythm\AxonLists\Demo_Follow - 2
```

### Converting All LogRhythm7 Lists
```
set LR_API_KEY=eyJhbGciOiJSUzI1NiIsInR5cCI....
set AXON_API_KEY=abcdefABCDEF1234....
python -m lr72axon.LR7List2AxonList -a --lr-api-key %LR_API_KEY% --axon-api-key %AXON_API_KEY%

2024-03-31 16:03:49,868 - INFO - Processing list: 1FDCEEEA-09AB-4C3F-9DE5-93B258E11A2C - Name: HC: Privileged Users
2024-03-31 16:03:49,888 - ERROR - No items found for GUID 1FDCEEEA-09AB-4C3F-9DE5-93B258E11A2C - Name: HC: Privileged Users.
2024-03-31 16:03:49,906 - INFO - Processing list: 3DAC143D-B2D6-4EF7-87A2-9A1D189F0094 - Name: CCF: Shared Accounts List
2024-03-31 16:03:49,923 - ERROR - No items found for GUID 3DAC143D-B2D6-4EF7-87A2-9A1D189F0094 - Name: CCF: Shared Accounts List.
2024-03-31 16:03:49,945 - INFO - Processing list: 459AF098-7C76-4960-BEAE-DF9FB958B5B5 - Name: MA: Local Accounts
2024-03-31 16:03:49,965 - ERROR - No items found for GUID 459AF098-7C76-4960-BEAE-DF9FB958B5B5 - Name: MA: Local Accounts.
2024-03-31 16:03:50,404 - INFO - Processing list: D42D7F2E-F573-4D5E-BEFA-DACBFFB7275F - Name: Open Source : abuse.ch URLHaus : Domain : Malware

2024-03-31 16:03:51,522 - INFO - Successfully saved Axon rule to C:\LogRhythm\AxonLists\Open_Source__abusech_URLHaus__Domain__Malware - 1
```
