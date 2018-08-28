import pymysql.cursors

class OpenMySqlDb:
    def __init__(self, db, newSchema=False):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)
        self.connection = connection
        self.newSchema = newSchema
        self.open(db)

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # for insert, return the id of the last row, since that is the row we just added
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # for select, return everything that is fetched from the database
                    result = cursor.fetchall()
                    return result
                else:
                    # if update/delete/others commit the changes and return nothing
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            #finally:
                # close the connection
                # self.connection.close()

    # yong's codes
    def open(self, db):
        if self.newSchema:
            self.query_db("SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;")
            self.query_db("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;")
            self.query_db("SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';")
            self.query_db("CREATE SCHEMA IF NOT EXISTS `" + db + "` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;")
        self.query_db("USE `" + db + "`;")
        self.opened = True
        self.db = db

    def close(self):
        if self.newSchema:
            self.query_db("SET SQL_MODE=@OLD_SQL_MODE;")
            self.query_db("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;")
            self.query_db("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;")
        self.connection.close()
        self.newSchema = False
        self.opened = False
        self.db = ""

    def new_friends_tab(self):
        self.query_db("CREATE TABLE IF NOT EXISTS `friends` (`id` INT NOT NULL AUTO_INCREMENT, `first_name` VARCHAR(45) NULL, `last_name` VARCHAR(45) NULL, `occupation` VARCHAR(45) NULL, `created_at` DATETIME NULL, `updated_at` DATETIME NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;")

def arr_from_qry(dicts, n = 2):
    arr = []
    for dic in dicts:
        for key, val in dic.items():
            if n == 2:
                arr.append(key)
            arr.append(val)
    return arr

def arr_from_dict(dict, n=2):
    arr = []
    for key, val in dict.items():
        if n == 2:
            arr.append(key)
        arr.append(val)
    return arr

def dict_from_arr(arr):
    dict = {}
    for i in range(int(len(arr)/2)):
        dict[arr[2*i]] = arr[2*i+1]
    return dict

def arr_with_percetage(arr):
    sum = 0
    arrnew = []
    for val in arr:
        arrnew.append(val)
    for i in range(len(arrnew)):
        if i % 2 == 1:
            arrnew[i] = int(arrnew[i])
            sum += arrnew[i]
    for i in range(len(arrnew)):
        if i % 2 == 1:
            arrnew[i] = round(arrnew[i]*1000/sum)/10
    return arrnew

