import pymysql

pymysql.version_info = (2, 2, 1, "final", 0)  # satisfies Django's mysqlclient version check
pymysql.install_as_MySQLdb()