import sqlite3
from abc import ABC, abstractmethod
from typing import List
from leitura import Leitura

class LeituraDAO(ABC):
    @abstractmethod
    def insere(self, leitura: Leitura):
        pass

    @abstractmethod
    def listarTodos(self):
        pass

class LeituraDAOImplem(LeituraDAO):
    def __init__(self):
        self.database = 'database/leituras.db'
        self.connection = None 

    def _get_connection(self):
        try:
            self.conn = sqlite3.connect(self.database)
            return self.conn
        except (sqlite3.Error, sqlite3.Warning) as e:
            print(f"Ocorreu um erro: {e}")
            return None

    def _close_connection(self):
        self.conn.close()
        

    def listarTodos(self) -> List[Leitura]:
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            sql = """SELECT * FROM leituras"""
            res = cursor.execute(sql)
            return res.fetchall()
        except sqlite3.Error as e:
            conn.rollback()
            conn.close()
        finally:
            cursor.close()
            conn.close()

    def insere(self,leitura: Leitura) -> None:
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            params = (leitura.getTimestamp(),leitura.getSensor(),leitura.getDados())
            sql = """INSERT INTO leituras(timestamp,sensor,dados)
                    VALUES(?,?,?)"""
            cursor.execute(sql,params)
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            conn.close()
        finally:
            cursor.close()
            conn.close()

