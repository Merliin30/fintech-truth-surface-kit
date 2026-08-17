# Security policy

## Supported versions

The latest version on the default branch is supported.

## Reporting a vulnerability

Please open a private security advisory on GitHub or contact the maintainer through GitHub if you find a vulnerability.

Do not include secrets, customer data, private trading logic, or production credentials in public issues.

## Security scope

This package provides local test helpers. It does not execute trades, connect to financial services, or process customer accounts.

Security-sensitive findings may still include:

- helpers that incorrectly allow fixture data as production truth
- helpers that allow query or cookie tier spoofing
- helpers that fail open on execution-adjacent tests
- documentation that encourages unsafe handling of financial truth surfaces
