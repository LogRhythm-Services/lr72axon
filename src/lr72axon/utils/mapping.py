# Dict to define all the common event classes and subclasses in Axon
axon_common_events = [
    {'name': 'General', 'guid': 'fe61f063-44e0-47f5-85af-7f8274813d5b', 'description': '', 'subclasses': [{'name': 'General Alert', 'guid': 'b737adbd-173c-4fa9-a64b-3b630772635f', 'description': 'Messages with a status of ALERT'}, {'name': 'General Audit', 'guid': 'fb4604c8-52fd-470c-b14e-2c373d5f4118', 'description': 'Audit messages without a designated severity.'}, {'name': 'General Critical', 'guid': '4a98a905-a35d-4a2f-b957-105bf3366100', 'description': 'Messages with a status of CRITICAL or CRIT'}, {'name': 'General Debug', 'guid': 'c578abc7-1007-4fd1-bc4c-f6afcc2d65b4', 'description': 'Messages with a status of DEBUG or DEBG'}, {'name': 'General Emergency', 'guid': '8c8c5abe-e307-4c2c-809c-591220c79ca2', 'description': 'Messages with a status of EMERGENCY or EMER'}, {'name': 'General Error', 'guid': '3f90606c-72d1-4d3d-bb44-91f9aaf0546a', 'description': 'Messages with a status of ERROR or ERR'}, {'name': 'General Information', 'guid': 'bb7a4e8d-cb4c-4d54-813f-4619e707950f', 'description': 'Messages with a status of INFO'}, {'name': 'General Notice', 'guid': 'da712da7-46d0-4986-b349-380b4f4cb748', 'description': 'Messages with a status of NOTICE'}, {'name': 'General Session Information', 'guid': '3b3c3a71-ea88-416e-aa5b-39e8ac13e90a', 'description': 'The message contains general session information.'}, {'name': 'General Warning', 'guid': 'e5c3c4f6-0887-4e11-893c-3232f63181a5', 'description': 'Messages with a status of WARNING or WARN'}, {'name': 'Unassigned', 'guid': '8dd79ade-f1ca-455c-bf90-085af754f162', 'description': 'Default Common Event assigned to messages if no other Common Events are assigned.'}]},
    {'name': 'Access', 'guid': '56717a45-b4af-4867-923b-aa058d2c9eae', 'description': '', 'subclasses': [{'name': 'Access Allowed', 'guid': 'f3cccdd0-0d47-4a2c-9543-b6d37b0bfc3f', 'description': 'Access to a resource was allowed.'}, {'name': 'Access Denied', 'guid': 'd2534a47-9f22-4876-9143-6a7bcc1290e7', 'description': 'Access to a resource was blocked or denied.'}, {'name': 'Access Requested', 'guid': '9b48957e-43e6-4b03-841b-e447faa62d4c', 'description': 'Access to a resource was requested but not necessarily allowed or denied.'}, {'name': 'Access Terminated', 'guid': '18f025d8-7b8b-45cd-8315-7c715a00c34a', 'description': 'Access to a resource was terminated. This implies that access to the object was originally allowed.'}, {'name': 'Kerberos Service Ticket Requested', 'guid': '83094d82-b6c5-4c9d-bc7b-a2585913dabb', 'description': 'A Kerberos Ticket Granting Service (TGS) ticket has been requested. Does not indicate the success or failure of the request.'}, {'name': 'Application Allowed', 'guid': '15075171-81f2-4aab-97cd-85c115149c69', 'description': 'An application has been allowed to execute on the target host.'}, {'name': 'Application Blocked', 'guid': '8c8d9caf-aee8-4d25-8422-8110018cfe08', 'description': 'An application has been prevented from executing on the target host.'}, {'name': 'External Device Allowed', 'guid': 'ca5f4491-820f-4d99-8316-ed5356b837d1', 'description': 'An external device, such as a USB storage device, has been allowed to mount to the target host.'}, {'name': 'External Device Blocked', 'guid': 'ae45322d-e445-4517-a0b5-adfae25bce6e', 'description': 'An external device, such as a USB storage device, has been blocked from mounting on the target host.'}, {'name': 'Token Issued', 'guid': '49c8548c-aa98-462c-9792-5101ad063f90', 'description': 'A token was successfully issued.'}, {'name': 'Token Issuance Failed', 'guid': 'addf8272-0111-47b2-8a96-432c2d432712', 'description': 'A token was failed to be issued.'}]},
    {'name': 'Authentication', 'guid': '0787e28f-71d8-4a1e-9048-71fd61e89a0d', 'description': '', 'subclasses': [{'name': 'General Authentication', 'guid': '655e7aa4-63f0-4ce4-b3c0-c56eff775b5c', 'description': 'Authentication activity was recorded.'}, {'name': 'Authentication Success', 'guid': 'a784ec9c-f6d9-4b73-9e00-f47184b5d1d8', 'description': 'An authentication attempt resulted in success.'}, {'name': 'Authentication Failure', 'guid': '09df6051-9311-41a8-bda9-5a65de2218cf', 'description': 'An authentication attempt resulted in failure.'}, {'name': 'Local Authentication', 'guid': 'd03f8acd-8e6d-4bdb-93d8-82c8017cfe21', 'description': 'An authentication attempt was made to a local resource.'}, {'name': 'Remote Authentication', 'guid': '997f1839-fe65-4da7-b38c-2ccb1caf2344', 'description': 'An authentication attempt was made to a remote resource.'}, {'name': 'Batch Authentication', 'guid': 'f3969b99-44da-4e84-a3b0-a5c2b0d28642', 'description': 'An authentication attempt was made in "batch" mode. This is typically performed by scheduled task operations.'}, {'name': 'Service Authentication', 'guid': '15794150-034a-41bc-a580-5e2933bc3706', 'description': 'An authentication attempt was made by a local service.'}, {'name': 'Admin Rights Granted', 'guid': 'fea39364-057f-4194-98aa-bb85f5881865', 'description': 'Local admin rights were granted to the authenticated or authenticating account.'}, {'name': 'Invalid Account', 'guid': '89925ad7-3c22-48c4-b747-c22978c1467f', 'description': 'An authentication attempt failed due to the account name being invalid.'}, {'name': 'Invalid Password', 'guid': '03e69f7c-ddb5-4169-be09-ed980fb9d251', 'description': 'An authentication attempt failed due to an invalid or wrong password.'}, {'name': 'Unauthorized Origin', 'guid': 'd0412e46-5a2f-4f27-8e0f-2787e7c9ec3c', 'description': 'An authentication attempt failed due to the source system or workstation not being authorized for access.'}, {'name': 'Expired Password', 'guid': '9b9de5c3-5475-4b07-ba33-50d8767fbc18', 'description': 'An authentication attempt failed due to an expired password.'}, {'name': 'Disabled Account', 'guid': 'a6ee2588-b6a0-4928-b8f0-ddbdd3300a25', 'description': 'An authentication attempt failed due to the account being disabled.'}, {'name': 'Expired Account', 'guid': '2fca3ba5-eeda-4c8f-bcce-f26088560d74', 'description': 'An authentication attempt failed due to the account being expired.'}, {'name': 'Password Change Required', 'guid': '7634391d-ff42-4e08-ab1d-63e12ce78883', 'description': 'An authentication attempt failed due to the account needing a password change.'}, {'name': 'Account Logoff', 'guid': 'e7820ffa-d396-40c7-b91b-2e3165bcef4d', 'description': 'An account was logged off.'}, {'name': 'Special Privileges Assigned', 'guid': 'db9f600a-bfd6-4156-9f1b-9ab7b029410e', 'description': 'An account was granted special permissions, excluding admin rights.'}, {'name': 'Time Sync Error', 'guid': 'd00d7a60-5509-483a-b75b-07fdb2691c24', 'description': 'An authentication attempt failed due to the origin and target host times being out of sync.'}]},
    {'name': 'Configuration Management', 'guid': 'e64f048e-570d-4dec-a30f-58c1c4d59e56', 'description': '', 'subclasses': [{'name': 'General Configuration', 'guid': '13d3fb29-ba9b-4f12-8560-a1418db59b43', 'description': 'A configuration event was recorded.'}, {'name': 'Configuration Change Submitted', 'guid': 'fe95876d-80fc-410b-a598-690f2b2cdba4', 'description': 'A configuration change has been submitted and is pending implementation.'}, {'name': 'Configuration Change Successful', 'guid': 'cdadfeb3-b18e-49cd-ba20-e577c85fafc3', 'description': 'A configuration change has been successfully applied.'}, {'name': 'Configuration Change Failed', 'guid': '482679d1-6a3f-4b86-afbb-43886c52987c', 'description': 'A configuration change has failed to take effect.'}, {'name': 'Configuration Change Denied', 'guid': '633a2513-4ea2-4e75-b961-12efba01294a', 'description': 'A configuration change has been denied.'}, {'name': 'System Time Changed', 'guid': 'b0d937c2-8599-4f56-9730-9540ed7fc87a', 'description': 'The time of the local system has been modified.'}, {'name': 'Object Loaded', 'guid': '10a15c70-60b2-4367-b0bd-a0655cec2ad1', 'description': 'An object was loaded into the system or application. This includes actions such as loading or registering packages into the OS or application.'}, {'name': 'Network Interface Down', 'guid': '3c6c7e98-699b-4450-be25-f3e4c0590534', 'description': 'A network interface has been put into the down status.'}, {'name': 'Network Interface Up', 'guid': '9b5274cf-1ec0-4e8a-9d1c-fa0e7fa34048', 'description': 'A network interface has been put into the up status.'}, {'name': 'Domain Trust Created', 'guid': 'fcd5557e-82cf-4cd5-80d4-00ee3628820c', 'description': 'A trust relationship was established between two Domains.'}, {'name': 'Domain Trust Modified', 'guid': 'edc4d0d4-92a0-4d6b-9904-120e793f2637', 'description': 'A trust relationship between two Domains was modified.'}, {'name': 'Domain Trust Removed', 'guid': '4709610c-478f-4174-8250-0d443e667915', 'description': 'A trust relationship was removed between two Domains.'}, {'name': 'Configuration Deleted', 'guid': '9db1e519-f164-4a28-8fce-67212995a366', 'description': 'A configuration deleted event was recorded.'}, {'name': 'Configuration Enabled', 'guid': 'e282ab28-b097-448c-9cce-666f08ab582f', 'description': 'A configuration enabled event was recorded.'}, {'name': 'Configuration Disabled', 'guid': '489c44d5-3b2f-41d3-80d3-a702d48c0540', 'description': 'A configuration disabled event was recorded.'}, {'name': 'Missing Data', 'guid': 'a0515dd5-abe5-46b7-839b-1d1a76afaebd', 'description': 'Missing data was observed.'}, {'name': 'Invalid Data', 'guid': '41f56937-37e3-4b6f-bf5f-06a6e3e9ee8f', 'description': 'Invalid data was observed.'}]},
    {'name': 'IAM', 'guid': '78344f03-a536-455a-96ec-1c1d24e233bd', 'description': '', 'subclasses': [{'name': 'Account Added to Group', 'guid': '1ea555bb-e9a3-4c79-9fa3-9a583242fe8c', 'description': 'An account was added to a specified group.'}, {'name': 'Account Created', 'guid': '83937455-69c4-476c-825f-14e4a7944255', 'description': 'An account was created.'}, {'name': 'Account Deleted', 'guid': 'b49e2331-aeb9-4b2f-837f-528d6793bcec', 'description': 'An account was deleted.'}, {'name': 'Account Disabled', 'guid': '4a9479a0-3c5c-4fd6-9b70-92104791badb', 'description': 'An account was disabled.'}, {'name': 'Account Enabled', 'guid': 'e7e1c6cf-45e7-416d-aedf-229bf6b0e940', 'description': 'An account was enabled.'}, {'name': 'Account Locked', 'guid': 'd6870faa-b1c4-4a74-9327-ceacb4d68f90', 'description': 'An account was locked.'}, {'name': 'Account Modified', 'guid': 'eb1c3075-feec-4bab-81d7-9bb30ce59eb0', 'description': 'An account or an attribute of an account object was modified.'}, {'name': 'Account Modification Failed', 'guid': 'abe2ed03-b262-4b5f-a07b-57254cf750e2', 'description': 'An attempt to modify an account object failed.'}, {'name': 'Account Removed from Group', 'guid': 'd8b9893a-afaa-4ddf-ab0c-081cfff93de3', 'description': 'An account was removed from a specific group.'}, {'name': 'Account Unlocked', 'guid': '92f1b539-7894-40eb-9636-3e3e5f6c52c2', 'description': 'An account was unlocked.'}, {'name': 'Group Created', 'guid': 'db7c6007-0493-4155-a7cd-8033a6aa574c', 'description': 'A group was created.'}, {'name': 'Group Deleted', 'guid': '678fcbd9-e3b0-455a-a9c4-a9510bc87551', 'description': 'A group was deleted.'}, {'name': 'Group Modified', 'guid': '66e31c41-8429-45e0-b407-533144276db1', 'description': 'A group, or an attribute of a group object, was modified. Does not include membership changes.'}, {'name': 'Password Modified', 'guid': '1bd270af-4661-41f9-a2ee-25b2bec391a6', 'description': 'The password of an account was successfully modified.'}, {'name': 'Password Change Failed', 'guid': '6ff6dac1-782d-4699-894b-73262f69f378', 'description': "An attempt to modify/change/reset an account's password failed."}, {'name': 'Permissions Added', 'guid': '4d3a3eaa-9d23-4713-a438-69e001e6c745', 'description': 'Permissions were added to an account.'}, {'name': 'Permissions Modified', 'guid': 'e2b1b144-2ffa-4f21-93eb-2f101e72ae73', 'description': 'Permissions were modified on an account.'}, {'name': 'Permissions Removed', 'guid': '59feb021-f360-434f-acca-52812c32310a', 'description': 'Permissions were removed from an account.'}, {'name': 'General Account Info', 'guid': '73805139-8d01-4f41-8f23-9f82b589cc0e', 'description': 'Contains general information about an account.'}, {'name': 'Role Created', 'guid': '69f274c8-b90e-4fd3-843c-e4ec269856aa', 'description': 'A role was created.'}, {'name': 'Role Modified', 'guid': 'c18e8794-1a8d-45d5-9690-f2900dcb83f4', 'description': 'A role was modified.'}, {'name': 'Role Deleted', 'guid': '49a3e174-b9fa-45f7-a24d-445a8debf0f6', 'description': 'A role was deleted.'}, {'name': 'Role Assigned', 'guid': 'b12fca6e-c0e4-439c-9e8f-eedb1fff53eb', 'description': 'A role was assigned to an account.'}, {'name': 'Role Removed', 'guid': '51e8bfad-b809-4894-a57c-b0f84de44b31', 'description': 'A role was removed from an account.'}, {'name': 'Account Compromised', 'guid': '297a26a3-9715-4adf-bd78-369a3e3d25bb', 'description': 'The account was compromised.'}]},
    {'name': 'Network', 'guid': 'ca8aeaf7-a68d-4b85-b569-8049f97d0e28', 'description': '', 'subclasses': [{'name': 'IPSec Negotiation Failed', 'guid': '54c96196-ad9b-4605-b28b-038e22ea696f', 'description': 'An IPSec tunnel negotiation failed'}, {'name': 'IPSec SA Ended', 'guid': 'e70b176b-7429-4db1-87ea-e9a4b99537cf', 'description': 'An IPSec Security Association ended.'}, {'name': 'IPSec SA Created', 'guid': '896f61ff-1e2e-4569-8eb1-8052a5140695', 'description': 'An IPSec Security Association was successfully created.'}, {'name': 'IPSec SA Deleted', 'guid': 'f6848565-9617-4d5c-b1da-b6233b3ca787', 'description': 'An IPSec Security Association was deleted.'}, {'name': 'General IPSec Info', 'guid': '93fcc219-08fc-418f-aa9a-38d0ca4e7b9e', 'description': 'General IPSec information not directly indicating the creation, deletion, or termination of Security Associations or other aspects of establishing and closing IPSec tunnels.'}, {'name': 'Network Session Started', 'guid': '5d939cff-6f45-47f2-932a-69998ef18c37', 'description': 'A network session has started.'}, {'name': 'Network Session Terminated', 'guid': '2de78fa5-b2d8-4b7e-8523-0eecce1c9fc7', 'description': 'A network session has ended without error.'}, {'name': 'Network Traffic Allowed', 'guid': '6331fb60-005b-41f1-b701-2fd6c09d971e', 'description': 'Network traffic was allowed by a security control.'}, {'name': 'Network Traffic Denied', 'guid': '9a78940e-8298-4003-8058-490ca891ff48', 'description': 'Network traffic was blocked by a security control.'}, {'name': 'DNS Query', 'guid': 'abff8bfe-2f68-454e-a686-a3c5170069ca', 'description': 'A DNS Query has returned successfully.'}, {'name': 'DNS Query Failed', 'guid': 'bd7b3dd5-0259-4232-a0b3-8c009aec0ec4', 'description': 'A DNS Query attempt has failed.'}, {'name': 'General Network Traffic', 'guid': 'c454770b-e13b-413f-bca6-82ea65a93054', 'description': 'General network traffic that does not indicate the start/end of a session or an allow/deny response action.'}, {'name': 'DHCP Lease Renewed', 'guid': 'd8e03b0a-f8bc-46a1-9cae-28cc72a50300', 'description': 'An IP address assigned to a host via DHCP has had its lease renewed.'}, {'name': 'DHCP Lease Issued', 'guid': 'e75e3caf-b308-4513-b973-e6021b09fb33', 'description': 'An IP address has been assigned to a host through DHCP.'}, {'name': 'Firewall Service Error', 'guid': '96855cb1-e7ae-4a29-bcfa-badbb38ae93a', 'description': 'An Error in the firewall service.'}, {'name': 'Failed Denial Of Service', 'guid': 'a5a7dabd-bb86-446e-8f0c-0f90b28b787b', 'description': 'Failed Denial of service message.'}, {'name': 'IPSEC Service Failed', 'guid': '6a6cd6dc-c30c-4e32-8f6b-5f4d1aa78b7b', 'description': 'The IPSEC service was failed.'}]},
    {'name': 'Object Management', 'guid': '4c273f57-e9f9-45d4-affb-ae706107f2c5', 'description': '', 'subclasses': [{'name': 'Certificate Issued', 'guid': '3139030b-9b5e-429c-bf9a-881d25fd3d12', 'description': 'A Certificate has been issued by the Certification Authority.'}, {'name': 'Certificate Request Denied', 'guid': '8d19557c-efa6-45da-a49e-a24622ff2e84', 'description': 'The Certification Authority has denied the request for Certificate signing.'}, {'name': 'Certificate Request Pending', 'guid': '9eddd627-8cb8-44d5-b4a7-254d95dfd57d', 'description': 'A Certificate Signing Request (CSR) is currently pending action by a Certification Authority.'}, {'name': 'Certificate Request Received', 'guid': '705a8dff-5aa2-4cc2-b06a-738d9a312f5a', 'description': 'A Certificate Signing Request (CSR) has been received by a Certification Authority.'}, {'name': 'Certificate Revoked', 'guid': 'e4b8b14d-797d-4bcb-b0a5-f0d92284477f', 'description': 'A Certificate has been revoked, and made invalid, by the Certification Authority.'}, {'name': 'Object Attribute Modified', 'guid': '5dc33b63-2159-4e47-a269-a050834d904d', 'description': "Message indicates that an attribute of a specific object or objects were modified. Does not include modifying the object's name or the permissions assigned to the object."}, {'name': 'Object Created', 'guid': 'b5f1a137-b926-45b3-bce0-69b9657116f5', 'description': 'An object was created.'}, {'name': 'Object Deleted', 'guid': 'c291ca27-ab66-41bd-9cdf-47be9963ba12', 'description': 'An object was deleted.'}, {'name': 'Object Modified', 'guid': 'b9684015-78e8-4cf0-8989-158e005510de', 'description': 'An object was modified.'}, {'name': 'Object Permissions Modified', 'guid': 'aceab2d2-90c1-4225-a244-b2f9d9e6dbfa', 'description': 'The permissions on an object were modified.'}, {'name': 'Registry Value Modified', 'guid': '49f2153d-8678-4acb-b050-ad237278b3c4', 'description': 'A Windows registry value was modified.'}, {'name': 'Scheduled Task Created', 'guid': '8b32afa3-e543-43f3-8b59-9d60e0270d85', 'description': 'A scheduled task was created. Examples of this include Windows Scheduled Tasks and *nix cron jobs.'}, {'name': 'Scheduled Task Deleted', 'guid': '5d2762c5-24f6-4078-a1a1-4c65fb639351', 'description': 'A scheduled task was deleted. Examples of this include Windows Scheduled Tasks and *nix cron jobs.'}, {'name': 'Scheduled Task Modified', 'guid': 'ad8de264-313b-45f5-8652-a0ce9e4edf95', 'description': 'A scheduled task eas modified. Examples of this include Windows Scheduled Tasks and *nix cron jobs.'}, {'name': 'Scheduled Task Disabled', 'guid': '77b65825-3a92-4469-ae86-95f165ae72ee', 'description': 'A scheduled task was disabled. Examples of this include Windows Scheduled Tasks and *nix cron jobs.'}, {'name': 'Scheduled Task Enabled', 'guid': '85e02b36-8007-445b-9e81-aaf359c8fe8c', 'description': 'A scheduled task was enabled. Examples of this include Windows Scheduled Tasks and *nix cron jobs.'}, {'name': 'Object Handle Closed', 'guid': '53852afa-1671-437e-a91f-11d9346b2b7d', 'description': 'A handle to an object is closed.'}, {'name': 'Object Read', 'guid': 'cae04c18-5607-4114-b826-80a22081e196', 'description': 'A read operation has been performed on an object.'}, {'name': 'Object Replicated', 'guid': 'c914061a-a75e-4f8a-9a66-286d1aeed1fe', 'description': 'Attributes of an object were replicated.'}, {'name': 'Object Listed', 'guid': 'e9808d4d-cee8-436c-b7ab-b1590dac7a7b', 'description': 'An object was listed.'}, {'name': 'Object Not Applied', 'guid': 'fc8a6977-71dd-4a43-9a80-5c44a7095517', 'description': 'An object was not applied.'}, {'name': 'Request Blocked', 'guid': '04a96565-8577-4b48-9309-a8968f331e2e', 'description': 'A request was blocked.'}, {'name': 'Object Virtualized', 'guid': '7270e348-8ec8-4b4b-bc8c-cfd6edad31a5', 'description': 'An object was Virtualized.'}, {'name': 'Object Restored', 'guid': '07f7746e-b617-4936-83d8-e9bc7522c880', 'description': 'An object was restored.'}, {'name': 'Object Added', 'guid': 'b0ded045-6964-4f09-a4a6-1faa64cc95f0', 'description': 'An object was added.'}, {'name': 'Object Load Failed', 'guid': 'd3f6f048-dcf6-4097-830e-5c1b4777df00', 'description': 'An object loading failed.'}]},
    {'name': 'Policy management', 'guid': 'e574cf19-000d-43d4-b41d-57ba4f009766', 'description': '', 'subclasses': [{'name': 'General Policy Management', 'guid': '8266ddb3-5e20-4ab5-93ec-d0db5a363d17', 'description': 'Describes general policy management activities.'}, {'name': 'Policy Created', 'guid': 'c8adbf86-d026-4d3b-bfcf-3bf884bcfe98', 'description': 'A policy object was created.'}, {'name': 'Policy Modified', 'guid': '8e152428-3ef7-4173-88bd-59346444b428', 'description': 'A policy object was modified.'}, {'name': 'Policy Assigned', 'guid': 'aae10cdd-04d7-4796-90f8-79300b45a519', 'description': 'A policy object was assigned to one or more targets.'}, {'name': 'Policy Removed', 'guid': '83429163-9619-4f87-bca1-62ae78b46950', 'description': 'A policy was removed or disassociated from one or more targets.'}, {'name': 'Policy Enabled', 'guid': 'b7485aff-3a31-4379-963f-fa5fbdba587f', 'description': 'A policy object was enabled.'}, {'name': 'Policy Disabled', 'guid': '5fdb26ea-2c19-4106-941d-795302583d37', 'description': 'A policy object was disabled.'}, {'name': 'Policy Deleted', 'guid': 'bc7566b8-d0b5-4c1c-926a-b1fcc953c9e6', 'description': 'A policy object was deleted.'}]},
    {'name': 'Software Management', 'guid': '4f2888b5-4916-40e6-9b71-22fc584a3ce0', 'description': '', 'subclasses': [{'name': 'Software Updated', 'guid': '7283c2cf-4763-47d0-b4ad-b2924810a4a2', 'description': 'An application or software update was completed successfully. This does not include signature updates.'}, {'name': 'Software Update Failed', 'guid': 'a0aa0078-8a8b-40a4-b1c3-e15abbe92796', 'description': 'An application or software update failed.'}, {'name': 'Software Installed', 'guid': 'aab52380-424a-4856-af5b-47fd920258d7', 'description': 'An application or software installation was completed successfully.'}, {'name': 'Software Install Failed', 'guid': '91c2ccca-7520-484a-a6ab-73766d209d59', 'description': 'An application or software installation failed.'}, {'name': 'Software Uninstalled', 'guid': '05ad4cae-6e9e-4df8-ae6b-a0b50a8eeaa3', 'description': 'An application or software was uninstalled.'}, {'name': 'Service Installed', 'guid': 'fd8051d5-ffcb-47f0-a5d5-4c2e814b46bc', 'description': 'A service or daemon was successfully installed.'}, {'name': 'Signature Update Successful', 'guid': 'b3099cda-6d90-41c4-a398-d720ae13ec60', 'description': 'A signature update attempted by an application or device succeeded.'}, {'name': 'Signature Update Failed', 'guid': '0b423b0e-ad14-40b8-83a8-a7ab9a01df88', 'description': 'A signature update attempted by an application or device failed.'}, {'name': 'Update Not Needed', 'guid': '23399934-62b0-40cc-86ef-cc65b675fd91', 'description': 'An update check was performed against an application, software, or software component (including signatures) and an update is not required.'}]},
    {'name': 'Status', 'guid': '8534ab1a-fb51-4db0-96a6-35a6cb1ad914', 'description': '', 'subclasses': [{'name': 'Service Stopped', 'guid': '9016ee01-665f-4cbe-83e4-968b0afe89c8', 'description': 'A service or daemon has been stopped or terminated and is no longer actively running.'}, {'name': 'Service Started', 'guid': '1901050b-700e-4679-9cbd-8f8ced3607e5', 'description': 'A service or daemon has started.'}, {'name': 'Log Cleared Successfully', 'guid': '7155d0de-70f0-4e9e-8438-dc0ff1829c23', 'description': 'A log file has been deleted or has had its content erased.'}, {'name': 'Log Full', 'guid': 'd1fd11cd-f653-441a-877f-1f770c26ccd7', 'description': 'A log file has reached the capacity allocated by the system or governing policy.'}, {'name': 'Backup Completed', 'guid': 'b8d941ee-7d48-4337-b3dc-ceec746cd052', 'description': 'A backup operation has been completed successfully.'}, {'name': 'System Started', 'guid': '17b3738d-e330-46cf-9b8c-a36f27d217bb', 'description': 'A system or host has started.'}, {'name': 'System Shutdown', 'guid': '13b5b251-57be-4806-ae25-e214f72bf305', 'description': 'A system or host has, or is being shut down.'}, {'name': 'Auditing Error', 'guid': '9a41f682-4b06-45f9-a10c-5224bfbed475', 'description': 'An error was encountered during the auditing or logging process.'}, {'name': 'Process Started', 'guid': '338659f4-28a7-48ee-a737-79f8de69382e', 'description': 'A process was started on a host system.'}, {'name': 'Process Stopped', 'guid': '27de9d15-3e75-44de-ab34-da34da8ec1dc', 'description': 'A running process was stopped/terminated on a host system.'}, {'name': 'General Health Information', 'guid': 'e9cb43af-1caa-4eac-8437-c68daf1e16ed', 'description': 'The message contains general health information.'}, {'name': 'General Performance Information', 'guid': 'c0554b52-f0a5-4816-8e26-e3fe36f1cde7', 'description': 'The message contains general performance information.'}, {'name': 'Backup Failed', 'guid': '63cd54b5-0443-42fd-a2e0-5178facc7d79', 'description': 'A backup operation failed to complete.'}, {'name': 'Restore Completed', 'guid': 'dafc94fe-c451-4929-830e-327b40aa4a27', 'description': 'A restore operation, typically from a backup, was completed successfully.'}, {'name': 'Restore Failed', 'guid': '54e61e75-def3-4428-bd8b-3fb14b9245a7', 'description': 'A restore operation failed to complete.'}, {'name': 'Scheduled Task Ended', 'guid': '18a852b5-e3d8-4b82-aa1f-0aa73f05a2b9', 'description': 'A scheduled task or job has ended/stopped.'}, {'name': 'Scheduled Task Started', 'guid': '094ba1ea-db11-4235-bba9-4d0cf58cd727', 'description': 'A scheduled task or job has started.'}, {'name': 'Script Execution', 'guid': 'd840973d-a052-4823-a07e-dad5dadd8b30', 'description': 'A script, such as a PowerShell script, is being executed on the system.'}, {'name': 'Scan Completed', 'guid': '119881ca-f7c2-4831-b9b2-ca48adc45fe4', 'description': 'A security control has successfully completed a scan of a device, system, or application.'}, {'name': 'Scan Failed', 'guid': '97136bee-0f75-4e30-a11d-37337882ab1e', 'description': 'A security control scan action failed.'}, {'name': 'Scan Paused', 'guid': 'bb28c1c4-b3dc-4243-a8e0-76835892db16', 'description': 'A security control scan has been paused.'}, {'name': 'Scan Started', 'guid': '3ab26438-192a-41d1-a2ab-1f8de118c336', 'description': 'A security control has started a scan of a device, system, or application.'}, {'name': 'Scan Stopped', 'guid': '84ecc7b5-5434-464a-92a3-3a596f039d03', 'description': 'A scan initiated by a security control has stopped.'}, {'name': 'General Backup Information', 'guid': '5c3ee836-49c0-4c18-9e4d-6fc10e757f8a', 'description': 'Messages describe high-level activity related to backups.'}, {'name': 'Device Inserted', 'guid': 'b26036a0-8873-466a-baf6-68fea9305553', 'description': 'A new device has been inserted into the system.'}, {'name': 'Device Removed', 'guid': '4d525bb9-e89c-450c-bb56-fd4c00c46433', 'description': 'A device has been removed/ejected from a system.'}, {'name': 'Device Initialized', 'guid': '7314ec7d-33bb-4088-a055-807fef473ad7', 'description': 'A device has been initialized on a system.'}, {'name': 'Package loaded', 'guid': '107a683d-069a-4444-8468-62695f90e74c', 'description': 'A package/DLL has been loaded by Windows service.'}, {'name': 'System Time Changed', 'guid': '49349df1-4862-4e90-951f-fd3c9a52f416', 'description': 'System time was changed.'}, {'name': 'Token Assigned', 'guid': '23bb016c-2bb0-4b8b-9f91-22e8f013365f', 'description': 'A token was assigned to process.'}, {'name': 'Privilege Assigned', 'guid': 'e7f9a5ce-c5a4-46d9-a38a-6e7191304f94', 'description': 'Privileged access was granted to an account.'}, {'name': 'Privilege Revoked', 'guid': '0b196902-2b65-4c47-87fa-a2d247bcc02f', 'description': 'Privileged access was revoked from an account.'}, {'name': 'Integrity Violation', 'guid': 'f7cd97ea-c652-46d0-80f7-0026ac1789d5', 'description': 'Integrity violation event was recorded.'}, {'name': 'CRL Published', 'guid': '758d3fe4-1fe6-49bf-b935-d48fe1be160c', 'description': 'Certificate Revocation List (CRL) was published by Certificate Services.'}, {'name': 'Key Retrieved', 'guid': '7b8e00fe-6625-48e5-a05f-0dbf537ebce8', 'description': 'A key was retrieved by Certificate Services.'}, {'name': 'Certificate Imported', 'guid': 'fd8c64de-49cc-488d-9dfb-a935f294677a', 'description': 'A Certificate was imported by Certificate Services.'}, {'name': 'Key Archived', 'guid': 'b3fc99f3-b00f-4458-8c39-bf04b1e6494e', 'description': 'A key was archived by Certificate Services.'}, {'name': 'Key Imported', 'guid': '7e22f8c8-0efb-4e08-a072-e86658b1e5bc', 'description': 'Key was imported by Certificate Services.'}, {'name': 'Certificate Published', 'guid': 'b7a80d1c-3af9-4980-a6ad-dfe5c793de41', 'description': 'CA certificate was published by Certificate Services.'}, {'name': 'Group Assigned', 'guid': 'b57df143-2e20-41c5-a16b-71e5fef7a73a', 'description': 'A group was assigned to an object.'}, {'name': 'Audit Failure', 'guid': 'ec1af324-d785-4e50-9889-c89afa894315', 'description': 'Audit failure event was recorded.'}, {'name': 'Service Aborted', 'guid': '8d86c6a4-47e5-4195-975e-2a33314d47ea', 'description': 'Services Stopped abnormally.'}, {'name': 'Cryptographic Operation', 'guid': '969f5084-d4c0-4890-bb52-74976d20a846', 'description': 'General Cryptographic Operation.'}, {'name': 'Cryptographic Failure', 'guid': '62b5cc2f-0f8f-40d2-8920-67620ee1d4ac', 'description': 'Cryptographic Operation Failure.'}, {'name': 'Registration Complete', 'guid': '260fbca0-dbbb-4f2e-a206-53196df9c9b2', 'description': 'An registration was completed successfully.'}, {'name': 'Registration Failure', 'guid': '58ff3453-f8c2-4f9c-aa9e-2d89c09f4ba7', 'description': 'The registration was failed.'}, {'name': 'New Device Found', 'guid': '7af8aba8-b44a-4071-9537-fe79ae0e635d', 'description': 'The new device was found.'}, {'name': 'Hardware Installed', 'guid': 'b92cba75-f02e-4965-9751-28a540e215ee', 'description': 'An hardware installation was completed successfully.'}, {'name': 'Request Failed to Validate', 'guid': '082bbdcb-eb03-4270-a877-6d4846e687b7', 'description': 'The request was not validated'}, {'name': 'Process Completed', 'guid': '3ff59145-136b-44e8-b128-1997cf05d8da', 'description': 'The process completed successfully.'}, {'name': 'Request Validated', 'guid': 'f54e4573-08db-47ee-acaa-a0ea885b38df', 'description': 'A request was validated successfully.'}]},
    {'name': 'Threat Detection', 'guid': '348a37e6-590e-4767-baae-a5c3951391ae', 'description': '', 'subclasses': [{'name': 'General Threat Detected', 'guid': '28de4ee0-ca58-40f5-9ac7-ca38edf7883a', 'description': 'A security control has identified a threat. This is meant to be a general category for detections that do not fit another more specific category. This detection was not blocked by the control.'}, {'name': 'Threat Blocked', 'guid': '48d2b046-301a-420f-9f33-75e3a097edd6', 'description': 'A security control has identified and blocked a threat.'}, {'name': 'Threat Allowed', 'guid': '02bb433e-6edb-47bc-ae4a-61cbae2a51be', 'description': 'A security control has identified a threat, but did not block or prevent it.'}, {'name': 'Threat Allowed by User', 'guid': '6f3db23f-3a61-4728-9480-c1b70ecfe34b', 'description': 'A security control identified and blocked a threat but that block was overridden by user action.'}, {'name': 'Threat Quarantined', 'guid': '9748aec9-b045-4db2-8760-b9a9759f7083', 'description': 'A security control has identified and quarantined a threat.'}, {'name': 'Host Quarantined', 'guid': '1b4e3c2d-f7ac-4e31-af8b-4ae3d77b71f9', 'description': 'A security control has quarantined, or contained, a host.'}, {'name': 'Host Quarantine Removed', 'guid': 'ca8eb1de-baf4-4ce9-b04b-838539c3c6fb', 'description': 'A previously quarantined host has had the quarantine lifted.'}, {'name': 'General Detection Information', 'guid': '152a7435-dd69-4034-87a5-ff38f86c5fb0', 'description': 'A security control is reporting on the status of an alert, case, or detection produced by that control.'}, {'name': 'Detection Updated', 'guid': '8a2f825b-253f-4b2f-9ffc-441285bafec8', 'description': 'A security control has updated the status or details of an alert, case, or detection. This is typically done by a user.'}, {'name': 'Watchlist Hit', 'guid': 'c7fe5346-0601-4659-a03c-ebbd8f84c883', 'description': 'A security control has detected a file, process, other object, or behavior that matches a watchlist.'}, {'name': 'Suspicious Activity', 'guid': 'dfeb1ad8-0b54-4759-a07a-4fc7dd9a4fc4', 'description': 'An abnormal activity has been detected.'}]},
]

# Dict to define what AIE block types are supported by this integration
SupportedBlockTypes = {
    'LogObserved': 1,
    'ThresholdObserved': 4,
    'UniqueValuesObserved': 7,
}

# Mapping between AIE block types and AXON block types, when more support is added in Axon, this dict will be updated
aie_block_types_to_axon_block_types = {
    'LogObserved': 'LOG_OBSERVED',
    'ThresholdObserved': 'COUNT_THRESHOLD_OBSERVED',
    'UniqueValuesObserved': 'COUNT_UNIQUE_VALUES_OBSERVED',
}

# Define the default common event for the case that the NPL model does not return a common event
axon_default_common_event = ["28de4ee0-ca58-40f5-9ac7-ca38edf7883a", "348a37e6-590e-4767-baae-a5c3951391ae"]

# Mapping between AXON fields and LR7 Fields. All unattributed fields and observer fields have been added to the target
# Or the Origin (Host, Identity, etc.), program must determinate if skip them or use them
axon_mdi_mapping = {
    # Application Tab
    'Action': 'action.command',
    'Amount': 'SKIP_FIELD',  # TODO: Validate
    'Command': 'action.command',
    'Hash': ['unattributed.hash.md5', 'unattributed.hash.sha1', 'unattributed.hash.sha256', 'unattributed.hash.sha512',
             'object.email_message.file.hash.md5', 'object.email_message.file.hash.sha1',
             'object.email_message.file.hash.sha256', 'object.email_message.file.hash.sha512', 'object.file.hash.md5',
             'object.file.hash.sha1', 'object.file.hash.sha256', 'object.file.hash.sha512', 'object.process.hash.md5',
             'object.process.hash.sha1', 'object.process.hash.sha256', 'object.process.hash.sha512',
             'object.process.parent_process.hash.md5', 'object.process.parent_process.hash.sha1',
             'object.process.parent_process.hash.sha256', 'object.process.parent_process.hash.sha512'],
    'Known Application': 'action.network.application',
    'Application': 'action.network.application',
    'Protnum': 'action.network.protocol.id',
    'Protname': 'action.network.protocol.name',
    'Object': ['object.registry_object.key', 'object.registry_object.root_key', 'object.policy.group',
               'object.interface.alias', 'object.file.type', 'object.email_message.file.name'],
    'Object Name': ['object.database.name', 'object.database.table.name', 'object.database.instance_name',
                    'object.device.name', 'object.device.vendor_name', 'object.directory_object.name',
                    'object.domain.name', 'object.file.name'],
    'ObjectName': ['object.database.name', 'object.database.table.name', 'object.database.instance_name',
                   'object.device.name', 'object.device.vendor_name', 'object.directory_object.name',
                   'object.domain.name', 'object.file.name'],
    'Object Type': 'object.type',
    'ObjectType': 'object.type',
    'Parent Process ID': 'object.process.parent_process.id',
    'ParentProcessID': 'object.process.parent_process.id',
    'Parent Process Name': 'object.process.parent_process.name',
    'ParentProcessName': 'object.process.parent_process.name',
    'Parent Process Path': 'object.process.parent_process.path',
    'ParentProcessPath': 'object.process.parent_process.path',
    'Policy': 'object.policy.name',
    'Process ID': 'object.process.id',
    'ProcessID': 'object.process.id',
    'Process Name': 'object.process.name',
    'Process': 'object.process.name',
    'Quantity': 'SKIP_FIELD',  # TODO: Validate
    'Rate': 'SKIP_FIELD',  # TODO: Validate
    'Reason': 'action.result.reason',
    'Response Code': 'action.result.code',
    'ResponseCode': 'action.result.code',
    'Result': 'action.result.message',
    'Session': ['observer.account.session.id', 'action.session.id', 'action.authentication.admin_session',],
    'Session Type': ['observer.account.session.type', 'action.session.type'],
    'SessionType': ['observer.account.session.type', 'action.session.type'],
    'Size': ['action.authentication.key_size', 'object.email_message.file.size', 'object.file.size',
             'object.script.size'],
    'Status': ['object.file.signature.status', 'object.process.signature.status',
               'object.process.parent_process.signature.status', 'threat.run_status',],
    'Subject': ['object.certificate.subject', 'object.email_message.subject'],
    'URL': 'object.url.complete',
    'User Agent': 'action.user_agent',
    'UserAgent': 'action.user_agent',
    'Version': ['object.file.version', 'origin.host.os.version', 'target.host.os.version', 'origin.host.version'
                'target.host.version', 'observer.host.os.version', 'observer.host.version'],
    # Kbytes Tab
    'Host (Impacted) Kbytes Sent': 'action.network.byte_information.sent',
    'BytesIn': 'action.network.byte_information.sent',
    'Host (Impacted) Kbytes Rcvd': 'action.network.byte_information.received',
    'BytesOut': 'action.network.byte_information.received',
    'Host (Impacted) Kbytes Total': 'action.network.byte_information.total',
    'Bytes': 'action.network.byte_information.total	',
    'Host (Impacted) Packets Rcvd': 'action.network.packet_information.received',
    'PacketsIn': 'action.network.packet_information.received',
    'Host (Impacted) Packets Sent': 'action.network.packet_information.sent',
    'PacketsOut': 'action.network.packet_information.sent',
    'Host (Impacted) Packets Total': 'action.network.packet_information.total',
    'Packets': 'action.network.packet_information.total',
    # Classification Tab
    'Classification': 'general_information.common_event',
    'Common Event': 'general_information.common_event',
    'CommonEvent': 'general_information.common_event',
    'Priority': 'SKIP_FIELD',  # TODO: Validate
    'Direction': 'action.network.direction',
    'CVE': 'threat.cve',
    'Severity': ['vendor_information.severity', 'threat.severity'],
    'Threat ID': 'threat.id',
    'ThreatID': 'threat.id',
    'Threat Name': 'threat.name',
    'ThreatName': 'threat.name',
    'Vendor Info': 'vendor_information.description',
    'VendorInfo': 'vendor_information.description',
    'Vendor Message ID': 'vendor_information.id',
    'VMID': 'vendor_information.id',
    # Host Tab
    'Host (Origin or Impacted)': ['unattributed.host.name', 'unattributed.host.ip_address.value',
                                  'origin.host.ip_address.value', 'target.host.ip_address.value', 'origin.host.name',
                                  'target.host.name', 'observer.host.ip_address.value', 'observer.host.name'],
    'Host (Impacted)': ['unattributed.host.name', 'unattributed.host.ip_address.value', 'target.host.ip_address.value',
                        'target.host.name', 'observer.host.ip_address.value', 'observer.host.name'],
    'IP Address (Impacted)': ['unattributed.host.ip_address.value', 'target.host.ip_address.value',
                              'observer.host.ip_address.value'],
    'DIP': ['unattributed.host.ip_address.value', 'target.host.ip_address.value', 'observer.host.ip_address.value'],
    'DName': ['unattributed.host.name', 'target.host.name', 'observer.host.name'],
    'Interface (Impacted)': 'target.host.interface.name',
    'DInterface': 'target.host.interface.name',
    'MAC Address (Impacted)': 'target.host.mac_address',
    'DMAC': 'target.host.mac_address',
    'NAT IP Address (Impacted)': 'target.host.ip_address.nat_value',
    'DNATIP': ['target.host.ip_address.nat_value', 'observer.host.ip_address.nat_value'],
    'Host (Origin)': ['origin.host.name', 'observer.host.name', 'unattributed.host.name'],
    'IP Address (Origin)': ['origin.host.ip_address.value', 'observer.host.ip_address.value',
                            'unattributed.host.ip_address.value'],
    'SIP': ['origin.host.ip_address.value', 'observer.host.ip_address.value', 'unattributed.host.ip_address.value'],
    'SName': ['origin.host.name', 'observer.host.name', 'unattributed.host.name'],
    'Interface (Origin)': 'origin.host.interface.name',
    'SInterface': 'origin.host.interface.name',
    'MAC Address (Origin)': 'origin.host.mac_address',
    'SMAC': 'origin.host.mac_address',
    'NAT IP Address (Origin)': ['origin.host.ip_address.nat_value', 'observer.host.ip_address.nat_value'],
    'SNATIP': ['origin.host.ip_address.nat_value', 'observer.host.ip_address.nat_value'],
    'Hostname (Origin)': ['origin.host.name', 'observer.host.name', 'unattributed.host.name'],
    'Hostname (Impacted)': ['target.host.name', 'observer.host.name', 'unattributed.host.name'],
    'Known Host (Origin)': 'SKIP_FIELD',  # TODO: Validate unattributed.host.identity.name for future use
    'Known Host (Impacted)': 'SKIP_FIELD',  # TODO: Validate unattributed.host.identity.name for future use
    'Serial Number': ['origin.host.serial_number', 'target.host.serial_number', 'observer.host.serial_number',
                      'object.certificate.serial_number', 'object.device.serial_number'],
    'SerialNumber': ['origin.host.serial_number', 'target.host.serial_number', 'observer.host.serial_number',
                     'object.certificate.serial_number', 'object.device.serial_number'],
    # Identity Tab
    'User (Impacted)': 'target.account.name',
    'Account': 'target.account.name',
    'Group': 'object.group.name',
    'User (Origin)': 'origin.account.name',
    'Login': 'origin.account.name',
    'Origin Login': 'origin.account.name',
    'User (Origin or Impacted)': ['origin.account.name', 'target.account.name'],
    'Recipient': 'target.account.email_address',
    'Sender': 'origin.account.email_address',
    # Location Tab
    'Entity (Origin)': 'SKIP_FIELD',  # TODO: Validate
    'Entity (Impacted)': 'SKIP_FIELD',  # TODO: Validate
    'Zone (Origin)': 'SKIP_FIELD',  # TODO: Validate
    'Zone (Impacted)': 'SKIP_FIELD',  # TODO: Validate
    'Location (Origin)': ['origin.host.location.geo_location', 'origin.host.location.city',
                          'origin.host.location.region'],
    'Location (Impacted)': ['target.host.location.geo_location', 'target.host.location.city',
                            'target.host.location.region'],
    'Country (Origin)': 'origin.host.location.country',
    'Country (Impacted)': 'target.host.location.country',
    # Log Tab
    'Log Source Type': 'general_information.log_source.type_name',
    'LogSourceType': 'general_information.log_source.type_name',
    'Log Source Entity': 'SKIP_FIELD',  # TODO: Validate
    'LogSourceEntity': 'SKIP_FIELD',  # TODO: Validate
    'Log Source Host': 'general_information.transit_path.collector_id',
    'LogSourceHost': 'general_information.transit_path.collector_id',
    'Log Source': 'general_information.log_source.name',
    'LogSource': 'general_information.log_source.name',
    # Network Tab
    'Network (Origin)': 'SKIP_FIELD',  # TODO: Validate
    'Network (Impacted)': 'SKIP_FIELD',  # TODO: Validate
    'Protocol': 'action.network.protocol.name',
    # Observer and target Domains doesn't have a .name suffix in AXON Documentation. Maybe a mistake
    # TODO: Validate this possible Documentation Error
    'Domain (Origin)': ['object.domain.name', 'object.url.domain', 'origin.account.domain', 'observer.account.domain',
                        'origin.host.domain.name', 'observer.host.domain'],
    'DomainOrigin': ['object.domain.name', 'object.url.domain', 'origin.account.domain', 'observer.account.domain',
                     'origin.host.domain.name', 'observer.host.domain'],
    'Domain (Impacted)': ['object.domain.name', 'object.url.domain', 'target.account.domain', 'observer.account.domain',
                          'target.host.domain', 'observer.host.domain'],
    'Domain': ['object.domain.name', 'object.url.domain', 'target.account.domain', 'observer.account.domain',
                'target.host.domain', 'observer.host.domain'],
    'NAT TCP/UDP Port (Impacted)': 'target.host.network_port.nat_value',
    'DNATPort': 'target.host.network_port.nat_value',
    'TCP/UDP Port (Impacted)': 'target.host.network_port.value',
    'DPort': 'target.host.network_port.value',
    'NAT TCP/UDP Port (Origin)': 'origin.host.network_port.nat_value',
    'SNATPort': 'origin.host.network_port.nat_value',
    'TCP/UDP Port (Origin)': 'origin.host.network_port.value',
    'SPort': 'origin.host.network_port.value',
    # Other MPE Tab
    'ItemsIn': 'SKIP_FIELD',  # TODO: Validate
    'ItemsOut': 'SKIP_FIELD',  # TODO: Validate
    # Derived Data
    'User Identity (Origin)': 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id / unattributed.account.identity.name for future use
    'User Identity (Impacted)': 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id / unattributed.account.identity.name for future use
    'Recipient Identity': 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id / unattributed.account.identity.name for future use
    'Sender Identity': 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id / unattributed.account.identity.name for future use
    'Duration': 'action.duration',
    'MPE Rule Name': 'SKIP_FIELD',  # TODO: Validate object.rule.name or general_information.processing_information.message_processing_policy_name
    # Range Logic
    "IP Address Range (Origin)": ['unattributed.host.ip_address.value', 'origin.host.ip_address.value',
                                  'observer.host.ip_address.value'],
    "IP Address Range (Impacted)": ['unattributed.host.ip_address.value', 'target.host.ip_address.value',
                                    'observer.host.ip_address.value'],
    "IP Address Range (Origin or Impacted)": ['unattributed.host.ip_address.value', 'target.host.ip_address.value',
                                              'observer.host.ip_address.value', 'origin.host.ip_address.value'],
    "NAT IP Address Range (Impacted)": ['target.host.ip_address.nat_value', 'observer.host.ip_address.nat_value'],
    "NAT IP Address Range (Origin)": ['origin.host.ip_address.nat_value', 'observer.host.ip_address.nat_value'],
    "NAT IP Address Range (Origin or Impacted)": ['origin.host.ip_address.nat_value',
                                                  'observer.host.ip_address.nat_value',
                                                  'target.host.ip_address.nat_value'],
    "TCP/UDP Port Range (Origin)": 'origin.host.network_port.value',
    "TCP/UDP Port Range (Impacted)": 'target.host.network_port.value',
    "TCP/UDP Port Range (Origin or Impacted)": ['origin.host.network_port.value', 'target.host.network_port.value'],
    "NAT TCP/UDP Port Range (Impacted)": 'target.host.network_port.nat_value',
    "NAT TCP/UDP Port Range (Origin)": 'origin.host.network_port.nat_value',
    "NAT TCP/UDP Port Range (Origin or Impacted)": ['origin.host.network_port.nat_value',
                                                    'target.host.network_port.nat_value'],
}

# Mapping between AXON fields and LR7 Fields for Grouping (this map is 1:1)
axon_group_by_mapping = {
    "IDMGroupForAccount": 'SKIP_FIELD',
    "Address": 'SKIP_FIELD',
    "Amount": 'SKIP_FIELD',
    "Application": 'action.network.application',
    "MsgClass": 'SKIP_FIELD', # Unsupported for GroupBy
    "Command": 'action.command',
    "CommonEvent": 'SKIP_FIELD', # Unsupported for GroupBy
    "Direction": 'action.network.direction',
    "Duration": 'action.duration',
    "Group": 'object.group.name',
    "BytesIn": 'action.network.byte_information.received',
    "BytesOut": 'action.network.byte_information.sent',
    "BytesInOut": 'action.network.byte_information.total',
    "DHost": 'target.host.name',
    "Host": 'target.host.name',
    "SHost": 'origin.host.name',
    "ItemsIn": 'SKIP_FIELD',
    "ItemsOut": 'SKIP_FIELD',
    "ItemsInOut": 'SKIP_FIELD',
    "DHostName": 'target.host.name',
    "HostName": 'target.host.name',
    "SHostName": 'origin.host.name',
    "KnownService": 'action.network.application',
    "DInterface": 'target.host.interface.name',
    "Interface": 'target.host.interface.name',
    "SInterface": 'origin.host.interface.name',
    "DIP": 'target.host.ip_address.value',
    'Destination': 'target.host.ip_address.value',
    'Source': 'origin.host.ip_address.value',
    "IP": 'target.host.ip_address.value',
    "SIP": 'origin.host.ip_address.value',
    "DIPRange": 'target.host.ip_address.value',
    "IPRange": 'target.host.ip_address.value',
    "SIPRange": 'origin.host.ip_address.value',
    "KnownDHost": 'SKIP_FIELD',
    "KnownHost": 'SKIP_FIELD',
    "KnownSHost": 'SKIP_FIELD',
    "Location": 'origin.host.location.geo_location',
    "SLocation": 'origin.host.location.geo_location',
    "DLocation": 'target.host.location.geo_location',
    "MsgSource": 'general_information.transit_path.collector_id',
    "Entity": 'SKIP_FIELD',
    "DEntity": 'SKIP_FIELD',
    "SEntity": 'SKIP_FIELD',
    "RootEntity": 'SKIP_FIELD',
    "MsgSourceType": 'general_information.log_source.type_name',
    "DMAC": 'target.host.mac_address',
    "MAC": 'target.host.mac_address',
    "SMAC": 'origin.host.mac_address',
    "Message": 'general_information.raw_message',
    "MPERule": 'SKIP_FIELD',
    "DNATIP": 'target.host.ip_address.nat_value',
    "NATIP": 'target.host.ip_address.nat_value',
    "SNATIP": 'origin.host.ip_address.nat_value',
    "DNATIPRange": 'target.host.ip_address.nat_value',
    "NATIPRange": 'target.host.ip_address.nat_value',
    "SNATIPRange": 'origin.host.ip_address.nat_value',
    "DNATPort": 'target.host.network_port.nat_value',
    "NATPort": 'target.host.network_port.nat_value',
    "SNATPort": 'origin.host.network_port.nat_value',
    "DNATPortRange": 'target.host.network_port.nat_value',
    "NATPortRange": 'target.host.network_port.nat_value',
    "SNATPortRange": 'origin.host.network_port.nat_value',
    "DNetwork": 'SKIP_FIELD',
    "Network": 'SKIP_FIELD',
    "SNetwork": 'SKIP_FIELD',
    "Object": 'object.registry_object.key',
    "ObjectName": 'object.file.name',
    "Login": 'origin.account.name',
    "IDMGroupForLogin": 'object.group.name',
    "Priority": 'SKIP_FIELD',  # TODO: Validate
    "Process": 'object.process.name',
    "PID": 'object.process.id',
    "Protocol": 'action.network.protocol.name',
    "Quantity": 'SKIP_FIELD',  # TODO: Validate
    "Rate": 'SKIP_FIELD',  # TODO: Validate   
    "Recipient": 'target.account.email_address',
    "Sender": 'origin.account.email_address',
    "Session": 'action.session.id',
    "Severity": 'vendor_information.severity',
    "Size": 'object.file.size',
    "Subject": 'object.email_message.subject',
    "DPort": 'target.host.network_port.value',
    "Port": 'target.host.network_port.value',
    "SPort": 'origin.host.network_port.value',
    "DPortRange": 'target.host.network_port.value',
    "PortRange": 'target.host.network_port.value',
    "SPortRange": 'origin.host.network_port.value',
    "URL": 'object.url.complete',
    "Account": 'target.account.name',
    "User": 'origin.account.name',
    "IDMGroupForUser": 'object.group.name',
    "VendorMsgID": 'vendor_information.id',
    "Version": 'object.file.version',
    "SZone": 'SKIP_FIELD',  # TODO: Validate
    "DZone": 'SKIP_FIELD',  # TODO: Validate
    "FilterGroup": 'SKIP_FIELD',  # TODO: Validate
    "PolyListItem": 'SKIP_FIELD',  # TODO: Validate
    "Domain": 'target.account.domain',
    "DomainOrigin": 'origin.account.domain',
    "Hash": 'object.file.hash.md5',
    "Policy": 'object.policy.name',
    "VendorInfo": 'vendor_information.description',
    "Result": 'action.result.message',
    "ObjectType": 'object.type',
    "CVE": 'threat.cve',
    "UserAgent": 'action.user_agent',
    "ParentProcessId": 'object.process.parent_process.id',
    "ParentProcessName": 'object.process.parent_process.name',
    "ParentProcessPath": 'object.process.parent_process.path',
    "SerialNumber": 'object.device.serial_number',
    "Reason": 'action.result.reason',
    "Status": 'threat.run_status',
    "ThreatId": 'threat.id',
    "ThreatName": 'threat.name',
    "SessionType": 'action.session.type',
    "Action": 'action.command',
    "ResponseCode": 'action.result.code',
    "UserOriginIdentityID": 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id
    "Identity": 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.name
    "UserImpactedIdentityID": 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id
    "SenderIdentityID": 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id
    "RecipientIdentityID": 'SKIP_FIELD',  # TODO: Validate unattributed.account.identity.id
    "SLocationRegion": 'origin.host.location.region',
    "DLocationRegion": 'target.host.location.region',
    "VendorMessageID": 'vendor_information.id',
    "Service": 'action.network.application',
    "SLocationCountry": 'origin.host.location.country',
    "DLocationCountry": 'target.host.location.country',
    "SLocationCity": 'origin.host.location.city',
    "DLocationCity": 'target.host.location.city',
    "MsgSourceHost": 'general_information.transit_path.collector_id',
}

# Mapping between Axon common events and LR7 classifications.
axon_classification_mapping = {
    'Startup and Shutdown': 'Status',  # Not a direct 1:1
    'Configuration': 'Configuration Management',
    'Policy': 'Policy management',
    'Account Created': 'Account Created',
    'Account Modified': 'Account Modified',
    'Account Deleted': 'Account Deleted',
    'Access Granted': 'Access Allowed',
    'Access Revoked': 'Access Terminated',
    'Authentication Success': 'Authentication Success',
    'Authentication Failure': 'Authentication Failure',
    'Access Success': 'Access Allowed',
    'Access Failure': 'Access Denied',
    'Other Audit Success': 'Access Allowed',
    'Other Audit Failure': 'Access Denied',
    'Other Audit': 'General Audit',
    'Critical': 'General Critical',
    'Error': 'General Error',
    'Warning': 'General Warning',
    'Information': 'General Information',
    'Network Allow': 'Network Traffic Allowed',
    'Network Deny': 'Network Traffic Denied',
    'Network Traffic': 'Network',
    'Other Operations': 'Status',
    'Compromise': 'Threat Detection',
    'Attack': 'Threat Allowed',
    'Denial of Service': 'Threat Detection',
    'Malware': 'Threat Detection',
    'Suspicious': 'Suspicious Activity',
    'Reconnaissance': 'Threat Detection',
    'Misuse': 'Threat Detection',
    'Activity': 'Threat Detection',
    'Failed Attack': 'Threat Blocked',
    'Failed Denial of Service': 'Threat Detection',
    'Failed Malware': 'Threat Detection',
    'Failed Suspicious': 'Threat Detection',
    'Failed Activity': 'Threat Detection',
    'Other Security': 'General Detection Information',
}


# Array of LR7 List Types to exclude from the lists as they're not supported into Axon
exclude_lr_list_types = ['Location', 'MsgSource', 'MPERule', 'Network', 'Entity', 'RootEntity', 'Identity']


# Mapping between LR7 ListTypes and Axon ListTypes
axon_list_types_mapping = {
    'List': 'PROCESS',
    'Int32': 'INTEGER',
    'String': 'STRING',
    'PortRange': 'PROCESS',
    'IP': 'IP',
    'IPRange': 'PROCESS',
}


# Function to get the AXON field for a given AIE field. Given the fact we can have observer and unattributed fields
# This will allow to specify if we need to include them or not
def get_axon_field_for_key(key, include_observer=False, include_unattributed=False):
    value = axon_mdi_mapping.get(key, None)

    # If the key doesn't exist or maps to SKIP_FIELD, return an empty list and 0
    if value is None or value == 'SKIP_FIELD':
        return [], 0

    # If the value is a string (not a list), we don't care about the include_observer and include_unattributed flags
    if isinstance(value, str):
        value = [value]

    # Apply filters based on the include_observer and include_unattributed flags
    filtered_values = []
    for v in value:
        if include_observer and v.startswith("observer"):
            filtered_values.append(v)
        elif include_unattributed and v.startswith("unattributed"):
            filtered_values.append(v)
        elif not v.startswith("observer") and not v.startswith("unattributed"):
            filtered_values.append(v)

    return filtered_values, len(filtered_values)


# Auxiliar function to validate if the block type is supported by this integration
def is_supported_block_type(name):
    return name in SupportedBlockTypes


# Auxiliar function to validate if the block type is supported by this integration, future use (maybe)
def get_block_type_id(name):
    return SupportedBlockTypes.get(name)
