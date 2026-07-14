"""
Burp Suite Extension - Custom SQLi Scanner
-------------------------------------------
A Burp Suite extension that passively scans for SQL injection
vulnerabilities by looking for database error messages.

Requirements:
- Jython (Python 2.7 for Burp Suite)
- Burp Suite Professional or Community Edition

Installation:
1. Open Burp Suite
2. Go to Extensions → Add
3. Select Extension Type: Python
4. Set the extension file to this script
5. Click Next to load
"""

from burp import IBurpExtender, IHttpListener, IScannerCheck
import re


class BurpExtender(IBurpExtender, IHttpListener, IScannerCheck):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Custom SQLi Scanner")
        callbacks.registerHttpListener(self)
        callbacks.registerScannerCheck(self)
        print("[*] Custom SQLi Scanner loaded successfully!")

    def doPassiveScan(self, baseRequestResponse):
        """
        Passively scan responses for SQL error patterns.
        This runs automatically on every HTTP response.
        """
        response = baseRequestResponse.getResponse()
        response_str = self._helpers.bytesToString(response)

        # SQL error patterns to detect
        sql_patterns = [
            # MySQL
            r'SQL syntax.*MySQL',
            r'Warning.*mysql_',
            r'MySQLSyntaxErrorException',
            r'valid MySQL result',
            r'MySqlClient\.',

            # PostgreSQL
            r'PostgreSQL.*ERROR',
            r'Warning.*pg_',
            r'valid PostgreSQL result',
            r'Npgsql\.',
            r'PG::SyntaxError',

            # Microsoft SQL Server
            r'Driver.*SQL[\-\_\ ]*Server',
            r'OLE DB.*SQL Server',
            r'\bSQL Server[^&lt;&quot;]+Driver',
            r'Warning.*mssql_',
            r'\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}',

            # Oracle
            r'\bORA-[0-9][0-9][0-9][0-9]',
            r'Oracle error',
            r'Oracle.*Driver',
            r'Warning.*oci_',
            r'Warning.*ora_',

            # SQLite
            r'SQLite/JDBCDriver',
            r'SQLite\.Exception',
            r'System\.Data\.SQLite\.SQLiteException',
            r'Warning.*sqlite_',
            r'Warning.*SQLite3::',
            r'\[SQLITE_ERROR\]',

            # Generic
            r'SQL syntax error',
            r'Syntax error.*in query',
            r'Unclosed quotation mark',
            r'Incorrect syntax near',
            r'Unexpected end of SQL command',
            r'Invalid column name',
        ]

        # Check response for SQL errors
        for pattern in sql_patterns:
            if re.search(pattern, response_str, re.IGNORECASE):
                # Found potential SQL error - report it
                issue = self._callbacks.buildHttpRequestResponse(
                    baseRequestResponse.getRequest(),
                    baseRequestResponse.getResponse(),
                    baseRequestResponse.getHttpService()
                )
                return [issue]

        return []

    def doActiveScan(self, baseRequestResponse, insertionPoint):
        """
        Active scan hook (called when actively scanning).
        """
        return []

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        """
        Consolidate duplicate issues to avoid flooding.
        """
        if existingIssue.getUrl() == newIssue.getUrl():
            return -1  # Keep existing issue
        return 0  # Both issues are different


# Extension loaded message
print("[*] SQLi Scanner Extension loaded. Active on all responses.")
