import sqlite3 as lite


# Next, we create a connection to the database. 
database=('DDM17.db')
con = lite.connect(database) 


with con: 
    # Get a cursor. 
    cur = con.cursor() 


    ######## CREATING THE TABLES   ###########
    command = """DROP TABLE MagTable"""
    cur.execute(command)
    command = """DROP TABLE PhysTable"""
    cur.execute(command)
    command = """CREATE TABLE IF NOT EXISTS {0} (Name varchar(10),
    Ra STRING, Dec STRING, B FLOAT, R FLOAT)""".format('MagTable')
    # Next, actually execute this command. 
    rows = cur.execute(command) 
    # Now that this is working, let us loop over the table entries 
    # and insert these into the table. 

    MagTable_Name = ['V0-001','V0-002','V0-003','V0-004']
    Ra = ['12:34:04.2','12:15:00.0','11:55:43.1','11:32:42.1']
    Dec = ['-00:00:23.4','-14:23:15','-02:34:17.2','-00:01:17.3']
    B = [15.4,15.9,17.2,16.5]
    R = [13.5,13.6,16.8,14.3]

    # Now that this is working, let us loop over the table entries
    # and insert these into the table.
    for i in range ((len(MagTable_Name))):
        command="INSERT OR IGNORE INTO MagTable VALUES('{0}','{1}','{2}',{3},{4}) ".format(MagTable_Name[i],Ra[i],Dec[i],B[i],R[i])
        cur.execute(command)

    command = """CREATE TABLE IF NOT EXISTS '{0}' (Name varchar(10),
    Teff FLOAT, FeH FLOAT)""".format('PhysTable')
    cur.execute(command)
    PhysTable_Name = ['V0-001','V0-002','V0-003']
    Teff = [4501,5321,6600] #Kelvin
    FeH = [0.13,-0.53,-0.32]

    for i in range ((len(PhysTable_Name))):
        command="INSERT OR IGNORE INTO PhysTable VALUES('{0}','{1}','{2}') ".format(PhysTable_Name[i],Teff[i],FeH[i])
        cur.execute(command)

    ######## DONE CREATING THE TABLES ############

    def command(command):
        '''
        executes and print the given command
        '''
        rows = cur.execute(command)
        for row in rows:
            print row

    command_a =""" 
    SELECT Ra,Dec FROM MagTable WHERE B > 16
    """
    # command(command_a)

    #command b is not well defined since not all stars are in both tables..
    command_b = """
    SELECT B, R, Teff, FeH FROM MagTable M, PhysTable P WHERE M.Name = P.Name
    """
    # command(command_b)

    command_c = """
    SELECT B, R, Teff, FeH FROM MagTable M, PhysTable P WHERE M.Name = P.Name AND FeH > 0
    """

    command(command_c)


    command_d = """
    DROP TABLE BR
    """
    command(command_d)
    command_d = """
    CREATE TABLE BR (Name STRING, Ra STRING, Dec STRING, B_minus_R FLOAT)
    """
    command(command_d)
    command_d = """
    INSERT INTO BR SELECT Name,Ra,Dec,B - R FROM MagTable 
    """
    command(command_d)

    command("""SELECT * FROM BR""")
    