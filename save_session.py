class Save_session:
    def __init__(self):
        pass

    def check_session(self):
        with open("session_file.txt", "r") as session:
            line = session.readlines()
            if line == []:
                return False
            return line[0]

    def save_session(self, login, password):
        with open("session_file.txt", "w") as session:
            session.write(f"{login} {password}")