class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'santiago'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'escuela'
    MYSQL_UNIX_SOCKET = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'

config = {
    'development': DevelopmentConfig
}
