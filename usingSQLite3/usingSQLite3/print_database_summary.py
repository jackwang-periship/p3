'''
Created on Mar 14, 2017

@author: jwang02
'''
import sqlite3

def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

def close(conn):
    """ Commit changes and close connection to the database """
    # conn.commit()
    conn.close()

def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    c.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = c.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]

def table_col_info(cursor, table_name, print_out=False):
    """ Returns a list of tuples with column informations:
        (id, name, type, notnull, default_value, primary_key)
    """
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = c.fetchall()

    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info

def values_in_col(cursor, table_name, print_out=True):
    """ Returns a dictionary with columns as keys and the number of not-null
        entries as associated values.
    """
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = c.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        c.execute('SELECT ({0}) FROM {1} WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a better performance than using COUNT
        number_rows = len(c.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return col_dict


if __name__ == '__main__':

    sqlite_file = 'my_first_db.sqlite3'
    table_name = 'my_table_3'

    conn, c = connect(sqlite_file)
    
    print '\n'
    print '==========================='
    print 'my_table_1'
    print '==========================='
    total_rows(c, 'my_table_1', print_out=True)
    table_col_info(c, 'my_table_1', print_out=True)
    values_in_col(c, 'my_table_1', print_out=True) # slow on large data bases

    print '\n'
    print '==========================='
    print 'my_table_2'
    print '==========================='
    total_rows(c, 'my_table_2', print_out=True)
    table_col_info(c, 'my_table_2', print_out=True)
    values_in_col(c, 'my_table_2', print_out=True) # slow on large data bases

    print '\n'
    print '==========================='
    print 'my_table_3'
    print '==========================='
    total_rows(c, 'my_table_3', print_out=True)
    table_col_info(c, 'my_table_3', print_out=True)
    values_in_col(c, 'my_table_3', print_out=True) # slow on large data bases
    
    close(conn)