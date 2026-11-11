# Authorized source-code review method

1. Establish the repository/ref, written authorization, exclusions, evidence location, and reporting audience. Pin a commit before collecting evidence.
2. Inventory entry points, trust boundaries, sensitive operations, dependencies and configuration using static reads. Do not execute unfamiliar repository scripts merely to inspect them.
3. Trace authentication, authorization, session management, validation, output encoding, file handling, secrets, crypto and dependency trust. Review server-side controls rather than inferring safety from UI behavior.
4. Record a file/line reference and source-to-sink reasoning for each candidate. Label candidates unconfirmed until reviewed. Existing test success is not proof of security.
5. Separate demonstrated weakness, plausible risk, and missing evidence. Describe prerequisites, impact and confidence. Use CWE when justified; do not invent CVSS precision.
6. Suggest minimal remediation and meaningful local regression tests. Actual code changes or dynamic validation require task authorization.
7. Retest against a new pinned commit and document residual risk and limitations.

References: [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/), [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/), [CWE](https://cwe.mitre.org/).
