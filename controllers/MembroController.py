import services.database as db
import models.membro as membro

def Incluir(membro):
    count = db.cursor.execute("""
    INSERT INTO membros (membro, idade, cidade)
    VALUES(?,?,?)""",
    membro.nome, membro.idade, membro.cidade).rowcount
    db.cnxn.commit()

def selecionartodos():
    db.cursor.execute('select * from membros')
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(membro.membro(row[0], row[1], row[2], row[3]))
    return costumerList