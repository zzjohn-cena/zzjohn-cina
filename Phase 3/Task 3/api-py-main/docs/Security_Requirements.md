# Requirements

#- The web API shall ensure the confidentiality of sensitive data during transmission by implementing Transport Layer Security (TLS) with a minimum strength of 128-bit encryption.
#- The web API must verify the integrity of incoming requests and responses using cryptographic mechanisms like HMAC (Hash-based Message Authentication Code) to detect and prevent tampering.
#- User authentication for the web API shall be enforced using a secure and industry-accepted mechanism, such as OAuth 2.0, ensuring that only authorized and authenticated users can access sensitive functionalities.
#- The web API must implement role-based access control (RBAC) to enforce fine-grained authorization policies, ensuring that users have the appropriate permissions to access specific resources and perform certain actions.
#- The web API shall log and maintain a secure audit trail for all significant transactions, including user actions and system events, to support non-repudiation and forensic analysis in case of security incidents.


# # Reference(s)

#- OWASP Transport Layer Protection Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
#- OWASP Cryptographic Storage Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
#- OWASP Authentication Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
#- OWASP Access Control Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
#- OWASP Logging Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)