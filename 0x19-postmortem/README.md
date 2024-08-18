**INCIDENT POSTMORTEM ON APACHE INTERNAL SERVOR ERROR**

**Issue Summary**
The outage lasted for almost an hour starting at 2.00pm and ending at 2.45pm (EAT)

**Impact of the Outage**
**Status Code 500**
The Apache Server returned a 500 error (server error)
Users were not able to access the requested resource or page, leading to frustration.

**Root Cause**
There was a faulty php extension file that caused the servor error

![Component Image](0x19-postmortem/comp.jpeg)

**Timeline**
The Issue was detected at 1403hrs EAT.

The Issue was detected by Datadog monitoring system by dispalaying an alert message and displaying the error on the dashboard.
We configured Apache for status monitoring by Datadog. Apache was configured to expose the server status by adding the following lines to Apacge Configuartion
     <Location "/server-status">
         SetHandler server-status
         Require host localhost
     </Location>

**Actions taken**
Immediately the outage was detected, the ALX team took corrective measures by first investigating the cause of the outage and working out the solution.

**Debugging Steps taken**

We used tmux in debugging.
tmux (Terminal Multiplexer) is a powerful tool used in debugging and development that allows users to manage multiple terminal sessions from a single window.Started two tmux sessions on two windows. Ran curl commands on window 1 and ran strace on window 2. 
tmux was an essential tool in the debugging process as it allows you to split your terminal into multiple panes, enabling you to run different commands or scripts simultaneously. This is useful for monitoring logs in one pane while executing commands in another.
**What was causing the isssue**
The issue was caused by a typographical error in a php extension file that caused the server Apache server to return a 500 internal server error

**How the Incident wa resolved**
The issue was resolved by fixing the typographical faulty line on the php extension file.

**Corrective and preventive measures taken**

start a tmux session on a window
start another tmux session on another window 
curl on window one
used strace on window 2
strace required as to kknow PID of Apache process as we needed to run strace attached to the Apache PID.
Ran strace on window 2 with apache PIDs.
curl commands on window 1 (Curl -sI 127.0.0.1) gaves us an error message on window 1.
  <error message
  No directory error
sub-file hosting the non-existing file /var/www/html directory
  >
Second curl gave another error on window 2(no such file).
Attaching strace on the other PID we got the same feed.
Closed tmux session (tmux kill-session)
to such for occurance of an intance of .phpp.we used the command "grep -ro "phpp" /var/www/html
this displayed all files that has phpp inside.

We checked them visually to know how to write them wright
vi /var/www/html/wp-includes/js/zxcvbn.min.js:phpp
this gives a compressed file
vi /var/www/html/wp-settings.php
gave us the content of the php file use the command grep -n "php" /var/www/html/wp-settings.php to find the line having the typographical error 
we then wrote a puppet file to fix the php extension resolving the servor error.





Fix Typographical Errors:
TODO: Review and correct all instances of "servor" to "server" in documentation and code.
TODO: Search for and fix any occurrences of ".phpp" in the codebase.


2. Enhance Monitoring:
TODO: Configure Datadog to monitor Apache error logs for 500 Internal Server Errors.
TODO: Set up alerts in Datadog for high error rates (e.g., more than 5 errors in 5 minutes).

3. Improve Apache Configuration:
TODO: Review and optimize Apache configuration settings for performance and error handling.
TODO: Ensure that the server-status endpoint is secured and accessible only to authorized users.

4. Documentation Updates:
TODO: Update the README.md file to include clear instructions on using tmux for debugging.
TODO: Document the steps taken during the incident for future reference.

5. Implement Code Review Process:
TODO: Establish a code review process to catch typographical errors before deployment.
TODO: Create a checklist for code reviews that includes common pitfalls like file extensions and naming conventions.

6. Conduct Post-Incident Review:
TODO: Schedule a meeting with the team to discuss the incident and gather feedback on the response process.
TODO: Document lessons learned and update incident response procedures accordingly.
7. Automate Testing:
TODO: Implement automated tests to catch common errors in PHP files before deployment.
TODO: Set up continuous integration (CI) to run tests on code changes.
8. Enhance Debugging Tools:
TODO: Create a guide for using tmux effectively in debugging sessions.
TODO: Explore additional debugging tools that can be integrated into the workflow


By addressing these tasks, the team can improve the overall reliability and performance of the Apache server and reduce the likelihood of similar incidents in the future.