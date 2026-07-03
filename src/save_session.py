import paths


class Save_session:
    def check_session(self):
        try:
            with open(paths.SESSION_FILE, "r") as session:
                line = session.read().strip()
                if not line:
                    return False
                return line
        except FileNotFoundError:
            return False

    def save_session(self, login):
        with open(paths.SESSION_FILE, "w") as session:
            session.write(login)

    def clear_session(self):
        with open(paths.SESSION_FILE, "w") as session:
            session.write("")
