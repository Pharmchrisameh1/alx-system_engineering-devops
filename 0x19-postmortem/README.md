Postmortem - Server Error 500 Incident

Issue Summary

Duration of the outage: June 2, 2024, 11:00 AM - 1:30 PM (GMT+1)

Impact of outage: The website server, operating on a LAMP stack, was completely inaccessible. Each incoming request resulted in an HTTP Status 500 (server error). This outage affected all users, rendering the website entirely unreachable.

Root cause: A typographical error in the wp-settings.php file, where an extra "p" was appended to a file reference, causing it to be "class-wp-locale.phpp" instead of "class-wp-locale.php".

Timeline

11:00 AM - Monitoring systems detected a spike in server errors (HTTP status code 500).
11:05 AM - The on-call engineer initiated an investigation, focusing on recently deployed code.
11:30 AM - Confirmed that the server was operational, but logs indicated multiple 500 errors.
11:45 AM - Database checks revealed no issues; attention shifted to web server configurations.
12:00 PM - Apache2 web server configurations were verified to be error-free.
12:15 PM - Investigation focused on PHP files in the /var/www/html/ directory.
12:30 PM - The engineer began searching for the faulty PHP file.
12:50 PM - Identified the misspelled "class-wp-locale.phpp" reference in the wp-settings.php file.
1:00 PM - Corrected the file reference to "class-wp-locale.php".
1:15 PM - Restarted the Apache2 server.
1:30 PM - Verified that the website was operational and accessible to all users without errors.
Root Cause and Resolution

Root cause: A typographical error in the PHP configuration files. An extra 'p' was appended to the PHP file extension, changing it from ".php" to ".phpp". This prevented the server from locating the correct files, resulting in HTTP 500 errors.

Resolution: The engineer identified and corrected the misspelled file reference in the PHP files, then restarted the Apache2 server.

Corrective and Preventative Measures

Improvements:

Implement stricter code review processes to catch typographical errors.
Enhance monitoring to detect file configuration issues before deployment.
Automate deployment checks to validate file references.
Tasks:

Implement Pre-Deployment Checks: Introduce automated scripts to validate file extensions and configurations before deploying to production.
Enhanced Monitoring: Update monitoring tools to alert on common configuration issues, such as file not found errors.
Documentation: Update deployment and configuration documentation to include this incident and steps to prevent similar issues.
Rollback Plan: Develop a robust rollback strategy to quickly revert changes in case of future misconfigurations.
