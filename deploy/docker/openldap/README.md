# Detalhes do conteiner:
*   https://hub.docker.com/r/bitnami/openldap

## Variáveis
The Bitnami Docker OpenLDAP can be easily setup with the following environment variables:

    LDAP_PORT_NUMBER: The port OpenLDAP is listening for requests. Default: 1389 (non privileged port)
    LDAP_ROOT: LDAP database root node of the LDAP tree. Default: dc=example,dc=org
    LDAP_ADMIN_USERNAME: LDAP database admin user. Default: admin
    LDAP_ADMIN_PASSWORD: LDAP database admin password. Default: adminpassword
    LDAP_CONFIG_ADMIN_ENABLED: Whether to create a configuration admin user. Default: no.
    LDAP_CONFIG_ADMIN_USERNAME: LDAP configuration admin user. This is separate from LDAP_ADMIN_USERNAME. Default: admin.
    LDAP_CONFIG_ADMIN_PASSWORD: LDAP configuration admin password. Default: configpassword.
    LDAP_USERS: Comma separated list of LDAP users to create in the default LDAP tree. Default: user01,user02
    LDAP_PASSWORDS: Comma separated list of passwords to use for LDAP users. Default: bitnami1,bitnami2
    LDAP_USER_DC: DC for the users' organizational unit. Default: users
    LDAP_GROUP: Group used to group created users. Default: readers
    LDAP_EXTRA_SCHEMAS: Extra schemas to add, among OpenLDAP's distributed schemas. Default: cosine, inetorgperson, nis
    LDAP_SKIP_DEFAULT_TREE: Whether to skip creating the default LDAP tree based on LDAP_USERS, LDAP_PASSWORDS, LDAP_USER_DC and LDAP_GROUP. Default: no
    LDAP_CUSTOM_LDIF_DIR: Location of a directory that contains LDIF files that should be used to bootstrap the database. Only files ending in .ldif will be used. Default LDAP tree based on the LDAP_USERS, LDAP_PASSWORDS, LDAP_USER_DC and LDAP_GROUP will be skipped when LDAP_CUSTOM_LDIF_DIR is used. When using this will override the usage of LDAP_ROOT,LDAP_USERS, LDAP_PASSWORDS, LDAP_USER_DC and LDAP_GROUP. Default: /ldifs
    LDAP_CUSTOM_SCHEMA_FILE: Location of a custom internal schema file that could not be added as custom ldif file (i.e. containing some structuralObjectClass). Default is /schema/custom.ldif"
    LDAP_ULIMIT_NOFILES: Maximum number of open file descriptors. Default: 1024.
    LDAP_ALLOW_ANON_BINDING: Allow anonymous bindings to the LDAP server. Default: yes.
