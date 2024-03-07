import sqlite3

def createTableActor():
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        CREATE TABLE IF NOT EXISTS Actor (
            ActorId Integer Primary Key Autoincrement,
            ActorName Text NOT NULL,
            ActorStatus Integer NOT NULL,
            createAt DateTime DEFAULT current_timestamp
        )
    """

    cursor = dataConnect.cursor()
    cursor.execute(query)

    dataConnect.close()

def insertActor(ActorName, ActorStatus):
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        INSERT INTO Actor (ActorName, ActorStatus) VALUES (?, ?)
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (ActorName, ActorStatus))
    
    dataConnect.commit()
    dataConnect.close()

def updateActor(ActorId, ActorName, ActorStatus):
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        UPDATE Actor SET 
            ActorName = ?,
            ActorStatus = ?
        WHERE ActorId = ?
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (ActorName, ActorStatus, ActorId))
    
    dataConnect.commit()
    dataConnect.close()

def deleteActor(ActorId):
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        DELETE FROM Actor WHERE ActorId = ?
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (ActorId,))
    
    dataConnect.commit()
    dataConnect.close()

def getActorAll():
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        SELECT ActorId, ActorName, ActorStatus FROM Actor
    """

    cursor = dataConnect.cursor()
    ActorList = cursor.execute(query).fetchall()

    dataConnect.close()

    return ActorList

def getActorId(ActorName):
    dataConnect = sqlite3.connect("ActorList.db")

    query = """
        SELECT ActorId FROM Actor WHERE ActorName = ?
    """

    cursor = dataConnect.cursor()
    ActorList = cursor.execute(query, (ActorName,)).fetchone()

    dataConnect.close()

    return ActorList[0]

if __name__ == "__main__":
    createTableActor()